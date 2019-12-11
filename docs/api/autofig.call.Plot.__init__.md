### [autofig](autofig.md).[call](autofig.call.md).[Plot](autofig.call.Plot.md).__init__ (method)


```py

def __init__(self, x=None, y=None, z=None, c=None, s=None, i=None, xerror=None, xunit=None, xlabel=None, yerror=None, yunit=None, ylabel=None, zerror=None, zunit=None, zlabel=None, cunit=None, clabel=None, cmap=None, sunit=None, slabel=None, smap=None, smode=None, iunit=None, itol=0.0, axorder=None, axpos=None, title=None, label=None, marker=None, linestyle=None, linebreak=None, highlight=True, uncover=False, trail=False, consider_for_limits=True, **kwargs)

```



Create a [autofig.call.Plot](autofig.call.Plot.md) object which defines a single call to
matplotlib.

See also:

* [autofig.call.Mesh](autofig.call.Mesh.md)

Note that the following keyword arguments are not allowed and will raise
an error suggesting the appropriate autofig argument:

* `markersize` or `ms`: use `size` or `s`
* `linewidth` or `lw`: use `size` or `s`


Arguments
-------------
* `x` (list/array, optional, default=None): array of values for the x-axes.
    Access via [autofig.call.Plot.x](autofig.call.Plot.x.md).
* `y` (list/array, optional, default=None): array of values for the y-axes.
    Access via [autofig.call.Plot.y](autofig.call.Plot.y.md).
* `z` (list/array, optional, default=None): array of values for the z-axes.
    Access via [autofig.call.Plot.z](autofig.call.Plot.z.md)
* `c` or `color` (list/array, optional, default=None): array of values for the
    color-direction.  Access via [autofig.call.Plot.c](autofig.call.Plot.c.md).  Note: `color`
    takes precedence over `c` if both are provided.
* `s` or `size` (list/array, optional, default=None): array of values for the
    size-direction.  Access via [autofig.call.Plot.s](autofig.call.Plot.s.md).  Note: `size` takes
    precedence over `s` if both are provided.
* `i` (list/array or string, optional, default=None): array of values for
    the independent-variable.  If a string, can be one of: 'x', 'y', 'z',
    'c', 's' to reference an existing array.  Access via
    [autofig.call.Plot.i](autofig.call.Plot.i.md).
* `xerror` (float or list/array, optional, default=None): errors for `x`.
    See [autofig.call.Plot.x](autofig.call.Plot.x.md) and [autofig.call.CallDimensionX.error](autofig.call.CallDimensionX.error.md).
* `xunit` (string or astropy unit, optional, default=None): units for `x`.
    See [autofig.call.Plot.x](autofig.call.Plot.x.md) and [autofig.call.CallDimensionX.unit](autofig.call.CallDimensionX.unit.md).
* `xlabel` (strong, optional, default=None): label for `x`.
    See [autofig.call.Plot.x](autofig.call.Plot.x.md) and [autofig.call.CallDimensionX.label](autofig.call.CallDimensionX.label.md).
* `yerror` (float or list/array, optional, default=None): errors for `y`.
    See [autofig.call.Plot.y](autofig.call.Plot.y.md) and [autofig.call.CallDimensionY.error](autofig.call.CallDimensionY.error.md).
* `yunit` (string or astropy unit, optional, default=None): units for `y`.
    See [autofig.call.Plot.y](autofig.call.Plot.y.md) and [autofig.call.CallDimensionY.unit](autofig.call.CallDimensionY.unit.md).
* `ylabel` (strong, optional, default=None): label for `y`.
    See [autofig.call.Plot.y](autofig.call.Plot.y.md) and [autofig.call.CallDimensionY.label](autofig.call.CallDimensionY.label.md).
* `zerror` (float or list/array, optional, default=None): errors for `z`.
    See [autofig.call.Plot.z](autofig.call.Plot.z.md) and [autofig.call.CallDimensionZ.error](autofig.call.CallDimensionZ.error.md).
* `zunit` (string or astropy unit, optional, default=None): units for `z`.
    See [autofig.call.Plot.z](autofig.call.Plot.z.md) and [autofig.call.CallDimensionZ.unit](autofig.call.CallDimensionZ.unit.md).
* `zlabel` (strong, optional, default=None): label for `x`.
    See [autofig.call.Plot.z](autofig.call.Plot.z.md) and [autofig.call.CallDimensionZ.label](autofig.call.CallDimensionZ.label.md).
* `cerror` (float or list/array, optional, default=None): errors for `c`.
    See [autofig.call.Plot.c](autofig.call.Plot.c.md) and [autofig.call.CallDimensionC.error](autofig.call.CallDimensionC.error.md).
* `cunit` (string or astropy unit, optional, default=None): units for `c`.
    See [autofig.call.Plot.c](autofig.call.Plot.c.md) and [autofig.call.CallDimensionC.unit](autofig.call.CallDimensionC.unit.md).
* `clabel` (strong, optional, default=None): label for `c`.
    See [autofig.call.Plot.c](autofig.call.Plot.c.md) and [autofig.call.CallDimensionC.label](autofig.call.CallDimensionC.label.md).
* `serror` (float or list/array, optional, default=None): errors for `s`.
    See [autofig.call.Plot.s](autofig.call.Plot.s.md) and [autofig.call.CallDimensionS.error](autofig.call.CallDimensionS.error.md).
* `sunit` (string or astropy unit, optional, default=None): units for `s`.
    See [autofig.call.Plot.s](autofig.call.Plot.s.md) and [autofig.call.CallDimensionS.unit](autofig.call.CallDimensionS.unit.md).
* `slabel` (strong, optional, default=None): label for `s`.
    See [autofig.call.Plot.s](autofig.call.Plot.s.md) and [autofig.call.CallDimensionS.label](autofig.call.CallDimensionS.label.md).
* `iunit` (string or astropy unit, optional, default=None): units for `i`.
    See [autofig.call.Plot.i](autofig.call.Plot.i.md) and [autofig.call.CallDimensionI.unit](autofig.call.CallDimensionI.unit.md).
* `itol` (float, optional, default=0.0): see [autofig.call.DimensionI.tol](autofig.call.DimensionI.tol.md).
* `axorder` (int, optional, default=None): see [autofig.call.Plot.axorder](autofig.call.Plot.axorder.md).
* `axpos` (tuple, optional, default=None): see [autofig.call.Plot.axpos](autofig.call.Plot.axpos.md).
* `title` (string, optional, default=None): see [autofig.call.Plot.title](autofig.call.Plot.title.md).
* `label` (string, optional, default=None): see [autofig.call.Plot.label](autofig.call.Plot.label.md).
* `marker` or `m` (string, optional, default=None): see [autofig.call.Plot.marker](autofig.call.Plot.marker.md).
    Note: `marker` takes precedence over `m` if both are provided.
* `linestyle` or `ls` (string, optional, default=None): see
    [autofig.call.Plot.linestyle](autofig.call.Plot.linestyle.md). Note: `linestyle` takes precedence
    over `ls` if both are provided.
* `linebreak` (string, optional, default=None): see [autofig.call.Plot.linebreak](autofig.call.Plot.linebreak.md).
* `highlight` (bool, optional, default=False): see [autofig.call.Plot.highlight](autofig.call.Plot.highlight.md).
* `highlight_marker` (string, optional, default=None)
* `highlight_linestyle` or `highlight_ls` (string, optional, default=None):
    Note: `highlight_linestyle` takes precedence over `highlight_ls` if
    both are provided.
* `highlight_size` or `highlight_s` (float, optional, default=None):
    Note: `highlight_size` takes precedence over `highlight_s` if both
    are provided.
* `highlight_color` or `highlight_c` (string, optional, default=None):
    Note: `highlight_color` takes precedence over `highlight_c` if both
    are provided.
* `consider_for_limits` (bool, optional, default=True): see
    [autofig.call.Call.consider_for_limits](autofig.call.Call.consider_for_limits.md).
* `uncover` (bool, optional, default=False): see [autofig.call.Call.uncover](autofig.call.Call.uncover.md).
* `trail` (bool or Float, optional, default=False): see
    [autofig.call.Call.trail](autofig.call.Call.trail.md).
* `**kwargs`: additional keyword arguments are stored and passed on when
    attaching to a parent axes.  See [autofig.axes.Axes.add_call](autofig.axes.Axes.add_call.md).

Returns
---------
* the instantiated [autofig.call.Plot](autofig.call.Plot.md) object.

