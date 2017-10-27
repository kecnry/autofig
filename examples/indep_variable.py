import autofig
import astropy.units as u

call1 = autofig.Plot(x=[1,2,3], xunit='solRad', y=[14,5,6], i='x')
call2 = autofig.Plot(x=[2,4,6], xunit='km', y=[4,5,16], i='x')
call3 = autofig.Plot(x=[1,3,5], y=[6,4,7], i=[0,1,2])

ax = autofig.Axes(call1, call2)
# ax.add_call(call3)  # throws error

fig = autofig.Figure(call1, call2, call3)
print fig.axes[0].indep.lim
