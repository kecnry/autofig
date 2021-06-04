<p align="center"><a href="http://autofig.readthedocs.io"><img src="./images/autofig.png" alt="autofig logo" width="300px" align="center"/></a></p>

**High-Level Interface to Create Figures/Animations with Matplotlib**

[![badge](https://img.shields.io/badge/github-kecnry%2Fautofig-blue.svg)](https://github.com/kecnry/autofig)
[![badge](https://img.shields.io/badge/pip-autofig-blue.svg)](https://pypi.org/project/autofig/)
[![badge](https://img.shields.io/badge/license-GPL3-blue.svg)](https://github.com/kecnry/autofig/blob/master/LICENSE)
[![badge](https://travis-ci.org/kecnry/autofig.svg?branch=master)](https://travis-ci.org/kecnry/autofig)
[![badge](https://readthedocs.org/projects/autofig/badge/?version=latest)](https://autofig.readthedocs.io/en/latest/?badge=latest)

This module provides a high-level interface to create figures/animations (currently only in matplotlib).  It was designed to be used within [PHOEBE](http://github.com/phoebe-project/phoebe2) but written in a way that it can be used as a standalone package.

**autofig** aims to provide the following:

* a unified calling structure to matplotlib's [plot](http://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.plot.html), [scatter](http://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.scatter.html), [errorbar](http://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.errorbar.html), [LineCollection](http://matplotlib.org/gallery/shapes_and_collections/line_collection.html), and [PolyCollection](http://matplotlib.org/api/collections_api.html#matplotlib.collections.PolyCollection) in both 2D and 3D projections.  So if you decide you want to add errorbars or colorscaling to an existing plot call, you don't need to change the entire calling structure anymore.
* basic "3D" support within 2D figures (by providing the z-coordinate, the z-orders will automatically be set)
* a high-level wrapper to animate an existing plot over some independent-variable (i.e. time), with effects including highlight and uncover.
* intelligent options for axes limits within animations.
* intelligent defaults for subplot creation based on conflicts in units/labels.

In general, autofig attempts to provide smart defaults with a high-level interface while still providing full customization with access to the underlying matplotlib objects.



## Getting Started

### Dependencies

**autofig** requires the following dependencies:

* [matplotlib](https://github.com/matplotlib/matplotlib)
* [numpy](https://github.com/numpy/numpy)
* [astropy](https://github.com/astropy/astropy)


You can see the [Travis testing matrix](https://travis-ci.org/kecnry/autofig) for
details on what exact versions have been tested and ensured to work.  If you run
into any issues with dependencies, please [submit an issue](https://github.com/kecnry/autofig/issues/new).

### Installation

**autofig** is available via [pip](https://pypi.org/project/autofig/):

```sh
pip install autofig
```

Alternatively, to install from source, use the standard python setup.py commands.

To install globally:
```sh
python setup.py build
sudo python setup.py install
```

Or to install locally:
```sh
python setup.py build
python setup.py install --user
```

### Import

Now from within python we can import the `autofig` package:

```py
import autofig
```

## Tutorials

* [basics](./tutorials/basics.md)
* [limits](tutorials/limits.md)
* [size modes](tutorials/size_modes.md)
* [subplot/axes positioning](tutorials/subplot_positioning.md)
* [meshes](tutorials/mesh.md)
* [3d](tutorials/3d.md)
* [saving & loading](tutorials/saving_and_loading.md)
* [objects](tutorials/objects.md)
* [accessing matplotlib objects and calling custom commands](tutorials/matplotlib_objects.md)

## Gallery

Browse the [gallery](./gallery.md) to find an example script for various types of figures.

## API Documentation

See the [API documentation](./api.md) for full details on each type of available distribution.

## How it works

**autofig** builds up objects for the Figure, Axes, and individual plotting Calls (currently Plot or Mesh).  These then handle high-level functionality such as axes limits and subplot placement.

## Contributors

[Kyle Conroy](https://github.com/kecnry)

Contributions are welcome!  Feel free to file an issue or fork and create a pull-request.
