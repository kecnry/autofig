import numpy as np
import astropy.units as u
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

from . import common

class Call(object):
    def __init__(self, i=None, iunit=None,
                       x=None, xerror=None, xunit=None, xlabel=None,
                       y=None, yerror=None, yunit=None, ylabel=None,
                       z=None, zerror=None, zunit=None, zlabel=None,
                       consider_for_limits=True,
                       **kwargs):
        """
        """
        self._backend_objects = []

        self._x = DimensionX(self, x, xerror, xunit, xlabel)
        self._y = DimensionY(self, y, yerror, yunit, ylabel)
        self._z = DimensionZ(self, z, zerror, zunit, zlabel)

        # defined last so all other dimensions are in place in case indep
        # is a reference and needs to access units, etc
        self._i = DimensionI(self, i, iunit)

        self.consider_for_limits = consider_for_limits

        self.kwargs = kwargs

        # TODO: add style

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
                       c=None, cunit=None, clabel=None,
                       consider_for_limits=True,
                       **kwargs):
        """
        """
        self._s = DimensionS(self, s, None, sunit, slabel)
        self._c = DimensionColor(self, c, None, cunit, clabel)

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

    def draw(self, ax=None):
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
        ms = kwargs.pop('markersize', kwargs.pop('ms', None))

        # linestyle - 'linestyle' has priority over 'ls'
        ls = kwargs.pop('linestyle', kwargs.pop('ls', 'None'))

        # linewidth - 'linewidth' has priority over 'lw'
        lw = kwargs.pop('linewidth', kwargs.pop('lw', None))

        # color
        color = kwargs.pop('color', None)

        # PLOTTING
        return_artists = []
        # TODO: handle getting in correct units (possibly passed from axes?)
        x = self.x.value
        y = self.y.value
        z = self.z.value
        c = self.c.value

        if axes_3d:
            data = (x, y, z)
        else:
            data = (x, y)

        # PLOT ERRORS, if applicable
        # TODO: match colors?
        if axes_3d:
            if self.x.error or self.y.error or self.z.error:
                artists = ax.errorbar(*data,
                                       fmt='', linestyle='None',
                                       xerr=self.x.error,
                                       yerr=self.y.error,
                                       zerr=self.z.error,
                                       ecolor='k')

                return_artists += artists
        else:
            if self.x.error or self.y.error:
                artists = ax.errorbar(*data,
                                       fmt='', linestyle='None',
                                       xerr=self.x.error,
                                       yerr=self.y.error,
                                       ecolor='k')

                return_artists += artists

        # PLOT DATA
        if c and ls.lower() is not 'none':
            # handle line with color changing
            if axes_3d:
                points = np.array([x, y, z]).T.reshape(-1, 1, 3)
            else:
                points = np.array([x, y]).T.reshape(-1, 1, 2)

            segments = np.concatenate([points[:-1], points[1:]], axis=1)

            # TODO: pass cmap
            # TODO: scale according to colorlimits
            lc = LineCollection(segments,
                norm=plt.Normalize(min(c), max(c)),
                ls=ls, lw=lw,
                **kwargs)
            lc.set_array(c)
            return_artists.append(lc)
            ax.add_collection(lc)

        if c and marker.lower() is not None:
            # TODO: pass cmap
            # TODO: scale according to colorlimits
            artist = ax.scatter(*data, c=c,
                norm=plt.Normalize(min(c), max(c)),
                marker=marker, ms=ms,
                linewidths=0) # linewidths=0 removes the black edge

            return_artists.append(artist)

        if not c:
            artists = ax.plot(*data,
                              marker=marker, ms=ms,
                              ls=ls, lw=lw,
                              color=color,
                              **kwargs)

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

        self._fc = DimensionColor(self, fc, None, fcunit, fclabel)
        self._ec = DimensionColor(self, ec, None, ecunit, eclabel)

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


class Dimension(object):
    def __init__(self, direction, call, value, error=None, unit=None, label=None):
        self._direction = None
        self._value = None
        self._error = None
        self._unit = None
        self._label = None
        # self._lim = None

        self._call = call
        self.direction = direction
        # unit must be set before value as setting value pulls the appropriate
        # unit for DimensionI
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

        accepted_values = ['i', 'x', 'y', 'z', 's', 'color', 'markersize']
        if direction not in accepted_values:
            raise ValueError("must be one of: {}".format(accepted_values))

        self._direction = direction

    # for value we need to define the property without decorators because of
    # this: https://stackoverflow.com/questions/13595607/using-super-in-a-propertys-setter-method-when-using-the-property-decorator-r
    # and the need to override these in the DimensionI class
    def _get_value(self):
        """
        access the value
        """
        return self._value

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
        else:
            raise TypeError("value must be of type array (or similar)")

    value = property(_get_value, _set_value)

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
            # TODO: switch to default
            label = ''

        if not isinstance(label, str):
            try:
                label = str(label)
            except:
                raise TypeError("label must be of type str")

        self._label = label


class DimensionI(Dimension):
    def __init__(self, *args):
        super(DimensionI, self).__init__('i', *args)

    @property
    def value(self):
        """
        access the value
        """
        if isinstance(self._value, str):
            dimension = self._value
            return getattr(self.call, dimension).value

        super(DimensionI, self)._get_value()

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
        super(DimensionI, self)._set_value(value)

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

class DimensionX(Dimension):
    def __init__(self, *args):
        super(DimensionX, self).__init__('x', *args)

class DimensionY(Dimension):
    def __init__(self, *args):
        super(DimensionY, self).__init__('y', *args)

class DimensionZ(Dimension):
    def __init__(self, *args):
        super(DimensionZ, self).__init__('z', *args)

class DimensionS(Dimension):
    def __init__(self, *args):
        super(DimensionS, self).__init__('s', *args)

class DimensionColor(Dimension):
    def __init__(self, *args):
        super(DimensionColor, self).__init__('color', *args)
