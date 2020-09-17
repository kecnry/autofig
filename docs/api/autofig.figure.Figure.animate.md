### [autofig](autofig.md).[figure](autofig.figure.md).[Figure](autofig.figure.Figure.md).animate (function)


```py

def animate(self, fig=None, i=None, tight_layout=False, draw_sidebars=True, draw_title=True, subplot_grid=None, interval=100, animate_callback=None, show=False, save=False, save_kwargs={}, save_afig=False)

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
* `interval` (int, optional, default=100): time in ms between each
    frame in the animation.
* `animate_callback` (callable, optional, default=None): Function which
    takes the matplotlib figure object and will be called at each frame
    within the animation.
* `show` (bool, optional, default=False): whether to immediately
    draw and show the resulting matplotlib animation.
* `save` (False or string, optional, default=False): the filename
    to save the resulting matplotlib animation, or False to not save.
* `save_kwargs` (dict, optional, default={}): dictionary of keyword
    arguments to be passed on to [anim.save](https://matplotlib.org/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation.save)
* `save_afig` (False or string, optional, default=False): the filename
    to save the autofig object, along with the options for this
    animate call.  See also [autofig.figure.Figure.save](autofig.figure.Figure.save.md).

Returns
----------
* ([matplotlib FuncAnimation](https://matplotlib.org/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib-animation-funcanimation)): the matplotlib animation object.

