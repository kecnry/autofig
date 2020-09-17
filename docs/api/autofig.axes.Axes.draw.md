### [autofig](autofig.md).[axes](autofig.axes.md).[Axes](autofig.axes.Axes.md).draw (function)


```py

def draw(self, ax=None, i=None, calls=None, draw_sidebars=True, draw_title=True, show=False, save=False, in_animation=False)

```



Draw the contents of the [autofig.axes.Axes](autofig.axes.Axes.md) to a matplotlib axes
object.

See also:

* [autofig.draw](autofig.draw.md)
* [autofig.figure.Figure.draw](autofig.figure.Figure.draw.md)
* [autofig.call.Plot.draw](autofig.call.Plot.draw.md)
* [autofig.call.Mesh.draw](autofig.call.Mesh.draw.md)


Arguments
------------
* `ax` (matplotlib axes or None, optional, default=None): matplotlib
    axes instances to use during drawing.
* `i` (float or None, optional, default=None): passed on to
    [autofig.call.Call.draw](autofig.call.Call.draw.md) for all [autofig.call.Call](autofig.call.Call.md)s in
    [autofig.axes.Axes.calls](autofig.axes.Axes.calls.md).
* `calls` (list of [autofig.call.Call](autofig.call.Call.md) objects or None, optional, default=None):
    [autofig.call.Call](autofig.call.Call.md)s to draw.  If not provided or None, will draw
    [autofig.axes.Axes.calls_sorted](autofig.axes.Axes.calls_sorted.md).
* `draw_sidebars` (bool, optional, default=True): whether to draw
    any applicable sidebars.
* `draw_title` (bool, optional, default=True): whether to draw the title
    on the matplotlib axes.
* `show` (bool, optional, default=False): whether to immediately
    draw and show the resulting matplotlib figure.
* `save` (False or string, optional, default=False): the filename
    to save the resulting matplotlib figure, or False to not save.
* `in_animation` (bool, optional, default=False): whether the current
    call to `draw` is a single frame in an animation.  Usually this
    should not be changed by the user.  See [autofig.figure.Figure.animate](autofig.figure.Figure.animate.md)
    for creating animations.

Returns
----------
* [matplotlib Axes](https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes): the matplotlib axes object.

