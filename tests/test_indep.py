import autofig
import numpy as np
from nose.tools import assert_raises

def test_plotting():
    # x as independent-variable
    x = np.linspace(-10,10,101)
    autofig.plot(x=x, y=x**2, i='x', marker='None', ls='solid', highlight=True, uncover=False)
    autofig.plot(x=x, y=2*x, i='x', marker='None', ls='solid', highlight=True, uncover=True)

    autofig.draw(i=7.123, show=False)

    # 'external' independent-variable
    time = np.linspace(0,2*np.pi,101)
    x = np.cos(time)
    y = np.sin(time)

    autofig.reset()
    autofig.plot(x=x, y=y, i=time, marker='None', ls='solid', highlight=True, uncover=True)
    autofig.draw(i=3./2*np.pi, show=False)

def test_interp():

    p = autofig.Plot(x=[1,2,3], y=[2,4,6], i='x')
    assert(p.x.interpolate_at_i(1.5)==1.5)
    assert(p.y.interpolate_at_i(1.5)==3)

    # TODO: what about extrapolation, should that throw any sort of error?

    p = autofig.Plot(x=[1,2,3], y=[2,4,6], i=[10,20,30])
    assert(p.x.interpolate_at_i(15)==1.5)
    assert(p.y.interpolate_at_i(15)==3)
    assert(p.i.interpolate_at_i(15)==15)

if __name__ == '__main__':
    test_plotting()
    test_interp()
