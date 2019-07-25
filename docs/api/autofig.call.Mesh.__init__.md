### [autofig](autofig.md).[call](autofig.call.md).[Mesh](autofig.call.Mesh.md).__init__ (method)


```py

def __init__(self, x=None, y=None, z=None, fc=None, ec=None, i=None, xerror=None, xunit=None, xlabel=None, xnormals=None, yerror=None, yunit=None, ylabel=None, ynormals=None, zerror=None, zunit=None, zlabel=None, znormals=None, fcunit=None, fclabel=None, fcmap=None, ecunit=None, eclabel=None, ecmap=None, iunit=None, itol=0.0, axorder=None, axpos=None, title=None, label=None, linestyle=None, consider_for_limits=True, uncover=True, trail=0, exclude_back=False, **kwargs)

```



Create a [autofig.call.Mesh](autofig.call.Mesh.md) object which defines a single call to
matplotlib.

See also:

* [autofig.call.Plot](autofig.call.Plot.md)


Arguments
-------------
* `x` (list/array, optional, default=None): array of values for the x-axes.
    Access via [autofig.call.Mesh.x](autofig.call.Mesh.x.md).
* `y` (list/array, optional, default=None): array of values for the y-axes.
    Access via [autofig.call.Mesh.y](autofig.call.Mesh.y.md).
* `z` (list/array, optional, default=None): array of values for the z-axes.
    Access via [autofig.call.Mesh.z](autofig.call.Mesh.z.md)
* `fc` or `facecolor` (list/array, optional, default=None): array of values for the
    facecolor-direction.  Access via [autofig.call.Mesh.fc](autofig.call.Mesh.fc.md).  Note: `facecolor`
    takes precedence over `fc` if both are provided.
* `ec` or `edgecolor` (list/array, optional, default=None): array of values for the
    edgecolor-direction.  Access via [autofig.call.Mesh.ec](autofig.call.Mesh.ec.md).  Note: `edgecolor`
    takes precedence over `ec` if both are provided.
* `i` (list/array or string, optional, default=None): array of values for
    the independent-variable.  If a string, can be one of: 'x', 'y', 'z',
    'fc', 'ec' to reference an existing array.  Access via
    [autofig.call.Mesh.i](autofig.call.Mesh.i.md).
* `xerror` (float or list/array, optional, default=None): errors for `x`.
    See [autofig.call.Mesh.x](autofig.call.Mesh.x.md) and [autofig.call.CallDimensionX.error](autofig.call.CallDimensionX.error.md).
* `xunit` (string or astropy unit, optional, default=None): units for `x`.
    See [autofig.call.Mesh.x](autofig.call.Mesh.x.md) and [autofig.call.CallDimensionX.unit](autofig.call.CallDimensionX.unit.md).
* `xlabel` (strong, optional, default=None): label for `x`.
    See [autofig.call.Mesh.x](autofig.call.Mesh.x.md) and [autofig.call.CallDimensionX.label](autofig.call.CallDimensionX.label.md).
* `xnormals` (list/array, optional, default=None): normals for `x`.
    Currently ignored.
    See [autofig.call.Mesh.x](autofig.call.Mesh.x.md) and [autofig.call.CallDimensionX.normals](autofig.call.CallDimensionX.normals.md).
* `yerror` (float or list/array, optional, default=None): errors for `y`.
    See [autofig.call.Mesh.y](autofig.call.Mesh.y.md) and [autofig.call.CallDimensionY.error](autofig.call.CallDimensionY.error.md).
* `yunit` (string or astropy unit, optional, default=None): units for `y`.
    See [autofig.call.Mesh.y](autofig.call.Mesh.y.md) and [autofig.call.CallDimensionY.unit](autofig.call.CallDimensionY.unit.md).
* `ylabel` (strong, optional, default=None): label for `y`.
    See [autofig.call.Mesh.y](autofig.call.Mesh.y.md) and [autofig.call.CallDimensionY.label](autofig.call.CallDimensionY.label.md).
* `ynormals` (list/array, optional, default=None): normals for `y`.
    Currently ignored.
    See [autofig.call.Mesh.y](autofig.call.Mesh.y.md) and [autofig.call.CallDimensionY.normals](autofig.call.CallDimensionY.normals.md).
* `zerror` (float or list/array, optional, default=None): errors for `z`.
    See [autofig.call.Mesh.z](autofig.call.Mesh.z.md) and [autofig.call.CallDimensionZ.error](autofig.call.CallDimensionZ.error.md).
* `zunit` (string or astropy unit, optional, default=None): units for `z`.
    See [autofig.call.Mesh.z](autofig.call.Mesh.z.md) and [autofig.call.CallDimensionZ.unit](autofig.call.CallDimensionZ.unit.md).
* `zlabel` (strong, optional, default=None): label for `x`.
    See [autofig.call.Mesh.z](autofig.call.Mesh.z.md) and [autofig.call.CallDimensionZ.label](autofig.call.CallDimensionZ.label.md).
* `znormals` (list/array, optional, default=None): normals for `z`.
    If provided then the back of the mesh can be ignored by setting
    `exclude_back=True`.
    See [autofig.call.Mesh.z](autofig.call.Mesh.z.md) and [autofig.call.CallDimensionZ.normals](autofig.call.CallDimensionZ.normals.md).
* `fcerror` (float or list/array, optional, default=None): errors for `fc`.
    See [autofig.call.Mesh.fc](autofig.call.Mesh.fc.md) and [autofig.call.CallDimensionC.error](autofig.call.CallDimensionC.error.md).
* `fcunit` (string or astropy unit, optional, default=None): units for `fc`.
    See [autofig.call.Mesh.fc](autofig.call.Mesh.fc.md) and [autofig.call.CallDimensionC.unit](autofig.call.CallDimensionC.unit.md).
* `fclabel` (strong, optional, default=None): label for `fc`.
    See [autofig.call.Mesh.fc](autofig.call.Mesh.fc.md) and [autofig.call.CallDimensionC.label](autofig.call.CallDimensionC.label.md).
* `ecerror` (float or list/array, optional, default=None): errors for `ec`.
    See [autofig.call.Mesh.ec](autofig.call.Mesh.ec.md) and [autofig.call.CallDimensionC.error](autofig.call.CallDimensionC.error.md).
* `ecunit` (string or astropy unit, optional, default=None): units for `ec`.
    See [autofig.call.Mesh.ec](autofig.call.Mesh.ec.md) and [autofig.call.CallDimensionC.unit](autofig.call.CallDimensionC.unit.md).
* `eclabel` (strong, optional, default=None): label for `ec`.
    See [autofig.call.Mesh.ec](autofig.call.Mesh.ec.md) and [autofig.call.CallDimensionC.label](autofig.call.CallDimensionC.label.md).
* `iunit` (string or astropy unit, optional, default=None): units for `i`.
    See [autofig.call.Mesh.i](autofig.call.Mesh.i.md) and [autofig.call.CallDimensionI.unit](autofig.call.CallDimensionI.unit.md).
* `itol` (float, optional, default=0.0): see [autofig.call.DimensionI.tol](autofig.call.DimensionI.tol.md).
* `axorder` (int, optional, default=None): see [autofig.call.Mesh.axorder](autofig.call.Mesh.axorder.md).
* `axpos` (tuple, optional, default=None): see [autofig.call.Mesh.axpos](autofig.call.Mesh.axpos.md).
* `title` (string, optional, default=None): see [autofig.call.Mesh.title](autofig.call.Mesh.title.md).
* `label` (string, optional, default=None): see [autofig.call.Mesh.label](autofig.call.Mesh.label.md).
* `linestyle` or `ls` (string, optional, default='solid'): see
    [autofig.call.Mesh.linestyle](autofig.call.Mesh.linestyle.md). Note: `linestyle` takes precedence
    over `ls` if both are provided.  So technically `ls` defaults
    to 'solid' and `linestyle` defaults to None.
* `consider_for_limits` (bool, optional, default=True): see
    [autofig.call.Call.consider_for_limits](autofig.call.Call.consider_for_limits.md).
* `exclude_back` (bool, optional, default=False): whether to exclude
    any elements pointing away from the screen.  This will be ignored
    for 3d projections or if `znormals` is not provided.  Setting this
    to True can save significant time in drawing the mesh in matplotlib,
    and is especially useful for closed surfaces if `fc` is not 'none'.
* `**kwargs`: additional keyword arguments are stored and passed on when
    attaching to a parent axes.  See [autofig.axes.Axes.add_call](autofig.axes.Axes.add_call.md).

Returns
---------
* the instantiated [autofig.call.Mesh](autofig.call.Mesh.md) object.

