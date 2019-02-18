### [autofig](autofig.md).[axes](autofig.axes.md).[AxDimensionZ](autofig.axes.AxDimensionZ.md).get_zorders (method)


```py

def get_zorders(self, z, i=None)

```



Compute the zorders for all values in the array.  zorders are mapped
on the range 0-1000 depending on the current `zlim` given `i`.

Arguments
------------
* `z` (array or None): values in z in which to compute zorders.
* `i` (float or None, optional, default=None): value of `i` to use
    when calling [autofig.axes.AxDimensinZ.get_norm](autofig.axes.AxDimensinZ.get_norm.md).

Returns
--------
* (array, bool): (zorders, do_zorder)

