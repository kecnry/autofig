from .call import Plot, Mesh
from .axes import Axes
from .figure import Figure

global _figure
_figure = None

global _inline
_inline = False

def reset():
    global _figure
    _figure = None

def gcf():
    global _figure
    global _inline

    if _figure is None:
        _figure = Figure(inline=_inline)

    return _figure

def plot(*args, **kwargs):
    return gcf().plot(*args, **kwargs)

def mesh(*args, **kwargs):
    return gcf().mesh(*args, **kwargs)

def draw(*args, **kwargs):
    return gcf().draw(*args, **kwargs)

def animate(*args, **kwargs):
    return gcf().animate(*args, **kwargs)

def inline(inline=True):
    global _inline
    if not isinstance(inline, bool):
        raise TypeError("inline must be of type bool")
    _inline = inline
