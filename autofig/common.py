import numpy as np
import astropy.units as u

try:
  basestring = basestring
except NameError:
  basestring = str

class Alias(object):
    def __init__(self, dict):
        self._dict = dict

    def map(self, key):
        return self._dict.get(key, key)


# https://matplotlib.org/examples/color/named_colors.html
# technically some of these (y, c, and m) don't exactly match, but as they "mean"
# the same thing, we'll handle the alias anyways
# Convention: always map to the spelled name and gray over grey
coloralias = Alias({'k': 'black', 'dimgrey': 'dimgray', 'grey': 'gray',
              'darkgrey': 'darkgray', 'lightgrey': 'lightgray',
               'w': 'white', 'r': 'red', 'y': 'yellow', 'g': 'green',
               'c': 'cyan', 'b': 'blue', 'm': 'magenta'})

# Convention: always map to the spelled name
linestylealias = Alias({'_': 'solid', '--': 'dashed', ':': 'dotted',
                      '-.': 'dashdot'})


def _convert_unit(unit):
    if unit is None:
        unit = u.dimensionless_unscaled

    if isinstance(unit, basestring):
        unit = u.Unit(unit)

    if not (isinstance(unit, u.Unit) or isinstance(unit, u.CompositeUnit) or isinstance(unit, u.IrreducibleUnit)):
        raise TypeError("unit must be of type Unit, got: {}".format(unit))

    return unit

dimensions = ['i', 'x', 'y', 'z', 's', 'c']
