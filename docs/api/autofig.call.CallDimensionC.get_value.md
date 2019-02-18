### [autofig](autofig.md).[call](autofig.call.md).[CallDimensionC](autofig.call.CallDimensionC.md).get_value (method)


```py

def get_value(self, i=None, unit=None, uncover=None, trail=None, linebreak=None, sort_by_indep=None, attr='_value')

```



Access the value for a given value of `i` (independent-variable) depending
on which effects (i.e. uncover) are enabled.

If `uncover`, `trail`, or `linebreak` are None (default), then the value from
the parent [autofig.call.Call](autofig.call.Call.md) from [autofig.call.CallDimension.call](autofig.call.CallDimension.call.md)
(probably ([autofig.call.Plot](autofig.call.Plot.md)) will be used.  See [autofig.call.Plot.uncover](autofig.call.Plot.uncover.md),
[autofig.call.Plot.trail](autofig.call.Plot.trail.md), [autofig.call.Plot.linebreak](autofig.call.Plot.linebreak.md).

Arguments
-----------
* `i`
* `unit`
* `uncover`
* `trail`
* `linebreak`
* `sort_by_indep`
* `attr`

Returns
----------
* (array or None)

