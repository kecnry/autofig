import autofig
from nose.tools import assert_raises

import astropy.units as u
import numpy as np

def test_units():
    autofig.reset()

    autofig.plot(x=[0,10], y=[0,10], yunit=u.solRad)
    assert(autofig.gcf().axes[0].y.unit==u.solRad)
    assert(autofig.gcf().calls[0].y.unit==u.solRad)

    autofig.reset()

    autofig.plot(x=[0,10], y=[0,10]*u.solRad)
    assert(autofig.gcf().axes[0].y.unit==u.solRad)
    assert(autofig.gcf().calls[0].y.unit==u.solRad)
    assert(np.all(autofig.gcf().calls[0].y.value==np.array([0,10])))

    autofig.reset()

    autofig.plot(x=[0,10], y=[0,10]*u.solRad, yunit='km')
    assert(autofig.gcf().axes[0].y.unit==u.km)
    assert(autofig.gcf().calls[0].y.unit==u.km)
    assert(np.all(autofig.gcf().calls[0].y.value==np.array([0,10])*u.solRad.to(u.km)))


if __name__ == '__main__':
    test_units()
