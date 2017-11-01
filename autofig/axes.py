import numpy as np
import astropy.units as u
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import LineCollection
from matplotlib import colorbar as mplcolorbar

from . import common
from . import cyclers
from . import call as _call

def _consistent_allow_none(thing1, thing2):
    if thing1 is None or thing2 is None:
        return True
    else:
        return thing1 == thing2

class AxesGroup(common.Group):
    def __init__(self, items):
        super(AxesGroup, self).__init__(Axes, [], items)


class Axes(object):
    def __init__(self, *calls, **kwargs):
        self._figure = None

        self._backend_object = None
        self._backend_artists = []

        self._colorcycler = cyclers.MPLColorCycler()
        self._markercycler = cyclers.MPLMarkerCycler()
        self._linestylecycler = cyclers.MPLLinestyleCycler()

        self._calls = []

        self._i = AxDimensionI(self, **kwargs)
        self._x = AxDimensionX(self, **kwargs)
        self._y = AxDimensionY(self, **kwargs)
        self._z = AxDimensionZ(self, **kwargs)

        # set default padding
        self.xyz.pad = 0.1

        self._ss = []
        self._cs = []

        self.add_call(*calls)

    def __repr__(self):
        dirs = []
        for direction in common.dimensions:
            if direction in ['c', 's']:
                if len(getattr(self, '{}s'.format(direction))):
                    dirs.append(direction)
            elif getattr(self, direction).lim != (None, None):
                dirs.append(direction)

        ncalls = len(self.calls)
        return "<Axes | {} call(s) | dims: {}>".format(ncalls, ", ".join(dirs))

    @property
    def figure(self):
        # no setter as this can only be set internally when attaching to a figure
        return self._figure

    @property
    def calls(self):
        return self._calls

    @property
    def colorcycler(self):
        return self._colorcycler

    @property
    def markercycler(self):
        return self._markercycler

    @property
    def linestylecycler(self):
        return self._linestylecycler

    @property
    def i(self):
        return self._i

    @property
    def indep(self):
        return self.i

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @property
    def xy(self):
        return AxDimensionGroup([self.x, self.y])

    @property
    def xyz(self):
        return AxDimensionGroup([self.x, self.y, self.z])

    @property
    def ss(self):
        return AxDimensionGroup(self._ss)

    @property
    def sizes(self):
        return self.ss

    @property
    def cs(self):
        return AxDimensionGroup(self._cs)

    @property
    def colors(self):
        return self.cs

    def consistent_with_call(self, call):
        """
        check to see if a new call would be consistent to add to this Axes instance

        checks include:
        * compatible units in all directions
        * compatible independent-variable (if applicable)
        """
        if len(self.calls) == 0:
            return True, ''

        msg = []
        # TODO: include s, c, fc, ec, etc and make these checks into loops
        if call.x.unit.physical_type != self.x.unit.physical_type:
            msg.append('inconsitent xunit, {} != {}'.format(call.x.unit, self.x.unit))
        if call.y.unit.physical_type != self.y.unit.physical_type:
            msg.append('inconsitent yunit, {} != {}'.format(call.y.unit, self.y.unit))
        if call.z.unit.physical_type != self.z.unit.physical_type:
            msg.append('inconsitent zunit, {} != {}'.format(call.z.unit, self.z.unit))
        if call.i.unit.physical_type != self.i.unit.physical_type:
            msg.append('inconsistent iunit, {} != {}'.format(call.i.unit, self.i.unit))
        if call.i.is_reference or self.i.is_reference:
            if call.i.reference != self.i.reference:
                msg.append('inconsistent i reference, {} != {}'.format(call.i.reference, self.i.reference))

        # here we send the protected _label so that we get None instead of empty string
        if not _consistent_allow_none(call.x._label, self.x._label):
            msg.append('inconsitent xlabel, {} != {}'.format(call.x.label, self.x.label))
        if not _consistent_allow_none(call.y._label, self.y._label):
            msg.append('inconsitent ylabel, {} != {}'.format(call.y.label, self.y.label))
        if not _consistent_allow_none(call.z._label, self.z._label):
            msg.append('inconsitent zlabel, {} != {}'.format(call.z.label, self.z.label))


        if len(msg):
            return False, ', '.join(msg)
        else:
            return True, ''

    def add_call(self, *calls):
        if len(calls) > 1:
            for c in calls:
                self.add_call(c)
            return

        elif len(calls) == 1:
            call = calls[0]
            if not isinstance(call, _call.Call):
                raise TypeError("call must be of type Call")

            consistent, reason = self.consistent_with_call(call)
            if not consistent:
                raise ValueError("call is not consistent with Axes: {}".format(reason))

            call._axes = self
            self._calls.append(call)

            if len(self.calls) == 1:
                # then this was the first, so set default units
                self.x.unit = call.x.unit
                self.y.unit = call.y.unit
                self.z.unit = call.z.unit
                self.i.unit = call.i.unit

                self.i.reference = call.i.reference

            # either way, fill in any missing labels - first set instance
            # will stick.  We check the protected underscored version to have
            # access to None instead of the empty string.
            if self.x._label is None:
                self.x.label = call.x._label
            if self.y._label is None:
                self.y.label = call.y._label
            if self.z._label is None:
                self.z.label = call.z._label

            # append the set props to the prop cycler.  Any prop that is None
            # will then request a temporary unused value from the prop cycler
            # at draw-time but will remain None in the object
            self._colorcycler.add_to_used(call.get_color())
            self._linestylecycler.add_to_used(call.get_linestyle())
            self._markercycler.add_to_used(call.get_marker())


            # handle axes-level colorscale(s)
            if call.c.value is not None and not isinstance(call.c.value, str):
                # now check to see whether we're consistent with any of the existing
                # colorscales - in reverse priority (i.e. the first most-recently
                # added match will be applied)
                used_cmaps = []
                for c in reversed(self.cs):
                    if c.consistent_with_calldimension(call.c):
                        c_match = c
                        break
                    used_cmaps.append(c.cmap)
                else:
                    # then we haven't found any matches so we need to add a new
                    # color dimension.  But first we want to make sure the cmap
                    # isn't in use by an existing colordimension.
                    if call.c.cmap in used_cmaps:
                        raise ValueError("cmap already in use in this axes, but could not attach to same colorscale")

                    c_match = AxDimensionC(self, unit=call.c.unit,
                                           label=call.c.label,
                                           cmap=call.c.cmap)

                    self._cs.append(c_match)

                # when the Call is in its draw method, it needs to know which
                # of the colorscales to obey.
                call._axes_c = c_match
                c_match._calls.append(call)

            # handle axes-level sizescale(s)
            if call.s.value is not None and not (isinstance(call.s.value, float) or isinstance(call.s.value, int)):
                # now check to see whether we're consistent with any of the existing
                # sizescales - in reverse priority (i.e. the first most-recently
                # added match will be applied)
                for s in reversed(self.ss):
                    if s.consistent_with_calldimension(call.s):
                        s_match = s
                        break
                else:
                    # unlike colors, we don't really care if the cmap is in
                    # use by an existing sizedimension
                    s_match = AxDimensionS(self, unit=call.s.unit,
                                           label=call.s.label,
                                           smap=call.s.smap)

                    self._ss.append(s_match)

                # when the Call is in its draw method, it needs to know which of
                # the sizescales to obey
                call._axes_s = s_match
                s_match._calls.append(call)

    def append_subplot(self, fig=None):
        def determine_grid(N):
            cols = np.floor(np.sqrt(N))
            rows = np.ceil(float(N)/cols) if cols > 0 else 1
            return int(rows), int(cols)

        if fig is None:
            fig = plt.gcf()

        N = len(fig.axes)

        # we'll reset the layout later anyways
        ax_new = fig.add_subplot(1,N+1,N+1)

        axes = fig.axes
        N = len(axes)

        rows, cols = determine_grid(N)

        for i,ax in enumerate(axes):
            ax.change_geometry(rows, cols, i+1)

        ax = self._get_backend_object(ax_new)
        self._backend_artists = []

        return ax

    def _get_backend_object(self, ax=None):
        if ax is None:
            if self._backend_object:
                ax = self._backend_object
            else:
                ax = plt.gca()
        else:
            if not isinstance(ax, plt.Axes):
                raise TypeError("ax must be of type plt.Axes")

        self._backend_object = ax

        return ax

    def _get_backend_artists(self):
        return self._backend_artists

    def draw(self, ax=None, i=None, calls=None, show=False, save=False):
        ax = self._get_backend_object(ax)

        # return_calls = []
        self._colorcycler.clear_tmp()
        self._linestylecycler.clear_tmp()
        self._markercycler.clear_tmp()
        for call in self.calls:
            if calls is None or call in calls:
                artists = call.draw(ax=ax, i=i,
                                    colorcycler=self._colorcycler,
                                    markercycler=self._markercycler,
                                    linestylecycler=self._linestylecycler)
                # return_calls.append(call)
                self._backend_artists += artists

        for c in self.cs:
            # then make axes for the colorbar(s) to sit in
            cbax, cbkwargs = mplcolorbar.make_axes((ax,), location='right', fraction=0.15, shrink=1.0, aspect=20, panchor=False)

            cb = mplcolorbar.ColorbarBase(cbax, cmap=c.cmap, norm=c.get_norm(i=i), **cbkwargs)
            cb.set_label(c.label_with_units)

        for s in self.ss:
            sbax, sbkwargs = mplcolorbar.make_axes((ax,), location='right', fraction=0.15, shrink=1.0, aspect=20, panchor=False)
            ys, sizes = s.get_sizebar_samples(i=i)
            # TODO: how to handle marker/color???
            sbax_done_markers = ['None']
            sbax_needs_line = False
            x = 0
            for n,call in enumerate(s.calls):
                # still not sure how to access the USED marker without
                # re-envoking the cycler...
                marker = call.get_marker()
                if marker not in sbax_done_markers:
                    x += 1
                    xs = [x]*len(ys)
                    sbax_done_markers.append(marker)
                    sbax.scatter(xs, ys, s=sizes,
                                 marker=call.get_marker(), color='black',
                                 linewidths=0)

                linestyle = call.get_linestyle()
                if linestyle != 'None':
                    sbax_needs_line = True

            if sbax_needs_line:
                x += 1 # for counter for xlim
                # we'll sample linewidths at a higher rate
                ys, sizes = s.get_sizebar_samples(nsamples=100, i=i)
                xs = [x]*len(ys)
                points = np.array([xs, ys]).T.reshape(-1, 1, 2)
                segments = np.concatenate([points[:-1], points[1:]], axis=1)
                lc = LineCollection(segments, color='k', linewidth=sizes)
                sbax.add_collection(lc)


            sbax.yaxis.set_ticks_position('right')
            sbax.yaxis.set_label_position('right')
            sbax.set_xlim(0, x+1)
            sbax.set_xticks([])
            sbax.set_ylim(s.get_lim(i=i))
            sbax.set_ylabel(s.label_with_units)

        # for s in self.ss:
            # for sbs in s.get_sizebar_samples(n=3, i=i):
                # we have to make dummy calls to scatter with a label in
                # order to show these in the legend.

        axes_3d = isinstance(ax, Axes3D)

        ax.set_xlabel(self.x.label_with_units)
        ax.set_ylabel(self.y.label_with_units)
        if axes_3d:
            ax.set_zlabel(self.z.label_with_units)

        ax.set_xlim(*self.x.get_lim(i=i))
        ax.set_ylim(*self.y.get_lim(i=i))
        if axes_3d:
            ax.set_zlim(*self.z.get_lim(i=i))

        if show:
            plt.show()

        if save:
            plt.savefig(save)

        # return return_calls


class AxDimensionGroup(common.Group):
    def __init__(self, items):
        super(AxDimensionGroup, self).__init__(AxDimension, ['direction', 'label'], items)

    @property
    def direction(self):
        return self._get_attrs('direction')

    @property
    def unit(self):
        return self._get_attrs('unit')

    @unit.setter
    def unit(self, unit):
        return self._set_attrs('unit', unit)

    @property
    def pad(self):
        return self._get_attrs('pad')

    @pad.setter
    def pad(self, pad):
        return self._set_attrs('pad', pad)

    @property
    def lim(self):
        return self._get_attrs('lim')

    @lim.setter
    def lim(self, lim):
        return self._set_attrs('lim', lim)

    @property
    def label(self):
        return self._get_attrs('label')

    @label.setter
    def label(self, label):
        return self._set_attrs('label', label)

class AxDimension(object):
    def __init__(self, direction, axes, unit=None, pad=None, lim=[None, None], label=None):
        self._axes = axes
        self.direction = direction
        self.unit = unit
        self.pad = pad
        self.lim = lim
        self.label = label

    def __repr__(self):

        return "<{} | limits: {} | type: {} | label: {}>".format(self.direction,
                                                                 self.lim,
                                                                 self.unit.physical_type,
                                                                 self.label)

    @property
    def axes(self):
        return self._axes

    @property
    def direction(self):
        """
        access the direction
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        set the direction
        """
        if not isinstance(direction, str):
            raise TypeError("direction must be of type str")

        accepted_values = ['i', 'x', 'y', 'z', 's', 'c', 'fc', 'ec']
        if direction not in accepted_values:
            raise ValueError("must be one of: {}".format(accepted_values))

        self._direction = direction

    @property
    def unit(self):
        return self._unit

    @property
    def unit_string(self):
        return self.unit.to_string()

    @property
    def unit_latex(self):
        return self.unit._repr_latex_()

    @unit.setter
    def unit(self, unit):
        unit = common._convert_unit(unit)
        self._unit = unit

    @property
    def pad(self):
        return self._pad

    @pad.setter
    def pad(self, pad):
        # TODO type checking
        self._pad = pad

    def get_lim(self, pad=None, i=None):

        if pad is None:
            pad = self.pad

        if self.direction == 'i':
            # then this doesn't really make sense
            return (None, None)

        lim_orig = self._lim

        if isinstance(lim_orig, tuple):
            # we'll need to edit the entries, so cast to list
            lim = list(self._lim)
        else:
            lim = [None, None]

        fixed_min = lim[0] is not None
        fixed_max = lim[1] is not None

        if lim_orig == 'fixed':
            # then fixed with automatic limits, ignoring i
            kind = 'fixed'
        elif isinstance(lim_orig, tuple):
            # then fixed with set limits, we'll still get the array in
            # case fixed_min==False or fixed_max==False
            kind = 'fixed'
        elif lim_orig == 'symmetric':
            kind = 'fixed'
        elif lim_orig == 'frame':
            # then per-frame limits
            kind = 'frame'
        elif lim_orig == 'sliding':
            # then sliding with automatic range
            kind = 'sliding'
        elif lim_orig is None:
            kind = 'sliding'
        elif isinstance(lim_orig, float):
            # then sliding with fixed range
            # let's also disable padding
            fixed_min = True
            fixed_max = True
            kind = 'sliding'

        else:
            raise NotImplementedError

        if kind == 'sliding':
            central_values = []
            for call in self.axes.calls:
                if not call.consider_for_limits:
                    continue
                if not hasattr(call, self.direction):
                    continue

                central_values.append(getattr(call, self.direction).interpolate_at_i(i))

            central_value = np.mean(central_values)

            if lim_orig in [None, 'sliding']:
                # then automatically try to determine the range
                rang = 0

                # try to set based on the maximum spread of the central values
                # through all available indeps
                # TODO: please make the following line less hideous
                indeps = list(set(np.concatenate([call.i.value.tolist() for call in self.axes.calls])))
                for indep in indeps:
                    central_values = []
                    for call in self.axes.calls:
                        # TODO: handle meshes differently by checking max-extent of mesh
                        try:
                            interp_in_direction = getattr(call, self.direction).interpolate_at_i(indep)
                        except ValueError:
                            pass
                        else:
                            central_values.append(interp_in_direction)

                    rang_at_indep = max(central_values) - min(central_values)
                    if rang_at_indep > rang:
                        rang = rang_at_indep

                if rang == 0:
                    # TODO: we should be able to predict this and avoid wasting time above
                    # if call.i.get_value()==self.direction for all calls in self.axes.calls?

                    # then fallback on 10% of the array(s)
                    for call in self.axes.calls:
                        array = getattr(call, self.direction).get_value(None)
                        rang_this_call = 0.1 * (np.max(array) - np.min(array))

                        if rang_this_call > rang:
                            rang = rang_this_call
                # else:
                    # raneg = rang * (1+pad)
                    # print "rang after padding", rang
            else:
                rang = float(lim_orig)

            # TODO: how will this handle flipped axes?
            lim = [central_value-rang/2, central_value+rang/2]


        elif kind in ['fixed', 'frame']:
            for call in self.axes.calls:
                if not call.consider_for_limits:
                    continue
                if not hasattr(call, self.direction):
                    continue

                if kind=='fixed':
                    array = getattr(call, self.direction).get_value(None)
                elif kind=='frame':
                    array = getattr(call, self.direction).get_value(i)
                else:
                    raise NotImplementedError

                if not fixed_min and (lim[0] is None or np.min(array) < lim[0]):
                    lim[0] = np.min(array)
                if not fixed_max and (lim[1] is None or np.max(array) > lim[1]):
                    lim[1] = np.max(array)

        else:
            raise NotImplementedError

        if lim_orig == 'symmetric':
            limabs = max(abs(np.array(lim)))
            # TODO: how will this work with inverting?
            lim = [-limabs, limabs]

        # now handle padding
        if pad is not None and lim != [None, None]:
            rang = abs(lim[1] - lim[0])
            if not fixed_min:
                lim[0] -= rang*pad
            if not fixed_max:
                lim[1] += rang*pad

        return tuple(lim)

    @property
    def lim(self):
        return self._lim

    @lim.setter
    def lim(self, lim):
        """
        set lim (limits)
        """
        if lim is None:
            self._lim = lim
            return

        typeerror_msg = "lim must be of type tuple, float, None, or in ['fixed', 'symmetric', 'frame', 'sliding']"

        if isinstance(lim, str):
            if lim in ['fixed', 'symmetric', 'frame', 'sliding']:
                self._lim = lim
                return
            else:
                raise ValueError(typeerror_msg)

        if isinstance(lim, int):
            lim = float(lim)

        if isinstance(lim, float):
            if lim <= 0.0:
                raise ValueError("lim cannot be <= 0")
            self._lim = lim
            return

        if not isinstance(lim, tuple):
            try:
                lim = tuple(lim)
            except:
                raise TypeError(typeerror_msg)

        if not len(lim)==2:
            raise ValueError('lim must have length 2')

        for l in lim:
            if not (isinstance(l, float) or isinstance(l, int) or l is None):
                raise ValueError("each item in limit must be of type float, int, or None")

        self._lim = lim

    @property
    def label(self):
        return '' if self._label is None else self._label

    @property
    def label_with_units(self):
        if self.unit.physical_type != 'dimensionless':
            return r"{} [{}]".format(self.label, self.unit_latex)
        else:
            return r"{}".format(self.label)

    @label.setter
    def label(self, label):
        self._label = label


def _process_dimension_kwargs(direction, kwargs):
    """
    process kwargs for AxDimension instances by stripping off the prefix
    for the appropriate direction
    """
    acceptable_keys = ['unit', 'pad', 'lim', 'label']
    processed_kwargs = {}
    for k,v in kwargs.items():
        if k.startswith(direction):
            processed_key = k.lstrip(direction)
        else:
            processed_key = k

        if processed_key in acceptable_keys:
            processed_kwargs[processed_key] = v

    return processed_kwargs

class AxDimensionI(AxDimension):
    def __init__(self, *args, **kwargs):
        processed_kwargs = _process_dimension_kwargs('i', kwargs)
        self._reference = None
        super(AxDimensionI, self).__init__('i', *args, **processed_kwargs)

    @property
    def is_reference(self):
        return self.reference is not None

    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        if not isinstance(reference, str) and reference is not None:
            raise TypeError("reference must be of type str")

        self._reference = reference

class AxDimensionX(AxDimension):
    def __init__(self, *args, **kwargs):
        processed_kwargs = _process_dimension_kwargs('x', kwargs)
        super(AxDimensionX, self).__init__('x', *args, **processed_kwargs)

class AxDimensionY(AxDimension):
    def __init__(self, *args, **kwargs):
        processed_kwargs = _process_dimension_kwargs('y', kwargs)
        super(AxDimensionY, self).__init__('y', *args, **processed_kwargs)

class AxDimensionZ(AxDimension):
    def __init__(self, *args, **kwargs):
        processed_kwargs = _process_dimension_kwargs('z', kwargs)
        super(AxDimensionZ, self).__init__('z', *args, **processed_kwargs)

class AxDimensionScale(AxDimension):
    def __init__(self, direction, *args, **kwargs):
        self._calls = []
        super(AxDimensionScale, self).__init__(direction, *args, **kwargs)

    @property
    def calls(self):
        return self._calls

    @property
    def default_pad(self):
        return 0.0

    def get_norm(self, pad=None, i=None):
        return plt.Normalize(*self.get_lim(pad=pad, i=i))

    @property
    def norm(self):
        return self.get_norm(pad=self.pad)

    def consistent_with_calldimension(self, calldimension):
        cd = calldimension
        if cd.direction != self.direction:
            raise TypeError("can only compare with another '{}' dimension".format(self.direction))

        if cd.unit.physical_type != self.unit.physical_type:
            return False

        if not _consistent_allow_none(cd._label, self._label):
            return False

        if self.direction=='c' and not _consistent_allow_none(cd.cmap, self.cmap):
            return False

        if self.direction=='s' and not _consistent_allow_none(cd.smap, self.smap):
            return False

        return True


class AxDimensionS(AxDimensionScale):
    def __init__(self, *args, **kwargs):
        processed_kwargs = _process_dimension_kwargs('s', kwargs)
        smap_ = kwargs.pop('smap', None)
        smap = kwargs.pop('sizemap', smap_)
        self.smap = smap


        self.nsamples = 20
        super(AxDimensionS, self).__init__('s', *args, **processed_kwargs)

    @property
    def nsamples(self):
        return self._nsamples

    @nsamples.setter
    def nsamples(self, nsamples):
        if not isinstance(nsamples, int):
            raise TypeError("nsamples must be of type int")
        if nsamples < 2:
            raise ValueError("nsamples must be >= 2")

        self._nsamples = nsamples

    @property
    def smap(self):
        smap = self._smap
        if smap is None:
            return (1,100)
        return smap

    @smap.setter
    def smap(self, smap):
        if smap is None:
            self._smap = smap
            return

        if not isinstance(smap, tuple):
            try:
                smap = tuple(smap)
            except:
                raise TypeError('smap must be of type tuple')

        if not len(smap)==2:
            raise ValueError('smap must have length 2')

        self._smap = smap

    def normalize(self, values, pad=None, i=None):
        norm = self.get_norm(pad=pad, i=None)
        values_normed = norm(values)
        smap = self.smap
        srang = smap[1] - smap[0]
        values_mapped = values_normed*srang+smap[0]
        return values_mapped

    def get_sizebar_samples(self, nsamples=None, pad=None, i=None):
        if nsamples is None:
            nsamples = self.nsamples
        lim = self.get_lim(pad=pad, i=i)
        smap = self.smap
        rang = float(lim[1] - lim[0])  # TODO: not sure how this will react with flipped limits
        srang = float(smap[1] - smap[0])
        samples = []
        sizes = []
        for i in range(nsamples):
            samples.append(lim[0]+i*rang/(nsamples-1))
            sizes.append(smap[0]+i*srang/(nsamples-1))
        return samples, sizes

class AxDimensionC(AxDimensionScale):
    def __init__(self, *args, **kwargs):
        cmap_ = kwargs.pop('cmap', None)
        cmap = kwargs.pop('colormap', cmap_)
        self.cmap = cmap

        processed_kwargs = _process_dimension_kwargs('c', kwargs)
        super(AxDimensionC, self).__init__('c', *args, **processed_kwargs)

    @property
    def default_pad(self):
        return 0.0

    @property
    def cmap(self):
        return self._cmap

    @cmap.setter
    def cmap(self, cmap):
        # print("setting axes cmap: {}".format(cmap))
        try:
            cmap = plt.get_cmap(cmap)
        except:
            raise TypeError("could not find cmap")

        self._cmap = cmap
