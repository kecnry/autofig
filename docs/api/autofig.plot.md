### [autofig](autofig.md).plot (function)


```py

def plot(*args, **kwargs)

```



Add a new [autofig.call.Plot](autofig.call.Plot.md) call to the current [autofig.figure.Figure](autofig.figure.Figure.md).

See also:

* [autofig.gcf](autofig.gcf.md)
* [autofig.figure.Figure.plot](autofig.figure.Figure.plot.md)
* [autofig.call.Plot.__init__](autofig.call.Plot.__init__.md)

Arguments
-----------
* `*args`: all arguments are passed on to [autofig.figure.Figure.plot](autofig.figure.Figure.plot.md),
    most of which are then passed on to [autofig.call.Plot.__init__](autofig.call.Plot.__init__.md).
* `**kwargs`: all keyword arguments are passed on to [autofig.figure.Figure.plot](autofig.figure.Figure.plot.md),
    most of which are then passed on to [autofig.call.Plot.__init__](autofig.call.Plot.__init__.md).

Returns
---------
* the return from [Figure.plot](Figure.plot.md)

