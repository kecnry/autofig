import autofig
import astropy.units as u

call1 = autofig.Call(x=[1,2,3], xunit=u.solRad, y=[4,5,6])
call2 = autofig.Call(x=[2,4,6], xunit='solRad', y=[4,5,6])
call_inconsistent = autofig.Call(x=[3,4,5], xunit='kg', y=[9,3,5])

ax = autofig.Axes(call1, call2, xlabel='myxlabel')
# ax.add_call(call_inconsistent)  # RAISES ERROR

# fig = autofig.Figure(call1, call2, call_inconsistent)
