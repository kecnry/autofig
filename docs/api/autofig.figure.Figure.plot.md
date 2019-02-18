### [autofig](autofig.md).[figure](autofig.figure.md).[Figure](autofig.figure.Figure.md).plot (method)


```py

def plot(self, *args, **kwargs)

```



Add a new [autofig.call.Plot](autofig.call.Plot.md) to the [autofig.figure.Figure](autofig.figure.Figure.md).

See also:

* [autofig.call.Plot.__init__](autofig.call.Plot.__init__.md)

Arguments
----------
* `*args`: all positional arguments are passed on to
    [autofig.call.Plot.__init__](autofig.call.Plot.__init__.md) to initialize the new
    [autofig.call.Plot](autofig.call.Plot.md).
* `tight_layout` (bool, optional, default=True): passed to
    [autofig.figure.Figure.draw](autofig.figure.Figure.draw.md) if `show` or `save`.  Whether to draw
    with the `tight_layout` option.
* `draw_title` (bool, optional, default=True): passed to
    [autofig.figure.Figure.draw](autofig.figure.Figure.draw.md) if `show` or `save`.  Whether to draw
    the title on the matplotlib axes.
* `subplot_grid` (None or tuple, optional, default=None): passed to
    [autofig.figure.Figure.draw](autofig.figure.Figure.draw.md) if `show` or `save`.  Override the
    subplot locations.
* `show` (bool, optional, default=False): whether to immediately
    draw and show the resulting matplotlib figure.  If True,
    [autofig.figure.Figure.draw](autofig.figure.Figure.draw.md) will be called.
* `save` (False or string, optional, default=False): the filename
    to save the resulting matplotlib figure, or False to not save.
    If not False, [autofig.figure.Figure.draw](autofig.figure.Figure.draw.md) will be called.
* `**kwargs`: additional keyword arguments are passed on to
    [autofig.call.Plot.__init__](autofig.call.Plot.__init__.md) to initialize the new
    [autofig.call.Plot](autofig.call.Plot.md).

