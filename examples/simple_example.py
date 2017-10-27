import autofig
import astropy.units as u

call1 = autofig.Call(x=[1,2,3], xunit=u.solRad, xlabel='call1_x_label', y=[4,5,6], ylabel='call1_y_label')
call2 = autofig.Call(x=[2,4,6], xunit='solRad', y=[4,5,6])
call3 = autofig.Call(x=[3,4,5], xunit='kg', y=[9,3,5])

ax = autofig.Axes(call1, call2, xlabel='ax_x_label')
# ax.add_call(call3)  # RAISES ERROR

ax.draw(show=True)
