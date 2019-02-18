
# Autofig Objects


```python
import autofig
import numpy as np
import astropy.units as u
```

``autofig`` works by creating a hierarchy of objects which dictates how a figure should be rendered.  These exist at three main levels:
* Figure
* Axes
  * AxesDimension (i, x, y, z, c, s)
* Call (Plot or Mesh)
  * CallDimension (i, x, y, z, c, s)

Calling `autofig.plot` is simply a shortcut to accessing a built-in Figure object.  We can access this object via `autofig.gcf()` (get current figure) at anytime, or can call the plot method of an instantiated Figure directly.


```python
autofig.reset()
autofig.plot(x=[1,2,3], xunit='s', y=[1,2,3], c=[1,2,3], i='x', uncover=True)
autofig.gcf()
```




    <Figure | 1 axes | 1 call(s)>




```python
figure = autofig.Figure()
figure.plot(x=[1,2,3], xunit='s', y=[1,2,3], c=[1,2,3], i='x', uncover=True)
figure
```




    <Figure | 1 axes | 1 call(s)>



## Figure

### Options

The Figure object holds the collection of Axes objects and is in charge of the subplot layout.  As such, it does not currently accept or hold many options.

### Methods

The Figure object has the following methods:
* plot
* mesh (not yet implemented)
* reset_draw
* draw
* animate
* add_axes
* add_call

### Hierarchy Links

From the Figure object, you can access the list of children axes:


```python
figure.axes
```




    <AxesGroup | 1 items | >



as well as the list of all Call objects in those axes:


```python
figure.calls
```




    <PlotGroup | 1 items | >



## Axes


```python
axes = figure.axes[0]
axes
```




    <Axes | 1 call(s) | dims: c>



### Options

#### equal_aspect


```python
axes.equal_aspect
```




    False



#### pad_aspect


```python
axes.pad_aspect
```




    False



### Methods

The Axes object has the following methods:
* draw
* add_call

### Hierarchy Links

From the Axes object, you can access the parent Figure or a list of the children Call objects


```python
axes.figure
```




    <Figure | 1 axes | 1 call(s)>




```python
axes.calls
```




    <PlotGroup | 1 items | >



As well as any of its dimensions (i, x, y, z)


```python
axes.x
```




    <x | limits: (None, None) | type: time | label: >



Or a combination of the cartesian dimensions


```python
axes.xyz
```




    <AxDimensionGroup | 3 items | directions: x, y, z | labels: , , >




```python
axes.xy
```




    <AxDimensionGroup | 2 items | directions: x, y | labels: , >



or a list of its color/size dimensions (cs, ss)


```python
axes.cs
```




    <AxDimensionGroup | 1 items | directions: c | labels: >



## AxesDimension


```python
ad = axes.x
ad
```




    <x | limits: (None, None) | type: time | label: >



### Options

#### unit

The unit in the AxesDimension will be those actually plotted (i.e. all values will be converted from their stored units to these)


```python
ad.unit
```




$\mathrm{s}$




```python
ad.unit='d'
ad.unit
```




$\mathrm{d}$



#### pad

Padding provided to an AxesDimension will override the default padding on the Axes itself.  Here since it has not been set yet, it defaults to the value from the Axes


```python
ad.pad
```




    0.1




```python
axes.pad=0.05
ad.pad
```




    0.1




```python
ad.pad=0.15
axes.pad=0.08
ad.pad
```




    0.15



#### lim

Limits will adhere to the padding of the same AxesDimension.


```python
ad.lim
```




    (None, None)




```python
ad.pad=0.0
ad.lim
```




    (None, None)



#### label


```python
ad.label
```




    ''




```python
ad.label='mylabel'
ad.label_with_units
```




    'mylabel [$\\mathrm{d}$]'



### Hierarchy Links

The AxesDimension object has a link back to its parent Axes


```python
ad.axes
```




    <Axes | 1 call(s) | dims: c>



## Cyclers


```python
lsc = axes.linestylecycler
lsc
```




    <linestylecycler | cycle: ['solid', 'dashed', 'dotted', 'dashdot'] | used: []>



### Options

#### cycle

The cycle defines the order at which the properties will be drawn.


```python
lsc.cycle
```




    ['solid', 'dashed', 'dotted', 'dashdot']



If desired, you can change this default order (Note: the cycle can be shorter than the original, but you cannot add new items)


```python
lsc.cycle = ['dashed', 'dotted', 'dashdot', 'solid']
```

## Plot (Call)


```python
plot = axes.calls[0]
plot
```




    <Call:Plot | dims: i, x, y, c>



### Options

#### kwargs (sent on to matplotlib, when possible)


```python
plot.kwargs
```




    {}



#### highlight


```python
plot.highlight
```




    True




```python
plot.highlight_marker
```




    'o'



If None, highlight_size will default to size


```python
plot.highlight_size
```




    0.04




```python
plot.highlight_linestyle
```




    'None'



If None, highlight_color will default to color


```python
plot.highlight_color
```

#### uncover


```python
plot.uncover
```




    True




```python
plot.uncover=True
ad.get_lim(i=1.5)
```




    (1.1574074074074073e-05, 3.472222222222222e-05)




```python
plot.uncover=False
ad.get_lim(i=1.5)
```




    (1.1574074074074073e-05, 3.472222222222222e-05)



#### consider for limits


```python
plot.consider_for_limits=False
ad.get_lim(i=1.5)
```




    (None, None)




```python
plot.consider_for_limits=True
ad.get_lim(i=1.5)
```




    (1.1574074074074073e-05, 3.472222222222222e-05)



### Methods

The Plot object has the following methods:
* draw

### Hierarchy Links

The Plot object has a link back to its parent Axes and grandparent Figure objects.


```python
plot.axes
```




    <Axes | 1 call(s) | dims: c>




```python
plot.figure
```




    <Figure | 1 axes | 1 call(s)>




## PlotDimension


```python
pd = plot.x
pd
```




    <x | len: 3 | type: time | label: None>



### Options

#### unit

The unit in PlotDimension holds the units of the provided array.  These will be converted to the necessary units for plotting.  Changing this unit does not do any converting of the array, so change with caution.


```python
pd.unit
```




$\mathrm{s}$



#### label


```python
pd.label
```

### Methods

#### get_value

In addition to the 'value' property, get_value will handle hiding values after 'i' and interpolating to that exact value.


```python
pd.get_value()
```




    array([1, 2, 3])




```python
plot.uncover=False
pd.get_value(i=1.5)
```




    array([1, 2, 3])




```python
plot.uncover=True
pd.get_value(i=1.5)
```




    array([1. , 1.5])



#### get_error (for cartesian only)

Same as above for get_value, except interpolation will not be used for the final value.

#### interpolate_at_i

interpolate_at_i simply interpolates the value for a given value of the independent variable


```python
pd.interpolate_at_i(i=1.5)
```




    1.5



### Hierarchy Links

The CallDimension objects have shortcuts back to their parent Call (Plot or Mesh)


```python
pd.call
```




    <Call:Plot | dims: i, x, y, c>


