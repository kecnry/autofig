import numpy as np
import astropy.units as u
import matplotlib.pyplot as plt

from . import common
from . import call as _call
from . import axes as _axes

class Figure(object):
    def __init__(self, *calls):
        self._axes = []
        self._calls = []

        self.add_call(*calls)

    def __repr__(self):
        naxes = len(self.axes)
        ncalls = len(self.calls)
        return "<Figure | {} axes | {} call(s)>".format(naxes, ncalls)

    @property
    def axes(self):
        return self._axes

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

    def draw(self, fig=None, tight_layout=True, show=False, save=False):

        if fig is None:
            fig = plt.gcf()

        for axesi in self.axes:
            ax = axesi.append_subplot(fig=fig)
            axesi.draw(ax=ax, show=False, save=False)

        if tight_layout:
            fig.tight_layout()

        if show:
            plt.show()

        if save:
            plt.savefig(save)
