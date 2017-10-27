import numpy as np
import astropy.units as u
from . import common

class Call(object):
    def __init__(self, i=None, iunit=None,
                       x=None, xerrors=None, xunit=None, xlabel=None,
                       y=None, yerrors=None, yunit=None, ylabel=None,
                       z=None, zerrors=None, zunit=None, zlabel=None,
                       c=None, cunit=None, clabel=None,
                       fc=None, fcunit=None, fclabel=None,
                       ec=None, ecunit=None, eclabel=None):
        """
        """
        self._x = CallDimensionX(self, x, xerrors, xunit, xlabel)
        self._y = CallDimensionY(self, y, yerrors, yunit, ylabel)
        self._z = CallDimensionZ(self, z, zerrors, zunit, zlabel)
        self._c = CallDimensionColor(self, c, None, cunit, clabel)
        self._fc = CallDimensionColor(self, fc, None, fcunit, fclabel)
        self._ec = CallDimensionColor(self, ec, None, ecunit, eclabel)

        # defined last so all other dimensions are in place in case indep
        # is a reference and needs to access units, etc
        self._i = CallDimensionI(self, i, iunit)

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
    def __init__(self, direction, call, value, errors=None, unit=None, label=None):
        self._direction = None
        self._value = None
        self._errors = None
        self._unit = None
        self._label = None
        # self._lim = None

        self._call = call
        self.direction = direction
        # unit must be set before value as setting value pulls the appropriate
        # unit for CallDimensionI
        self.unit = unit
        self.value = value
        self.errors = errors
        self.label = label
        # self.lim = lim

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

        accepted_values = ['i', 'x', 'y', 'z', 'color', 'markersize']
        if direction not in accepted_values:
            raise ValueError("must be one of: {}".format(accepted_values))

        self._direction = direction

    # for value we need to define the property without decorators because of
    # this: https://stackoverflow.com/questions/13595607/using-super-in-a-propertys-setter-method-when-using-the-property-decorator-r
    # and the need to override these in the CallDimensionI class
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
        # TODO: check length with value?
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
        if self.direction in ['i'] and label is not None:
            raise ValueError("label not accepted for indep dimension")


        if label is None:
            # TODO: switch to default
            label = 'DEFAULT LABEL'

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

        super(CallDimensionI, self)._get_value()

    @value.setter
    def value(self, value):
        """
        set the value
        """
        # for the indep direction we also allow a string which points to one
        # of the other available dimensions
        # TODO: support c, fc, ec?
        if isinstance(value, unicode):
            value = str(value)
        if isinstance(value, str) and value in ['x', 'y', 'z']:
            self._value  = value
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

class CallDimensionColor(CallDimension):
    def __init__(self, *args):
        super(CallDimensionColor, self).__init__('color', *args)
