### [autofig](autofig.md).[axes](autofig.axes.md).[Axes](autofig.axes.Axes.md).append_subplot (method)


```py

def append_subplot(self, fig=None, subplot_grid=None)

```



Append this [autofig.axes.Axes](autofig.axes.Axes.md) as a subplot to a matplotlib figure.

Arguments
----------
* `fig` (matplotlib figure, optional, default=None): the matplotlib figure
    on which to append the subplot.  If not provided or None, will default
    to plt.gcf().
* `subplot_grid` (tuple of length 2 or None, optional, default=None):
    subplot grid in format (nrows [int], ncols [int]).  The appended
    subplot will then be placed in the location determined by
    [autofig.axes.Axes.axpos](autofig.axes.Axes.axpos.md) or the next open slot.

Returns
------------
* [matplotlib Axes](https://matplotlib.org/api/axes_api.html#matplotlib.axes.Axes)

Raises
-----------
* TypeError: if `subplot_grid` is not None or a tuple
* ValueError: if `subplot_grid` is a tuple, but not of 2 integers

