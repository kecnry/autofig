from matplotlib import colors, markers

_mplcolors = ['k', 'b', 'r', 'g', 'p']
_mplcolors = _mplcolors + [c for c in colors.ColorConverter.colors.keys() + colors.cnames.keys() if c not in _mplcolors]
_mplmarkers = ['.', 'o', '+', 's', '*', 'v', '^', '<', '>', 'p', 'h', 'o', 'D']
# could do matplotlib.markers.MarkerStyle.markers.keys()
_mpllinestyles = ['solid', 'dashed', 'dotted', 'dashdot', 'None']
# could also do matplotlib.lines.lineStyles.keys()

class MPLPropCycler(object):
    def __init__(self, options=[]):
        self._options = options
        self._used = []
        self._used_tmp = []


    @property
    def options(self):
        return self._options

    @property
    def used(self):
        return list(set(self._used + self._used_tmp))

    @property
    def next(self):
        for option in self.options:
            if option not in self.used:
                self.add_to_used(option)
                return option
        else:
            return self.options[-1]

    @property
    def next_tmp(self):
        for option in self.options:
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
        if option not in self.options:
            raise ValueError("{} not one of {}".format(option, self.options))
        if option not in self._used:
            self._used.append(option)

    def add_to_used_tmp(self, option):
        if option in [None, 'None', 'none']:
            return
        if option not in self.options:
            raise ValueError("{} not one of {}".format(option, self.options))
        if option not in self._used_tmp:
            self._used_tmp.append(option)

    def clear_tmp(self):
        self._used_tmp = []
        return



class MPLColorCycler(MPLPropCycler):
    def __init__(self):
        super(MPLColorCycler, self).__init__(options=_mplcolors)

class MPLMarkerCycler(MPLPropCycler):
    def __init__(self):
        super(MPLMarkerCycler, self).__init__(options=_mplmarkers)

class MPLLinestyleCycler(MPLPropCycler):
    def __init__(self):
        super(MPLLinestyleCycler, self).__init__(options=_mpllinestyles)
