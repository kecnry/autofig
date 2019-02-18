### [autofig](autofig.md).[axes](autofig.axes.md).[Axes](autofig.axes.Axes.md).add_call (method)


```py

def add_call(self, *calls)

```



Add a new [autofig.call.Call](autofig.call.Call.md) ([autofig.call.Plot](autofig.call.Plot.md) or [autofig.call.Mesh](autofig.call.Mesh.md))
to the [autofig.axes.Axes](autofig.axes.Axes.md).

Arguments
-------------
* `*calls` ([autofig.call.Call](autofig.call.Call.md)): positional arguments must each be an
    [autofig.call.Call](autofig.call.Call.md) object.

Raises
----------
* TypeError: if any argument is not of type [autofig.call.Call](autofig.call.Call.md).
* ValueError: if the [autofig.call.Call](autofig.call.Call.md) is not consistent with this
    [autofig.axes.Axes](autofig.axes.Axes.md).  See [autofig.axes.Axes.consistent_with_call](autofig.axes.Axes.consistent_with_call.md).

