### [autofig](autofig.md).save (function)


```py

def save(filename)

```



Save the current [autofig.figure.Figure](autofig.figure.Figure.md).  Note: this saves the autofig
figure object itself, not the image.  To save the image, call [autofig.draw](autofig.draw.md)
and pass `save`.

See also:
* [autofig.open](autofig.open.md)
* [autofig.gcf](autofig.gcf.md)
* [autofig.figure.Figure.save](autofig.figure.Figure.save.md)

Arguments
-----------
* `filename` (string): path to save the figure instance.

Returns
-----------
* (str) the path of the saved figure instance.

