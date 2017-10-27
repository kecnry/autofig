import numpy as np
import astropy.units as u

def _convert_unit(unit):
    if unit is None:
        unit = u.dimensionless_unscaled

    if isinstance(unit, basestring):
        unit = u.Unit(unit)

    if not (isinstance(unit, u.Unit) or isinstance(unit, u.CompositeUnit) or isinstance(unit, u.IrreducibleUnit)):
        raise TypeError("unit must be of type Unit, got: {}".format(unit))

    return unit
