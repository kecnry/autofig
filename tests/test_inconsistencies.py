import autofig
from nose.tools import assert_raises

def test_unit_inconsistencies():
    # Bottom-Up
    call1 = autofig.Plot(x=[1,2,3], y=[1,2,3], xunit='solRad')
    call2 = autofig.Plot(x=[1,2,3], y=[1,2,3], yunit='kg')

    assert_raises(ValueError, autofig.Axes, call1, call2)

    fig = autofig.Figure(call1, call2)
    assert(len(fig.axes)==2)


if __name__ == '__main__':
    test_unit_inconsistencies()
