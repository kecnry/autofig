### [autofig](autofig.md).[axes](autofig.axes.md).[AxDimensionS](autofig.axes.AxDimensionS.md).get_norm (function)


```py

def get_norm(self, pad=None, i=None)

```



Compute the adopted normalization at a given value of `i`, given the
value of [autofig.axes.AxDimension.pad](autofig.axes.AxDimension.pad.md) (or `pad`).

See also:

* [autofig.axes.AxDimension.norm](autofig.axes.AxDimension.norm.md)

Arguments
-----------
* `pad` (float, optional, default=None): override the padding.  If not
    provided or None, will use [autofig.axes.AxDimension.pad](autofig.axes.AxDimension.pad.md).
* `i` (float, optional, default=None): the value to use for `i` when
    computing visible data and limits.

Returns
--------
* (plt.Normalize object)

