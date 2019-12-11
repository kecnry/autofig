### [autofig](autofig.md).[figure](autofig.figure.md).[Figure](autofig.figure.Figure.md).to_dict (method)


```py

def to_dict(self, renders=[])

```



Export the current [autofig.figure.Figure](autofig.figure.Figure.md) to a json-safe dictionary.

See also:
* [autofig.figure.Figure.save](autofig.figure.Figure.save.md)

Arguments
-----------
* `filename` (string): path to save the figure instance.
* `renders` (list of dictionaries, default=[]): commands to execute
    for rendering when opened by the command-line tool or by passing
    `do_renders` to [autofig.figure.Figure.open](autofig.figure.Figure.open.md).  The format must
    be a list of dictionaries, where each dictionary must at least have
    'render': 'draw' or 'render': 'animate'.  Any additional key-value
    pairs will be passed as keyword arguments to the respective
    rendering method.


Returns
-----------
* (str) the path of the saved figure instance.

