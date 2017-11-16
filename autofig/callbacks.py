from matplotlib import backend_bases, collections, lines
from mpl_toolkits.mplot3d import Axes3D

import numpy as np


class Callbacks(object):
    def __init__(self, parent):
        # parent should be Axes or Figure instance
        self.parent = parent
        self._artists = {}

    def connect(self, afevent, artist, mplevent, callback):
        self.parent.callbacks.connect(mplevent, callback)
        # if callback in self.parent.callbacks.callbacks.get(event, {}):

        print "connecting callback:", afevent
        if afevent not in self._artists.keys():
            self._artists[afevent] = []

        self._artists[afevent].append(artist)

    def get_artists(self, callback):
        if not isinstance(callback, str):
            # then maybe we were based the callable itself
            callback = callback.__name__

        return self._artists.get(callback, [])


def _connect_to_autofig(afobj, mplobj):
    if not hasattr(mplobj, '_af'):
        print "connecting to autofig", mplobj
        mplobj._af = afobj
        mplobj._af_callbacks = Callbacks(mplobj)


##################### BEGIN AVAILABLE CALLBACKS ################################

def update_indep(artist, call):
    def callback_key_event(event):
        if event.key == 'i':
            callback_event(event)

    def callback_event(event):
        axes = event.inaxes
        if axes is None:
            return

        if isinstance(axes, Axes3D):
            # xdata and ydata will likely be meaningless
            return

        afaxes = axes._af
        if afaxes.i.reference == 'x':
            i = event.xdata
        elif afaxes.i.reference == 'y':
            i = event.ydata

        for artist in axes._af_callbacks.get_artists('update_indep'):
            if not hasattr(artist, '_af'):
                continue

            call = artist._af

            # TODO: need to clear artists from call and redraw with i=i
            print "*** new i=", i

    raise NotImplementedError
    artist.axes.figure.canvas._af_callbacks.connect('update_indep', artist, 'button_press_event', callback_event)
    artist.axes.figure.canvas._af_callbacks.connect('update_indep', artist, 'key_press_event', callback_key_event)

def update_sizes(artist, call):
    def callback_canvas(event):
        for axes in event.canvas.figure.axes:
            callback_axes(axes)

        return

    def callback_axes(ax):
        if not hasattr(ax, '_af_callbacks'):
            print "skipping axes (no _af_callbacks)", ax
            return


        for artist in ax._af_callbacks.get_artists('update_sizes'):
            if not hasattr(artist, '_af'):
                print "skipping artist (no _af)", artist
                continue

            call = artist._af

            if not hasattr(call, 'size_scale'):
                print "skipping call (no size_scale)", call
                continue

            # TODO: move this logic inside Call/Plot??
            split = call.size_scale.split(':')
            size_scale_dims = split[0]
            size_scale_mode = split[1] if len(split) > 1 else 'noresize'

            if size_scale_mode == 'noresize':
                if hasattr(ax, '_af_update_size_draw_complete'):
                    return
                else:
                    ax._af_update_size_draw_complete = True
                    size_scale_mode = 'current'

            if size_scale_mode == 'current':
                xlim = ax.get_xlim()
                ylim = ax.get_ylim()
            elif size_scale_mode == 'original':
                # TODO: need to pass i
                xlim = call.axes.x.get_lim()
                ylim = call.axes.y.get_lim()
            else:
                raise NotImplementedError

            # print "update_sizes for artist:", artist, size_scale_dims, size_scale_mode

            xr_disp = ax.transData.transform([float(max(xlim)), 0])
            xl_disp = ax.transData.transform([float(min(xlim)), 0])

            yt_disp = ax.transData.transform([0, float(max(ylim))])
            yb_disp = ax.transData.transform([0, float(min(ylim))])

            w_disp = abs(xr_disp[0] - xl_disp[0])
            h_disp = abs(yt_disp[1] - yb_disp[1])


            if size_scale_dims == 'x':
                a_disp = w_disp**2
            elif size_scale_dims == 'y':
                a_disp = h_disp**2
            elif size_scale_dims == 'xy':
                a_disp = w_disp * h_disp
            else:
                raise NotImplementedError

            # print "a_disp", a_disp

            # TODO: need to pass i
            sizes_orig = call.s.get_value(i=None, unit=call.axes_s.unit if call.axes_s is not None else None)
            if sizes_orig is None:
                continue

            if isinstance(artist, collections.PathCollection):
                sizes = sizes_orig**2 * a_disp / 1.23
                artist.set_sizes(sizes)
            elif isinstance(artist, lines.Line2D):
                ms = sizes_orig * np.sqrt(a_disp) / 1.11
                lw = sizes_orig * np.sqrt(a_disp) / 1.11
                # print "setting markersize/linewidth: ", ms
                artist.set_markersize(ms)
                artist.set_linewidth(lw)
            elif isinstance(artist, collections.LineCollection):
                lw = sizes_orig * np.sqrt(a_disp) / 1.11
                artist.set_linewidths(lw)
            else:
                raise NotImplementedError("rescale_sizes not implemented for artist-type: {}".format(type(artist)))

        return

    artist.axes.figure.canvas._af_callbacks.connect('update_sizes', artist, 'resize_event', callback_canvas)

    artist.axes._af_callbacks.connect('update_sizes', artist, 'xlim_changed', callback_axes)
    artist.axes._af_callbacks.connect('update_sizes', artist, 'ylim_changed', callback_axes)
