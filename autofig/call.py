import numpy as np
import astropy.units as u
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import LineCollection, PolyCollection
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from . import common

def _map_none(value):
    if isinstance(value, str):
        if value.lower() == 'none':
            return 'None'
        else:
            return value
    elif value is None:
        return 'None'
    else:
        return value

class Call(object):
    def __init__(self, i=None, iunit=None,
                       x=None, xerror=None, xunit=None, xlabel=None,
                       y=None, yerror=None, yunit=None, ylabel=None,
                       z=None, zerror=None, zunit=None, zlabel=None,
                       consider_for_limits=True,
                       **kwargs):
        """
        """
        self._axes = None
        self._backend_objects = []

        self._x = CallDimensionX(self, x, xerror, xunit, xlabel)
        self._y = CallDimensionY(self, y, yerror, yunit, ylabel)
        self._z = CallDimensionZ(self, z, zerror, zunit, zlabel)

        # defined last so all other dimensions are in place in case indep
        # is a reference and needs to access units, etc
        self._i = CallDimensionI(self, i, iunit)

        self.consider_for_limits = consider_for_limits

        map_none_kwargs = ['linestyle', 'ls', 'marker']
        self.kwargs = {k: _map_none(v) if k in map_none_kwargs else v for k,v in kwargs.items()}

        # TODO: add style

    def _get_backend_object():
        return self._backend_artists

    @property
    def axes(self):
        # no setter as this can only be set internally when attaching to an axes
        return self._axes

    @property
    def figure(self):
        # no setter as this can only be set internally when attaching to an axes
        if self.axes is None:
            return None
        return self.axes.figure

    @property
    def i(self):
        return self._i

    @property
    def indep(self):
        return self.i

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @property
    def consider_for_limits(self):
        return self._consider_for_limits

    @consider_for_limits.setter
    def consider_for_limits(self, consider):
        if not isinstance(consider, bool):
            raise TypeError("consider_for_limits must be of type bool")

        self._consider_for_limits = consider

class Plot(Call):
    def __init__(self, i=None, iunit=None,
                       x=None, xerror=None, xunit=None, xlabel=None,
                       y=None, yerror=None, yunit=None, ylabel=None,
                       z=None, zerror=None, zunit=None, zlabel=None,
                       s=None, sunit=None, slabel=None,
                       c=None, cunit=None, clabel=None, cmap=None,
                       highlight=True, uncover=False,
                       consider_for_limits=True,
                       **kwargs):
        """
        marker
        markersize / ms
        linestyle / ls
        linewidth / lw
        color


        highlight_marker
        highlight_markersize / highlight_ms
        highlight_color
        """
        self._s = CallDimensionS(self, s, None, sunit, slabel)
        self._c = CallDimensionC(self, c, None, cunit, clabel, cmap=cmap)

        # TODO: do the same for size??
        self._axes_c = None

        self.highlight = highlight
        self.uncover = uncover

        super(Plot, self).__init__(i=i, iunit=iunit,
                                   x=x, xerror=xerror, xunit=xunit, xlabel=xlabel,
                                   y=y, yerror=yerror, yunit=yunit, ylabel=ylabel,
                                   z=z, zerror=zerror, zunit=zunit, zlabel=zlabel,
                                   consider_for_limits=consider_for_limits,
                                   **kwargs
                                   )

    def __repr__(self):
        dirs = []
        for direction in ['i', 'x', 'y', 'z', 's', 'c']:
            if getattr(self, direction).value is not None:
                dirs.append(direction)

        return "<Call:Plot | dims: {}>".format(", ".join(dirs))

    @property
    def axes_c(self):
        # currently no setter as this really should be handle by axes.add_call
        return self._axes_c

    @property
    def highlight(self):
        return self._highlight

    @highlight.setter
    def highlight(self, highlight):
        if not isinstance(highlight, bool):
            raise TypeError("highlight must be of type bool")

        self._highlight = highlight

    @property
    def uncover(self):
        return self._uncover

    @uncover.setter
    def uncover(self, uncover):
        if not isinstance(uncover, bool):
            raise TypeError("uncover must be of type bool")

        self._uncover = uncover

    @property
    def s(self):
        return self._s

    @property
    def size(self):
        return self.s

    @property
    def c(self):
        return self._c

    @property
    def color(self):
        return self.c

    def draw(self, ax=None, i=None):
        if ax is None:
            ax = plt.gca()
        else:
            if not isinstance(ax, plt.Axes):
                raise TypeError("ax must be of type plt.Axes")

        # determine 2D or 3D
        axes_3d = isinstance(ax, Axes3D)

        kwargs = self.kwargs.copy()

        # marker
        marker = kwargs.pop('marker', '.')

        # markersize - 'markersize' has priority over 'ms'
        ms_ = kwargs.pop('ms', None)
        ms = kwargs.pop('markersize', ms_)

        # linestyle - 'linestyle' has priority over 'ls'
        ls_ = kwargs.pop('ls', 'solid')
        ls = kwargs.pop('linestyle', ls_)

        # linewidth - 'linewidth' has priority over 'lw'
        lw_ = kwargs.pop('lw', None)
        lw = kwargs.pop('linewidth', lw_)

        # color - 'color' has priority over 'c' over dimension color
        if isinstance(self.c.value, str):
            color_from_dim = self.c.value
        else:
            color_from_dim = None
        color = kwargs.pop('color', color_from_dim)

        # highlight styling
        highlight_marker = kwargs.pop('highlight_marker', 'o')
        highlight_ms_ = kwargs.pop('highlight_ms', None)
        highlight_ms = kwargs.pop('highlight_markersize', highlight_ms_)
        highlight_color = kwargs.pop('highlight_color', 'k')

        # PLOTTING
        return_artists = []
        # TODO: handle getting in correct units (possibly passed from axes?)
        x = self.x.get_value(i=i)
        xerr = self.x.get_error(i=i)
        y = self.y.get_value(i=i)
        yerr = self.y.get_error(i=i)
        c = self.c.get_value(i=i)

        if axes_3d:
            z = self.z.get_value(i=i)
            zerr = self.z.get_error(i=i)

            data = (x, y, z)
        else:
            zerr = None

            data = (x, y)

        # PLOT ERRORS, if applicable
        # TODO: match colors?... just by passing ecolor=color?
        if xerr or yerr or zerr:
            artists = ax.errorbar(*data,
                                   fmt='', linestyle='None',
                                   xerr=xerr,
                                   yerr=yerr,
                                   zerr=zerr,
                                   ecolor='k')

            return_artists += artists

        # PLOT DATA
        do_colorscale = c is not None and not isinstance(c, str)

        if do_colorscale and ls.lower() != 'none':
            # print("attempting to plot colored lines with cmap: {}".format(self.axes_c.cmap if self.axes is not None else None))
            # handle line with color changing
            # TODO: scale according to colorlimits
            if axes_3d:
                points = np.array([x, y, z]).T.reshape(-1, 1, 3)
            else:
                points = np.array([x, y]).T.reshape(-1, 1, 2)

            segments = np.concatenate([points[:-1], points[1:]], axis=1)

            # TODO: pass cmap
            # TODO: scale according to colorlimits (especially important since c can be filtered by i)
            lc = LineCollection(segments,
                norm=self.axes_c.get_norm(i=i) if self.axes_c is not None else None,
                cmap=self.axes_c.cmap if self.axes_c is not None else None,
                linestyle=ls, linewidth=lw)
            lc.set_array(c)


            return_artists.append(lc)
            ax.add_collection(lc)

        if do_colorscale and marker.lower() != 'none':
            # print("attempting to plot colored markers with cmap: {}".format(self.axes_c.cmap if self.axes is not None else None))
            # TODO: scale according to colorlimits (especially important since c can be filtered by i)
            artist = ax.scatter(*data, c=c,
                norm=self.axes_c.get_norm(i=i) if self.axes_c is not None else None,
                cmap=self.axes_c.cmap if self.axes_c is not None else None,
                marker=marker, s=10 if ms is None else ms**2,
                linewidths=0) # linewidths=0 removes the black edge

            return_artists.append(artist)

        if not do_colorscale:
            artists = ax.plot(*data,
                              marker=marker, ms=ms,
                              ls=ls, lw=lw,
                              color=color,
                              **kwargs)

            return_artists += artists

        if self.highlight and i is not None:
            if axes_3d:
                highlight_data = (self.x.interpolate_at_i(i),
                                  self.y.interpolate_at_i(i),
                                  self.z.interpolate_at_i(i))
            else:
                highlight_data = (self.x.interpolate_at_i(i),
                                  self.y.interpolate_at_i(i))

            # TODO: highlight formatting - highlight_marker, highlight_color,
            # highlight_ms (and highlight_markersize).  Will probably need
            # to pop these all from the kwargs earlier and pass on below
            artists = ax.plot(*highlight_data,
                              marker=highlight_marker, ms=highlight_ms,
                              ls='None', color=highlight_color)

            return_artists += artists

        self._backend_objects = return_artists

        return return_artists


class Mesh(Call):
    def __init__(self, i=None, iunit=None,
                       x=None, xerror=None, xunit=None, xlabel=None,
                       y=None, yerror=None, yunit=None, ylabel=None,
                       z=None, zerror=None, zunit=None, zlabel=None,
                       fc=None, fcunit=None, fclabel=None,
                       ec=None, ecunit=None, eclabel=None,
                       consider_for_limits=True,
                       **kwargs):
        """
        """

        self._fc = CallDimensionC(self, fc, None, fcunit, fclabel)
        self._ec = CallDimensionC(self, ec, None, ecunit, eclabel)

        super(Mesh, self).__init__(i=i, iunit=iunit,
                                   x=x, xerror=xerror, xunit=xunit, xlabel=xlabel,
                                   y=y, yerror=yerror, yunit=yunit, ylabel=ylabel,
                                   z=z, zerror=zerror, zunit=zunit, zlabel=zlabel,
                                   consider_for_limits=consider_for_limits,
                                   **kwargs
                                   )

    def __repr__(self):
        dirs = []
        for direction in ['i', 'x', 'y', 'z', 'fc', 'ec']:
            if getattr(self, direction).value is not None:
                dirs.append(direction)

        return "<Call:Mesh | dims: {}>".format(", ".join(dirs))

    @property
    def fc(self):
        return self._fc

    @property
    def facecolor(self):
        return self.fc

    @property
    def ec(self):
        return self._ec

    @property
    def edgecolor(self):
        return self.ec

    def draw(self, ax=None):
        raise NotImplementedError


class CallDimension(object):
    def __init__(self, direction, call, value, error=None, unit=None, label=None):
        self._call = call
        self.direction = direction
        # unit must be set before value as setting value pulls the appropriate
        # unit for CallDimensionI
        self.unit = unit
        self.value = value
        self.error = error
        self.label = label
        # self.lim = lim

    def __repr__(self):

        return "<{} | len: {} | type: {} | label: {}>".format(self.direction,
                                       len(self.value) if self.value is not None else 'n/a',
                                       self.unit.physical_type,
                                       self.label)

    @property
    def call(self):
        return self._call

    @property
    def direction(self):
        """
        access the direction
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        set the direction
        """
        if not isinstance(direction, str):
            raise TypeError("direction must be of type str")

        accepted_values = ['i', 'x', 'y', 'z', 's', 'c']
        if direction not in accepted_values:
            raise ValueError("must be one of: {}".format(accepted_values))

        self._direction = direction

    def interpolate_at_i(self, i):
        """
        access the interpolated value at a give value of i (independent-variable)
        """
        if len(self.call.i.value) != len(self._value):
            raise ValueError("length mismatch with independent-variable")

        return np.interp(i, self.call.i.value, self._value)

    def get_value(self, i=None):
        """
        access the value for a given value of i (independent-variable) depending
        on which effects (i.e. uncover) are enabled.
        """
        if i is None:
            return self._value

        if self._value is None:
            return None

        if self.call.uncover:
            return np.append(self._value[self.call.i.value <= i],
                             np.array([self.interpolate_at_i(i)]))
        else:
            return self._value


    # for value we need to define the property without decorators because of
    # this: https://stackoverflow.com/questions/13595607/using-super-in-a-propertys-setter-method-when-using-the-property-decorator-r
    # and the need to override these in the CallDimensionI class
    def _get_value(self):
        """
        access the value
        """
        return self.get_value(i=None)

    def _set_value(self, value):
        """
        set the value
        """
        if value is None:
            self._value = value
            return

        # handle casting to acceptable types
        if isinstance(value, list) or isinstance(value, tuple):
            value = np.array(value)
        if isinstance(value, int):
            value = float(value)

        # handle setting based on type
        if isinstance(value, np.ndarray):
            self._value = value
        elif isinstance(value, float):
            # TODO: do we want to cast to np.array([value])??
            # this will most likely be used for axhline/axvline
            self._value = value
        # elif isinstance(value, str):
            # TODO: then need to pull from the bundle??? Or will this happen
            # at a higher level
        elif self.direction=='c' and isinstance(value, str):
            self._value = value
        else:
            raise TypeError("value must be of type array (or similar)")

    value = property(_get_value, _set_value)

    def get_error(self, i=None):
        """
        access the error for a given value of i (independent-variable) depending
        on which effects (i.e. uncover) are enabled.
        """
        if i is None:
            return self._error

        if self._error is None:
            return None

        if self.call.uncover:
            return np.append(self._value[self.call.i.value <= i],
                             np.array([np.nan]))
        else:
            return self._value

    @property
    def error(self):
        """
        access the error
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        set the error
        """
        # TODO: check length with value?
        # TODO: type checks (similar to value)
        if self.direction not in ['x', 'y', 'z'] and error is not None:
            raise ValueError("error only accepted for x, y, z dimensions")

        self._error = error

    @property
    def unit(self):
        """
        access the unit
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        set the unit
        """
        unit = common._convert_unit(unit)
        self._unit = unit

    @property
    def label(self):
        """
        access the label
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        set the label
        """
        if self.direction in ['i'] and label is not None:
            raise ValueError("label not accepted for indep dimension")


        if label is None:
            self._label = label
            return

        if not isinstance(label, str):
            try:
                label = str(label)
            except:
                raise TypeError("label must be of type str")

        self._label = label


class CallDimensionI(CallDimension):
    def __init__(self, *args):
        super(CallDimensionI, self).__init__('i', *args)

    @property
    def value(self):
        """
        access the value
        """
        if isinstance(self._value, str):
            dimension = self._value
            return getattr(self.call, dimension).value

        return super(CallDimensionI, self)._get_value()

    @value.setter
    def value(self, value):
        """
        set the value
        """
        # for the indep direction we also allow a string which points to one
        # of the other available dimensions
        # TODO: support c, fc, ec?
        if isinstance(value, common.basestring) and value in ['x', 'y', 'z']:
            # we'll cast just to get rid of any python2 unicodes
            self._value  = str(value)
            dimension = value
            self._unit = getattr(self.call, dimension).unit
            return

        # NOTE: cannot do super on setter directly, see this python
        # bug: https://bugs.python.org/issue14965 and discussion:
        # https://mail.python.org/pipermail/python-dev/2010-April/099672.html
        super(CallDimensionI, self)._set_value(value)

    @property
    def is_reference(self):
        """
        whether referencing another dimension or its own
        """
        return isinstance(self._value, str)

    @property
    def reference(self):
        """
        reference (will return None if not is_reference)
        """
        if self.is_reference:
            return self._value

        else:
            return None

class CallDimensionX(CallDimension):
    def __init__(self, *args):
        super(CallDimensionX, self).__init__('x', *args)

class CallDimensionY(CallDimension):
    def __init__(self, *args):
        super(CallDimensionY, self).__init__('y', *args)

class CallDimensionZ(CallDimension):
    def __init__(self, *args):
        super(CallDimensionZ, self).__init__('z', *args)

class CallDimensionS(CallDimension):
    def __init__(self, *args):
        super(CallDimensionS, self).__init__('s', *args)

class CallDimensionC(CallDimension):
    def __init__(self, call, value, error=None, unit=None, label=None, cmap=None):

        self.cmap = cmap
        super(CallDimensionC, self).__init__('c', call, value, error, unit,
                                             label)

    @property
    def cmap(self):
        return self._cmap

    @cmap.setter
    def cmap(self, cmap):
        # print("setting call cmap: {}".format(cmap))
        try:
            cmap = plt.get_cmap(cmap)
        except:
            raise TypeError("could not find cmap")

        self._cmap = cmap
