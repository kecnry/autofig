# autofig

**High-Level Interface to Create Figures/Animations with Matplotlib**

[![badge](https://img.shields.io/badge/github-kecnry%2Fautofig-blue.svg)](https://github.com/kecnry/autofig)
[![badge](https://img.shields.io/badge/pip-autofig-blue.svg)](https://pypi.org/project/autofig/)
[![badge](https://img.shields.io/badge/license-GPL3-blue.svg)](https://github.com/kecnry/autofig/blob/master/LICENSE)
[![badge](https://travis-ci.org/kecnry/autofig.svg?branch=master)](https://travis-ci.org/kecnry/autofig)
[![badge](https://readthedocs.org/projects/autofig/badge/?version=latest)](https://autofig.readthedocs.io/en/latest/?badge=latest)

This module provides a high-level interface to create figures/animations (currently only in matplotlib).  It was designed to be used within [PHOEBE](http://github.com/phoebe-project/phoebe2) but written in a way that it can be used as a standalone package.

Read the [latest documentation on readthedocs](https://autofig.readthedocs.io) or [browse the current documentation](./docs/index.md).

## Dependencies

* [matplotlib](https://github.com/matplotlib/matplotlib)
* [numpy](https://github.com/numpy/numpy)
* [astropy](https://github.com/astropy/astropy)

See the [travis report](https://travis-ci.org/kecnry/autofig) for details on the full testing-matrix.

## Installation

**autofig** is available via [pip](https://pypi.org/project/autofig/):

```
pip install autofig
```

Alternatively, to install from source, use the standard python setup.py commands.

To install globally:
```
python setup.py build
sudo python setup.py install
```

Or to install locally:
```
python setup.py build
python setup.py install --user
```

## Basic Usage

**autofig** is imported as a python module:

```
import autofig
```

Read the [latest documentation on readthedocs](https://autofig.readthedocs.io) or [browse the current documentation](./docs/index.md).

## Contributors

[Kyle Conroy](https://github.com/kecnry)

Contributions are welcome!  Feel free to file an issue or fork and create a pull-request.
