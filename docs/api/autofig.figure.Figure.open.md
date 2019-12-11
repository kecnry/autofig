### [autofig](autofig.md).[figure](autofig.figure.md).[Figure](autofig.figure.Figure.md).open (method)


```py

def open(cls, filename, do_renders=False, allow_renders_save=False)

```



Open a [autofig.figure.Figure](autofig.figure.Figure.md) from a saved file.

See also:
* [autofig.figure.Figure.save](autofig.figure.Figure.save.md)

Arguments
-----------
* `filename` (string): path to the saved figure instance
* `do_renders` (bool, default=False): whether to execute any render
    (ie. draw/animate) statements included in the file.
* `allow_renders_save` (bool, default=False): whether to allow render
    statements to save images/animations to disk.  Be careful if setting
    this to True from an untrusted source.

Returns
---------
* the loaded [autofig.figure.Figure](autofig.figure.Figure.md) instance.

Raises
----------
* ValueError: if `do_render` is True but the render statements are invalid.

