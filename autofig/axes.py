import numpy as np
import astropy.units as u
from . import common
from . import call as _call

class Axes(object):
    def __init__(self, *calls, **kwargs):
        self._available_dimensions = ['x', 'y', 'z', 'c', 'fc', 'ec']

        self._calls = []

        self._x = AxDimensionX(self, **kwargs)
        self._y = AxDimensionY(self, **kwargs)
        self._z = AxDimensionZ(self, **kwargs)
        # TODO: think about multiple scalings for each of these... they may
        # need to move to the calls
        self._s = AxDimensionS(self)
        self._c = AxDimensionC(self)
        self._fc = AxDimensionFC(self)
        self._ec = AxDimensionEC(self)


        # TODO: allow passing/setting pad(s)
        self._default_pad = 0.0

        self.add_call(*calls)

    @property
    def calls(self):
        return self._calls

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

    @property
    def default_pad(self):
        return self._default_pad

    @default_pad.setter
    def default_pad(self, pad):
        if not isinstance(pad, float):
            try:
                pad = float(pad)
            except:
                raise TypeError("pad must be of type float")

        self._pad = pad

    def consistent_with_call(self, call):
        """
        check to see if a new call would be consistent to add to this Axes instance

        checks include:
        * compatible units in all directions
        """
        if len(self.calls) == 0:
            return True, ''

        msg = []
        # TODO: include c, fc, ec and make this into a loop
        if call.x.unit.physical_type != self.x.unit.physical_type:
            msg.append('inconsitent xunit, {} != {}'.format(call.x.unit, self.x.unit))
        if call.y.unit.physical_type != self.y.unit.physical_type:
            msg.append('inconsitent yunit, {} != {}'.format(call.y.unit, self.y.unit))
        if call.z.unit.physical_type != self.z.unit.physical_type:
            msg.append('inconsitent zunit, {} != {}'.format(call.z.unit, self.z.unit))

        if len(msg):
            return False, ', '.join(msg)
        else:
            return True, ''

    def add_call(self, *calls):
        if len(calls) > 1:
            for c in calls:
                self.add_call(c)
            return

        elif len(calls) == 1:
            call = calls[0]
            if not isinstance(call, _call.Call):
                raise TypeError("call must be of type Call")

            consistent, reason = self.consistent_with_call(call)
            if not consistent:
                raise ValueError("call is not consistent with Axes: {}".format(reason))

            self._calls.append(call)

            if len(self.calls) == 1:
                # then this was the first, so set default units
                self.x.unit = call.x.unit
                self.y.unit = call.y.unit
                self.z.unit = call.z.unit



class AxDimension(object):
    def __init__(self, direction, ax, unit=None, pad=None, lim=[None, None], label=None):
        self._direction = None
        self._unit = None
        self._pad = None
        self._lim = None
        self._label = None

        self._ax = ax
        self.direction = direction
        self.unit = unit
        self.pad = pad
        self.lim = lim
        self.label = label

    @property
    def ax(self):
        return self._ax

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

        accepted_values = ['x', 'y', 'z', 's', 'c', 'fc', 'ec']
        if direction not in accepted_values:
            raise ValueError("must be one of: {}".format(accepted_values))

        self._direction = direction

    @property
    def unit(self):
        return self._unit

    @property
    def unit_string(self):
        return self.unit.to_string()

    @property
    def unit_latex(self):
        return self.unit._repr_latex_()

    @unit.setter
    def unit(self, unit):
        unit = common._convert_unit(unit)
        self._unit = unit

    @property
    def default_pad(self):
        return self.ax.default_pad

    @property
    def pad(self):
        default = self.default_pad
        return self._pad if self._pad is not None else self.default_pad

    @pad.setter
    def pad(self, pad):
        # TODO type checking
        self._pad = pad

    def get_lim(self, pad=None):

        if pad is None:
            pad = self.pad

        lims = self._lim
        fixed_min = lims[0] is not None
        fixed_max = lims[1] is not None
        for call in self.ax.calls:
            array = getattr(call, self.direction).value
            if not fixed_min and (lims[0] is None or np.min(array) < lims[0]):
                lims[0] = np.min(array)
            if not fixed_max and (lims[1] is None or np.max(array) > lims[1]):
                lims[1] = np.max(array)

        if pad:
            rang = abs(lims[1] - lims[0])
            if not fixed_min:
                lims[0] -= rang*pad
            if not fixed_max:
                lims[1] += rang*pad

        return lims

    @property
    def lim(self):
        return self.get_lim(pad=self.pad)

    @lim.setter
    def lim(self, lim):
        """
        set lim (limits)
        """
        if lim is None:
            self._lim = lim
            return

        if not isinstance(lim, tuple):
            try:
                lim = tuple(lim)
            except:
                raise TypeError('lim must be of type tuple')

        if not len(lim)==2:
            raise ValueError('lim must have length 2')

        self._lim = lim

    @property
    def label(self):
        return '' if self._label is None else self._label

    @property
    def label_with_units(self):
        return r"{} ({})".format(self.label, self.unit_latex)

    @label.setter
    def label(self, label):
        self._label = label


def _process_dimension_kwargs(direction, kwargs):
    """
    process kwargs for AxDimension instances by stripping off the prefix
    for the appropriate direction
    """
    acceptable_keys = ['unit', 'pad', 'lim', 'label']
    processed_kwargs = {}
    for k,v in kwargs.items():
        if k.startswith(direction):
            processed_key = k.lstrip(direction)
        else:
            processed_key = k

        if processed_key in acceptable_keys:
            processed_kwargs[processed_key] = v

    return processed_kwargs


class AxDimensionX(AxDimension):
    def __init__(self, *args, **kwargs):
        processed_kwargs = _process_dimension_kwargs('x', kwargs)
        super(AxDimensionX, self).__init__('x', *args, **processed_kwargs)

class AxDimensionY(AxDimension):
    def __init__(self, *args, **kwargs):
        processed_kwargs = _process_dimension_kwargs('y', kwargs)
        super(AxDimensionY, self).__init__('y', *args, **processed_kwargs)

class AxDimensionZ(AxDimension):
    def __init__(self, *args, **kwargs):
        processed_kwargs = _process_dimension_kwargs('z', kwargs)
        super(AxDimensionZ, self).__init__('z', *args, **processed_kwargs)

class AxDimensionS(AxDimension):
    def __init__(self, *args, **kwargs):
        processed_kwargs = _process_dimension_kwargs('s', kwargs)
        super(AxDimensionS, self).__init__('s', *args, **processed_kwargs)

    @property
    def default_pad(self):
        return 0.0

class AxDimensionC(AxDimension):
    def __init__(self, *args, **kwargs):
        processed_kwargs = _process_dimension_kwargs('c', kwargs)
        super(AxDimensionC, self).__init__('c', *args, **processed_kwargs)

    @property
    def default_pad(self):
        return 0.0

class AxDimensionFC(AxDimension):
    def __init__(self, *args, **kwargs):
        processed_kwargs = _process_dimension_kwargs('fc', kwargs)
        super(AxDimensionFC, self).__init__('fc', *args, **processed_kwargs)

    @property
    def default_pad(self):
        return self.ax.c.pad

class AxDimensionEC(AxDimension):
    def __init__(self, *args, **kwargs):
        processed_kwargs = _process_dimension_kwargs('ec', kwargs)
        super(AxDimensionEC, self).__init__('ec', *args, **processed_kwargs)

    @property
    def default_pad(self):
        return self.ax.c.pad
