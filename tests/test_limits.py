import autofig
from nose.tools import assert_raises

def test_limits():
    autofig.reset()

    autofig.plot(x=[0,10], y=[0,10])
    autofig.plot(x=[-5,5], y=[-5,5])

    autofig.gcf().axes[0].xyz.pad = 0.0

    assert(autofig.gcf().axes[0].x.get_lim() == (-5,10))
    assert(autofig.gcf().axes[0].y.get_lim() == (-5,10))

def test_padding():
    autofig.reset()

    autofig.plot(x=[0,10], y=[0,10])
    autofig.plot(x=[-5,5], y=[-5,5])

    autofig.gcf().axes[0].xyz.pad = 0.1

    assert(autofig.gcf().axes[0].x.get_lim() == (-6.5,11.5))
    assert(autofig.gcf().axes[0].y.get_lim() == (-6.5,11.5))

    autofig.gcf().axes[0].y.pad = 0.0

    assert(autofig.gcf().axes[0].x.get_lim() == (-6.5,11.5))
    assert(autofig.gcf().axes[0].y.get_lim() == (-5,10))


def test_consider_for_limits():
    autofig.reset()

    autofig.plot(x=[0,10], y=[0,10])
    autofig.plot(x=[-5,5], y=[-5,5])
    autofig.plot(x=[-30,30], y=[-30,30], consider_for_limits=False)

    autofig.gcf().axes[0].xyz.pad = 0

    assert(autofig.gcf().axes[0].x.get_lim() == (-5,10))
    assert(autofig.gcf().axes[0].y.get_lim() == (-5,10))

if __name__ == '__main__':
    test_limits()
    test_padding()
    test_consider_for_limits()
