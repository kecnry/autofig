import autofig
from nose.tools import assert_raises

import astropy.units as u
import numpy as np

def test_set_get():
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

def test_convert():

    autofig.reset()

    autofig.plot(x=[0,10], y=[0,10], yunit=u.km)
    autofig.plot(x=[0,10], y=[0,10], yunit=u.solRad)

    # axes units will be the first (km)
    assert(autofig.gcf().axes[0].y.unit==u.km)

    # first call should be stored in km and retrieved in km
    assert(np.all(autofig.gcf().calls[0].y.get_value(unit=u.km)==np.array([0,10])))

    # second call should be stored in solRad but retrieved in km
    assert(np.all(autofig.gcf().calls[1].y.get_value(unit=u.km)==np.array([0,10])*u.solRad.to(u.km)))

    # axes limits should compare in the axes units (km)
    autofig.gcf().axes[0].y.pad = 0
    assert(np.all(autofig.gcf().axes[0].y.get_lim()==np.array([0,10*u.solRad.to(u.km)])))

if __name__ == '__main__':
    test_set_get()
    test_convert()
