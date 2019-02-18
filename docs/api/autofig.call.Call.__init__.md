### [autofig](autofig.md).[call](autofig.call.md).[Call](autofig.call.Call.md).__init__ (method)


```py

def __init__(self, x=None, y=None, z=None, i=None, xerror=None, xunit=None, xlabel=None, yerror=None, yunit=None, ylabel=None, zerror=None, zunit=None, zlabel=None, iunit=None, itol=0.0, axorder=None, axpos=None, title=None, label=None, consider_for_limits=True, uncover=False, trail=False, **kwargs)

```



Create a [autofig.call.Call](autofig.call.Call.md) object which defines a single call to
matplotlib.

Arguments
-------------
* `x` (list/array, optional, default=None): array of values for the x-axes.
    Access via [autofig.call.Call.x](autofig.call.Call.x.md).
* `y` (list/array, optional, default=None): array of values for the y-axes.
    Access via [autofig.call.Call.y](autofig.call.Call.y.md).
* `z` (list/array, optional, default=None): array of values for the z-axes.
    Access via [autofig.call.Call.z](autofig.call.Call.z.md)
* `i` (list/array or string, optional, default=None): array of values for
    the independent-variable.  If a string, can be one of: 'x', 'y', 'z'
    to reference an existing array.  Access via [autofig.call.Call.i](autofig.call.Call.i.md).
* `xerror` (float or list/array, optional, default=None): errors for `x`.
    See [autofig.call.Call.x](autofig.call.Call.x.md) and [autofig.call.CallDimensionX.error](autofig.call.CallDimensionX.error.md).
* `xunit` (string or astropy unit, optional, default=None): units for `x`.
    See [autofig.call.Call.x](autofig.call.Call.x.md) and [autofig.call.CallDimensionX.unit](autofig.call.CallDimensionX.unit.md).
* `xlabel` (strong, optional, default=None): label for `x`.
    See [autofig.call.Call.x](autofig.call.Call.x.md) and [autofig.call.CallDimensionX.label](autofig.call.CallDimensionX.label.md).
* `yerror` (float or list/array, optional, default=None): errors for `y`.
    See [autofig.call.Call.y](autofig.call.Call.y.md) and [autofig.call.CallDimensionY.error](autofig.call.CallDimensionY.error.md).
* `yunit` (string or astropy unit, optional, default=None): units for `y`.
    See [autofig.call.Call.y](autofig.call.Call.y.md) and [autofig.call.CallDimensionY.unit](autofig.call.CallDimensionY.unit.md).
* `ylabel` (strong, optional, default=None): label for `y`.
    See [autofig.call.Call.y](autofig.call.Call.y.md) and [autofig.call.CallDimensionY.label](autofig.call.CallDimensionY.label.md).
* `zerror` (float or list/array, optional, default=None): errors for `z`.
    See [autofig.call.Call.z](autofig.call.Call.z.md) and [autofig.call.CallDimensionZ.error](autofig.call.CallDimensionZ.error.md).
* `zunit` (string or astropy unit, optional, default=None): units for `z`.
    See [autofig.call.Call.z](autofig.call.Call.z.md) and [autofig.call.CallDimensionZ.unit](autofig.call.CallDimensionZ.unit.md).
* `zlabel` (strong, optional, default=None): label for `x`.
    See [autofig.call.Call.z](autofig.call.Call.z.md) and [autofig.call.CallDimensionZ.label](autofig.call.CallDimensionZ.label.md).
* `iunit` (string or astropy unit, optional, default=None): units for `i`.
    See [autofig.call.Call.i](autofig.call.Call.i.md) and [autofig.call.CallDimensionI.unit](autofig.call.CallDimensionI.unit.md).
* `itol` (float, optional, default=None): see [autofig.call.DimensionI.tol](autofig.call.DimensionI.tol.md).
* `axorder` (int, optional, default=None): see [autofig.call.Call.axorder](autofig.call.Call.axorder.md).
* `axpos` (tuple, optional, default=None): see [autofig.call.Call.axpos](autofig.call.Call.axpos.md).
* `title` (string, optional, default=None): see [autofig.call.Call.title](autofig.call.Call.title.md).
* `label` (string, optional, default=None): see [autofig.call.Call.label](autofig.call.Call.label.md).
* `consider_for_limits` (bool, optional, default=True): see
    [autofig.call.Call.consider_for_limits](autofig.call.Call.consider_for_limits.md).
* `uncover` (bool, optional, default=False): see [autofig.call.Call.uncover](autofig.call.Call.uncover.md).
* `trail` (bool or Float, optional, default=False): see
    [autofig.call.Call.trail](autofig.call.Call.trail.md).
* `**kwargs`: additional keyword arguments are stored and passed on when
    attaching to a parent axes.  See [autofig.axes.Axes.add_call](autofig.axes.Axes.add_call.md).

Returns
---------
* the instantiated [autofig.call.Call](autofig.call.Call.md) object.

