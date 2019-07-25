### [autofig](autofig.md).[figure](autofig.figure.md).[Figure](autofig.figure.Figure.md).save (method)


```py

def save(self, filename)

```



Save the current [autofig.figure.Figure](autofig.figure.Figure.md).  Note: this saves the autofig
figure object itself, not the image.  To save the image, call
[autofig.figure.Figure.draw](autofig.figure.Figure.draw.md) and pass `save`.

Arguments
-----------
* `filename` (string): path to save the figure instance.


Returns
-----------
* (str) the path of the saved figure instance.

