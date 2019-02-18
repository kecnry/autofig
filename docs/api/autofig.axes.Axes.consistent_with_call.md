### [autofig](autofig.md).[axes](autofig.axes.md).[Axes](autofig.axes.Axes.md).consistent_with_call (method)


```py

def consistent_with_call(self, call)

```



Check to see if a new [autofig.call.Call](autofig.call.Call.md) would be consistent to add to
this [autofig.axes.Axes](autofig.axes.Axes.md) instance.

Cchecks include:

* compatible units in all directions
* compatible independent-variable (if applicable)

Arguments
-----------
* `call` ([autofig.call.Call](autofig.call.Call.md))

Returns
----------
* (bool, string): whether the call is consistent, and a message describing
    why/why not (usually empty if returning True).

