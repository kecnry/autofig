import autofig
from nose.tools import assert_raises

def test_unit_inconsistencies():
    autofig.reset()

    # Bottom-Up
    call1 = autofig.Plot(x=[1,2,3], y=[1,2,3], xunit='solRad')
    call2 = autofig.Plot(x=[1,2,3], y=[1,2,3])

    # None should cause issues, regardless of order
    assert_raises(ValueError, autofig.Axes, call1, call2)
    assert_raises(ValueError, autofig.Axes, call2, call1)

    # different provided values should cause inconsistency
    call1 = autofig.Plot(x=[1,2,3], y=[1,2,3], xunit='solRad')
    call2 = autofig.Plot(x=[1,2,3], y=[1,2,3], xunit='kg')

    assert_raises(ValueError, autofig.Axes, call1, call2)

    fig = autofig.Figure(call1, call2)
    assert(len(fig.axes)==2)

    # Top-down
    autofig.plot(x=[1,2,3], y=[1,2,3], xunit='solRad', yunit='AU')
    autofig.plot(x=[1,2,3], y=[1,2,3], xunit='km', yunit='kg')
    assert(len(autofig.gcf().axes)==2)

def test_label_inconsistencies():
    autofig.reset()

    # Bottom-Up
    call1 = autofig.Plot(x=[1,2,3], y=[1,2,3], xlabel='blah')
    call2 = autofig.Plot(x=[1,2,3], y=[1,2,3])

    # None shouldn't cause issues
    ax = autofig.Axes(call1, call2)
    assert(len(ax.calls)==2)
    fig = autofig.Figure(call1, call2)
    assert(len(fig.axes)==1)
    assert(len(fig.calls)==2)

    # None shouldn't cause issues if first either
    ax = autofig.Axes(call2, call1)
    assert(len(ax.calls)==2)
    fig = autofig.Figure(call2, call1)
    assert(len(fig.axes)==1)
    assert(len(fig.calls)==2)

    # different provided values should cause inconsistency
    call1 = autofig.Plot(x=[1,2,3], y=[1,2,3], xlabel='blah')
    call2 = autofig.Plot(x=[1,2,3], y=[1,2,3], xlabel='OTHER')

    assert_raises(ValueError, autofig.Axes, call1, call2)

    fig = autofig.Figure(call1, call2)
    assert(len(fig.axes)==2)

    # Top-down
    autofig.reset()
    autofig.plot(x=[1,2,3], y=[1,2,3], ylabel='blah')
    autofig.plot(x=[1,2,3], y=[1,2,3], ylabel='OTHER')
    assert(len(autofig.gcf().axes)==2)
    assert(len(autofig.gcf().calls)==2)

def test_title_inconsistencies():
    autofig.reset()

    call1 = autofig.Plot(x=[1,2,3], y=[1,2,3], title='title1')
    call2 = autofig.Plot(x=[1,2,3], y=[1,2,3], title='title2')
    call3 = autofig.Plot(x=[1,2,3], y=[1,2,3], title=None)

    # None shouldn't cause issues
    ax = autofig.Axes(call1, call3)
    assert(len(ax.calls)==2)
    fig = autofig.Figure(call1, call3)
    assert(len(fig.axes)==1)
    assert(len(fig.calls)==2)

    # None should cause issues if first either
    ax = autofig.Axes(call3, call2)
    assert(len(ax.calls)==2)
    fig = autofig.Figure(call3, call2)
    assert(len(fig.axes)==1)
    assert(len(fig.calls)==2)

    # different provided values should cause inconsistency
    assert_raises(ValueError, autofig.Axes, call1, call2)

    fig = autofig.Figure(call1, call2)
    assert(len(fig.axes)==2)

    # Top-down
    autofig.reset()
    autofig.plot(x=[1,2,3], y=[1,2,3], title='title1')
    autofig.plot(x=[1,2,3], y=[1,2,3], title='title2')
    assert(len(autofig.gcf().axes)==2)
    assert(len(autofig.gcf().calls)==2)

def test_axorder_inconsistencies():
    # Top-down
    autofig.reset()
    autofig.plot(x=[1,2,3], y=[1,2,3])
    autofig.plot(x=[1,2,3], y=[1,2,3], axorder=1)
    assert(len(autofig.gcf().axes)==1)
    assert(len(autofig.gcf().calls)==2)

    autofig.reset()
    autofig.plot(x=[1,2,3], y=[1,2,3], axorder=2)
    autofig.plot(x=[1,2,3], y=[1,2,3], axorder=1)
    assert(len(autofig.gcf().axes)==2)
    assert(len(autofig.gcf().calls)==2)

    autofig.reset()
    autofig.plot(x=[1,2,3], y=[1,2,3], xunit='solRad', axorder=1)
    autofig.plot(x=[1,2,3], y=[1,2,3], xunit='kg', axorder=1)
    assert(len(autofig.gcf().axes)==1)
    assert(len(autofig.gcf().calls)==2)

if __name__ == '__main__':
    test_unit_inconsistencies()
    test_label_inconsistencies()
    test_title_inconsistencies()
    test_axorder_inconsistencies()
