### [autofig](autofig.md).save (function)


```py

def save(filename, renders=[])

```



Save the current [autofig.figure.Figure](autofig.figure.Figure.md).  Note: this saves the autofig
figure object itself, not the image.  To save the image, call [autofig.draw](autofig.draw.md)
and pass `save`.

See also:
* [autofig.open](autofig.open.md)
* [autofig.to_dict](autofig.to_dict.md)
* [autofig.gcf](autofig.gcf.md)
* [autofig.figure.Figure.save](autofig.figure.Figure.save.md)

Arguments
-----------
* `filename` (string): path to save the figure instance.
* `renders` (list of dictionaries, default=[]): commands to execute
    for rendering when opened by the command-line tool or by passing
    `do_renders` to [autofig.open](autofig.open.md).  The format must
    be a list of dictionaries, where each dictionary must at least have
    'render': 'draw' or 'render': 'animate'.  Any additional key-value
    pairs will be passed as keyword arguments to the respective
    rendering method.

Returns
-----------
* (str) the path of the saved figure instance.

