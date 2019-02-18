### [autofig](autofig.md).[call](autofig.call.md).[MeshGroup](autofig.call.MeshGroup.md).draw (method)


```py

def draw(self, *args, **kwargs)

```



Calls [autofig.call.Plot.draw](autofig.call.Plot.draw.md) or [autofig.call.Mesh.draw](autofig.call.Mesh.draw.md) for each
[autofig.call.Call](autofig.call.Call.md) in the [autofig.call.CallGroup](autofig.call.CallGroup.md).

See also:

* [autofig.draw](autofig.draw.md)
* [autofig.figure.Figure.draw](autofig.figure.Figure.draw.md)
* [autofig.axes.Axes.draw](autofig.axes.Axes.draw.md)
* [autofig.call.Plot.draw](autofig.call.Plot.draw.md)
* [autofig.call.Mesh.draw](autofig.call.Mesh.draw.md)

Arguments
------------
* `*args`: all arguments are passed on to each [autofig.call.Call](autofig.call.Call.md).
* `**kwargs`: all keyword arguments are passed on to each
    [autofig.call.Call](autofig.call.Call.md).

Returns
-----------
* (list): list of all created matplotlib artists

