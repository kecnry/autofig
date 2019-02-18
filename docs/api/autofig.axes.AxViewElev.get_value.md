### [autofig](autofig.md).[axes](autofig.axes.md).[AxViewElev](autofig.axes.AxViewElev.md).get_value (method)


```py

def get_value(self, i, indeps=None)

```



Access the interpolated value at a given value of `i`
(independent-variable).

If `indeps` is not passed, then the entire range of `indeps` over all
calls is assumed.

Arguments
-----------
* `i` (float, array, or None)
* `indeps` (list/array or None, optional, default=None): must have same
    length as [autofig.axes.AxView.value](autofig.axes.AxView.value.md)

Returns
----------
* (float or array): interpolated value(s)

Raises
---------
* ValueError: if [autofig.axes.AxView.value](autofig.axes.AxView.value.md) and `indeps` have different
    lengths.

