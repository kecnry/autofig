# autofig

autofig is a work-in-progress, and is not yet stable.

This module provides a high-level interface to create figures/animations (currently only in matplotlib).  It was designed to be used within [PHOEBE](http://github.com/phoebe-project/phoebe2).

**NOTE:** autofig is still a work in progress and so the API may change at any time.

## Dependencies

* [matplotlib](https://github.com/matplotlib/matplotlib)
* [numpy](https://github.com/numpy/numpy)
* [astropy](https://github.com/astropy/astropy)

See the [travis report](https://travis-ci.org/kecnry/autofig) for details on the full testing-matrix.

## Installation

Installation is done using the standard python setup.py commands.

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

autofig is imported as a python module:

```
import autofig
```

For more details, see the example scripts in the examples directory:

## How it works

autofig builds up objects for the Figure, Axes, and individual plotting Calls (currently Plot or Mesh).  These then handle high-level functionality such as axes limits and subplot placement.

## Contributing

Contributions are welcome!  Feel free to file an issue or fork and create a pull-request.
