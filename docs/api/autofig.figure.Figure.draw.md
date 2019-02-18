### [autofig](autofig.md).[figure](autofig.figure.md).[Figure](autofig.figure.Figure.md).draw (method)


```py

def draw(self, fig=None, i=None, calls=None, tight_layout=True, draw_sidebars=True, draw_title=True, subplot_grid=None, show=False, save=False, in_animation=False)

```



Draw the contents of the [autofig.figure.Figure](autofig.figure.Figure.md) to a matplotlib figure
object.

See also:

* [autofig.figure.Figure.animate](autofig.figure.Figure.animate.md)
* [autofig.draw](autofig.draw.md)
* [autofig.axes.Axes.draw](autofig.axes.Axes.draw.md)
* [autofig.call.Plot.draw](autofig.call.Plot.draw.md)
* [autofig.call.Mesh.draw](autofig.call.Mesh.draw.md)

Arguments
------------
* `fig` (matplotlib figure or None, optional, default=None): matplotlib
    figure instances to use during drawing.
* `i` (float or None, optional, default=None): passed on to
    [autofig.axes.Axes.draw](autofig.axes.Axes.draw.md) for all [autofig.axes.Axes](autofig.axes.Axes.md) in
    [autofig.figure.Figure.axes](autofig.figure.Figure.axes.md).
* `calls` (list of [autofig.call.Call](autofig.call.Call.md) objects or None, optional, default=None):
    passed on to [autofig.axes.Axes.draw](autofig.axes.Axes.draw.md) for all [autofig.axes.Axes](autofig.axes.Axes.md) in
    [autofig.figure.Figure.axes](autofig.figure.Figure.axes.md).
* `tight_layout` (bool, optional, default=True): whether to call
    `fig.tight_layout` after positioning all subplots, but before
    drawing any applicable sidebars.
* `draw_sidebars` (bool, optional, default=True): whether to draw
    any applicable sidebars.
* `draw_title` (bool, optional, default=True): passed on to
    [autofig.axes.Axes.draw](autofig.axes.Axes.draw.md) for all [autofig.axes.Axes](autofig.axes.Axes.md) in
    [autofig.figure.Figure.axes](autofig.figure.Figure.axes.md).  Whether to draw the title on the
    matplotlib axes.
* `subplot_grid` (None or tuple, optional, default=None): Override the
    subplot locations.  Passed on to [autofig.axes.Axes.append_subplot](autofig.axes.Axes.append_subplot.md)
    for each [autofig.axes.Axes](autofig.axes.Axes.md) in [autofig.figure.Figure.axes](autofig.figure.Figure.axes.md).
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
* ([matplotlib Figure](https://matplotlib.org/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure)): the matplotlib figure object.

