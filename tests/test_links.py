import autofig
from nose.tools import assert_raises

from autofig.figure import Figure
from autofig.axes import Axes
from autofig.call import Call

def test_hierarchy_links():
    autofig.reset()

    autofig.plot(x=[1,2,3], y=[1,2,3], c=[1,2,3], s=[1,2,3])

    figure = autofig.gcf()

    assert(isinstance(figure, Figure))

    axes = figure.axes[0]

    assert(isinstance(axes, Axes))
    assert(axes.figure==figure)

    call = figure.calls[0]
    call = axes.calls[0]

    assert(isinstance(call, Call))
    assert(call.axes==axes)
    assert(call.figure==figure)

if __name__ == '__main__':
    test_hierarchy_links()
