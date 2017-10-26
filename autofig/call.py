import numpy as np
import astropy.units as u
from . import common

class Call(object):
    def __init__(self, x=None, xerrors=None, xunit=None, xlabel=None,
                       y=None, yerrors=None, yunit=None, ylabel=None,
                       z=None, zerrors=None, zunit=None, zlabel=None,
                       c=None, cunit=None, clabel=None,
                       fc=None, fcunit=None, fclabel=None,
                       ec=None, ecunit=None, eclabel=None):
        """
        """
        self._x = CallDimensionX(x, xerrors, xunit, xlabel)
        self._y = CallDimensionY(y, yerrors, yunit, ylabel)
        self._z = CallDimensionZ(z, zerrors, zunit, zlabel)
        self._c = CallDimensionColor(c, None, cunit, clabel)
        self._fc = CallDimensionColor(fc, None, fcunit, fclabel)
        self._ec = CallDimensionColor(ec, None, ecunit, eclabel)

        # TODO: add style

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
    def c(self):
        return self._c

    @property
    def color(self):
        return self.c

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



class CallDimension(object):
    def __init__(self, direction, value, errors, unit, label):
        self._direction = None
        self._value = None
        self._errors = None
        self._unit = None
        self._label = None
        # self._lim = None

        self.direction = direction
        self.value = value
        self.errors = errors
        self.unit = unit
        self.label = label
        # self.lim = lim

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

        accepted_values = ['x', 'y', 'z', 'color', 'markersize']
        if direction not in accepted_values:
            raise ValueError("must be one of: {}".format(accepted_values))

        self._direction = direction

    @property
    def value(self):
        """
        access the value
        """
        return self._value

    @property
    def value_as_array(self):
        """
        """
        raise NotImplementedError

    @value.setter
    def value(self, value):
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

    @property
    def errors(self):
        """
        access the errors
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        set the errors
        """
        # TODO: check length with value_as_array?
        # TODO: type checks (similar to value)
        if self.direction not in ['x', 'y', 'z'] and errors is not None:
            raise ValueError("errors only accepted for x, y, z dimensions")

        self._errors = errors

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
        if label is None:
            # TODO: switch to default
            label = 'DEFAULT LABEL'

        if not isinstance(label, str):
            try:
                label = str(label)
            except:
                raise TypeError("label must be of type str")

        self._label = label

    # @property
    # def lim(self):
    #     """
    #     access the lim (limits)
    #     """
    #     return self._lim
    #
    # @lim.setter
    # def lim(self, lim):
    #     """
    #     set the lim (limits)
    #     """
    #     if lim is None:
    #         self._lim = lim
    #         return
    #
    #     if not isinstance(lim, tuple):
    #         try:
    #             lim = tuple(lim)
    #         except:
    #             raise TypeError('lim must be of type tuple')
    #
    #     if not len(lim)==2:
    #         raise ValueError('lim must have length 2')
    #
    #     self._lim = lim




class CallDimensionX(CallDimension):
    def __init__(self, *args):
        super(CallDimensionX, self).__init__('x', *args)

class CallDimensionY(CallDimension):
    def __init__(self, *args):
        super(CallDimensionY, self).__init__('y', *args)

class CallDimensionZ(CallDimension):
    def __init__(self, *args):
        super(CallDimensionZ, self).__init__('z', *args)

class CallDimensionColor(CallDimension):
    def __init__(self, *args):
        super(CallDimensionColor, self).__init__('color', *args)
