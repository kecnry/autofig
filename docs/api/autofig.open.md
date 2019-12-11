### [autofig](autofig.md).open (function)


```py

def open(filename, do_renders=False, allow_renders_save=False)

```



Open and replace the current [autofig.figure.Figure](autofig.figure.Figure.md).

See also:
* [autofig.save](autofig.save.md)
* [autofig.reset](autofig.reset.md)
* [autofig.gcf](autofig.gcf.md)

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

