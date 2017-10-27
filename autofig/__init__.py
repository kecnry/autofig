from .call import Plot, Mesh
from .axes import Axes
from .figure import Figure

global _figure
_figure = None

def gcf():
    global _figure
    if _figure is None:
        _figure = Figure()

    return _figure

def plot(*args, **kwargs):
    return gcf().plot(*args, **kwargs)

def mesh(*args, **kwargs):
    return gcf().mesh(*args, **kwargs)

def draw(*args, **kwargs):
    return gcf().draw(*args, **kwargs)
