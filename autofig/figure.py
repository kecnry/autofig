import numpy as np
import astropy.units as u
import matplotlib.pyplot as plt

from matplotlib import animation

from . import common
from . import call as _call
from . import axes as _axes
from . import mpl_animate as _mpl_animate

class Figure(object):
    def __init__(self, *args):
        self._backend_object = None
        self._backend_artists = []
        self._axes = []
        self._calls = []

        for ca in args:
            if isinstance(ca, _axes.Axes):
                self.add_axes(ca)
            elif isinstance(ca, _call.Call):
                self.add_call(ca)
            else:
                raise TypeError("all arguments must be of type Call or Axes")

    def __repr__(self):
        naxes = len(self.axes)
        ncalls = len(self.calls)
        return "<Figure | {} axes | {} call(s)>".format(naxes, ncalls)

    @property
    def axes(self):
        return self._axes

    def add_axes(self, *axes):
        if len(axes) > 1:
            for a in axes:
                self.add_axes(a)
            return

        elif len(axes) == 1:
            if not isinstance(axes, _axes.Axes):
                raise TypeError("axes must be of type Axes")


            self._axes.append(axes)
            for call in axes.calls:
                self._calls.append(call)

    @property
    def calls(self):
        return self._calls

    def add_call(self, *calls):
        if len(calls) > 1:
            for c in calls:
                self.add_call(c)
            return

        elif len(calls) == 1:
            call = calls[0]
            if not isinstance(call, _call.Call):
                raise TypeError("call must be of type Call")

            # try to add to existing axes in reverse order before making a new one
            for ax in reversed(self.axes):
                consistent, reason = ax.consistent_with_call(call)
                if consistent:
                    break
            else:
                # then no axes were consistent so we must add a new one
                ax = _axes.Axes()
                self._axes.append(ax)

            ax.add_call(call)
            self._calls.append(call)

    def _get_backend_object(self, fig=None):
        if fig is None:
            if self._backend_object:
                fig = self._backend_object
            else:
                fig = plt.gcf()
                fig.clf()
                self._backend_artists = []

        self._backend_object = fig
        return fig

    def _get_backend_artists(self):
        return self._backend_artists

    def plot(self, *args, **kwargs):
        """
        """

        tight_layout = kwargs.pop('tight_layout', True)
        show = kwargs.pop('show', False)
        save = kwargs.pop('save', False)

        call = _call.Plot(*args, **kwargs)
        self.add_call(call)
        return self.draw(calls=[call], tight_layout=tight_layout, show=show, save=save)

    def mesh(self, *args, **kwargs):
        """
        """

        tight_layout = kwargs.pop('tight_layout', True)
        show = kwargs.pop('show', False)
        save = kwargs.pop('save', False)

        call = _call.Mesh(*args, **kwargs)
        self.add_call(call)
        return self.draw(calls=[call], tight_layout=tight_layout, show=show, save=save)

    # def show(self):
    #     plt.show()

    def reset_draw(self):
        # TODO: figure options like figsize, etc
        self._get_backend_object(fig=plt.figure())

    def draw(self, fig=None, i=None, calls=None,
             tight_layout=True, show=False, save=False):

        fig = self._get_backend_object(fig)

        if calls is None:
            # then we need to reset the backend figure.  This is especially
            # important when passing draw(i=something)
            fig.clf()

        for axesi in self.axes:
            if axesi._backend_object not in fig.axes:
                # then axes doesn't have a subplot yet.  Adding one will also
                # shift the location of all axes already drawn/created.
                ax = axesi.append_subplot(fig=fig)
                # if axesi._backend_object already existed (but maybe on a
                # different figure) it will be reset on the draw call below.
            else:
                # then this axes already has a subplot on the figure, so we'll
                # allow it to default to that instance
                ax = None

            axesi.draw(ax=ax, i=i, calls=calls, show=False, save=False)

            self._backend_artists += axesi._get_backend_artists()

        if tight_layout:
            fig.tight_layout()

        if save:
            fig.savefig(save)

        if show:
            # TODO: allow top-level option for whether to block or not?
            plt.show()  # <-- blocking
            # fig.show()  #<-- not blocking

        if show or save:
            self.reset_draw()
            return None
        else:
            return fig

    def animate(self, fig=None, indeps=None,
                tight_layout=True, show=False, save=False, save_kwargs={}):

        if indeps is None:
            # TODO: can we get i from the underlying Axes/Calls?
            raise NotImplementedError()


        interval = 100 # time interval in ms between each frame
        blit = False # TODO: set this to True if no Mesh calls?

        ao = _mpl_animate.Animation(self, indeps)
        anim = animation.FuncAnimation(ao.mplfig, ao, fargs=(),\
                init_func=ao.anim_init, frames=indeps, interval=interval,\
                blit=blit)

        if show:
            plt.show()

        if save:
            anim.save(save, **save_kwargs)

        return anim
