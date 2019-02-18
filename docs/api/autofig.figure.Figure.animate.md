### [autofig](autofig.md).[figure](autofig.figure.md).[Figure](autofig.figure.Figure.md).animate (method)


```py

def animate(self, fig=None, i=None, tight_layout=False, draw_sidebars=True, draw_title=True, subplot_grid=None, show=False, save=False, save_kwargs={})

```



Draw the contents of the [autofig.figure.Figure](autofig.figure.Figure.md) to a matplotlib animation.

See also:

* [autofig.figure.Figure.plot](autofig.figure.Figure.plot.md)

Arguments
------------
* `fig` (matplotlib figure or None, optional, default=None): matplotlib
    figure instances to use during drawing.
* `i` (list/array, **required**): iterable values for `i`.  Each item
    in the list/array will become a single frame in the resulting
    animation.
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
    draw and show the resulting matplotlib animation.
* `save` (False or string, optional, default=False): the filename
    to save the resulting matplotlib animation, or False to not save.
* `save_kwargs` (dict, optional, default={}): dictionary of keyword
    arguments to be passed on to [anim.save](https://matplotlib.org/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation.save)

Returns
----------
* ([matplotlib FuncAnimation](https://matplotlib.org/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib-animation-funcanimation)): the matplotlib animation object.

