### [autofig](autofig.md).[axes](autofig.axes.md).[AxDimensionY](autofig.axes.AxDimensionY.md).get_lim (function)


```py

def get_lim(self, pad=None, i=None)

```



Compute the adopted axes limits at a given value of `i`, given the
value of [autofig.axes.AxDimension.lim](autofig.axes.AxDimension.lim.md) and [autofig.axes.AxDimension.pad](autofig.axes.AxDimension.pad.md)
(or `pad`).

See also:

* [autofig.axes.AxDimension.lim](autofig.axes.AxDimension.lim.md)

Arguments
-----------
* `pad` (float, optional, default=None): override the padding.  If not
    provided or None, will use [autofig.axes.AxDimension.pad](autofig.axes.AxDimension.pad.md).
* `i` (float, optional, default=None): the value to use for `i` when
    computing visible data and limits.

Returns
--------
* (tuple): (min, max) in the [autofig.axes.AxDimension.direction](autofig.axes.AxDimension.direction.md)

