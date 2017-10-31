from matplotlib import colors, markers
from . import common

_mplcolors = ['black', 'blue', 'red', 'green', 'purple']
_mplcolors = _mplcolors + [common.coloralias.map(c) for c in list(colors.ColorConverter.colors.keys()) + list(colors.cnames.keys()) if common.coloralias.map(c) not in _mplcolors]
_mplmarkers = ['.', 'o', '+', 's', '*', 'v', '^', '<', '>', 'p', 'h', 'o', 'D']
# could do matplotlib.markers.MarkerStyle.markers.keys()
_mpllinestyles = ['solid', 'dashed', 'dotted', 'dashdot', 'None']
# could also do matplotlib.lines.lineStyles.keys()





class MPLPropCycler(object):
    def __init__(self, prop, options=[]):
        self._prop = prop
        self._options_orig = options
        self._options = options
        self._used = []
        self._used_tmp = []

    def __repr__(self):
        return '<{}cycler | cycle: {} | used: {}>'.format(self._prop,
                                                          self.cycle,
                                                          self.used)


    @property
    def cycle(self):
        return self._options

    @cycle.setter
    def cycle(self, cycle):
        for option in cycle:
            if option not in self._options_orig:
                raise ValueError("invalid option: {}".format(option))
        self._options = cycle

    @property
    def used(self):
        return list(set(self._used + self._used_tmp))

    @property
    def next(self):
        for option in self.cycle:
            if option not in self.used:
                self.add_to_used(option)
                return option
        else:
            return self.options[-1]

    @property
    def next_tmp(self):
        for option in self.cycle:
            if option not in self.used:
                self.add_to_used_tmp(option)
                return option
        else:
            return self.options[-1]

    def get(self, option=None):
        if option is not None:
            self.add_to_used(option)
            return option
        else:
            return self.next

    def get_tmp(self, option=None):
        if option is not None:
            self.add_to_used_tmp(option)
            return option
        else:
            return self.next_tmp

    def add_to_used(self, option):
        if option in [None, 'None', 'none']:
            return
        if option not in self._options_orig:
            raise ValueError("{} not one of {}".format(option, self._options_orig))
        if option not in self._used:
            self._used.append(option)

    def replace_used(self, oldoption, newoption):
        if newoption in [None, 'None', 'none']:
            return
        if newoption not in self._options_orig:
            raise ValueError("{} not one of {}".format(newoption, self._options_orig))

        if oldoption in self._used:
            ind = self._used.index(oldoption)
            self._used[ind] = newoption
        elif oldoption in self._used_tmp:
            # in many cases the old option may actually be in _used_tmp but
            # None will be passed because we don't have access to the previous
            # state of the color cycler.  But _used_tmp will be reset on the
            # next draw anyways, so this doesn't really hurt anything.
            self._used_tmp.remove(oldoption)
            self.add_to_used(newoption)
        else:
            self.add_to_used(newoption)


    def add_to_used_tmp(self, option):
        if option in [None, 'None', 'none']:
            return
        if option not in self._options_orig:
            raise ValueError("{} not one of {}".format(option, self._options_orig))
        if option not in self._used_tmp:
            self._used_tmp.append(option)

    def clear_tmp(self):
        self._used_tmp = []
        return



class MPLColorCycler(MPLPropCycler):
    def __init__(self):
        super(MPLColorCycler, self).__init__('color', options=_mplcolors)

class MPLMarkerCycler(MPLPropCycler):
    def __init__(self):
        super(MPLMarkerCycler, self).__init__('marker', options=_mplmarkers)

class MPLLinestyleCycler(MPLPropCycler):
    def __init__(self):
        super(MPLLinestyleCycler, self).__init__('linestyle', options=_mpllinestyles)
