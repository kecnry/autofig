import autofig
import astropy.units as u

call1 = autofig.Plot(x=[1,2,3], xunit=u.solRad, xlabel='call1_x_label', y=[4,5,6], ylabel='call1_y_label', color='k', marker='.', linestyle='dashed', ms=15)
call2 = autofig.Plot(x=[2,4,6], xunit='solRad', y=[4,5,6], color='r', marker='x', ms=15)
call3 = autofig.Plot(x=[3,4,5], xunit='kg', y=[9,3,5], linestyle='dashed')

ax = autofig.Axes(call1, call2, xlabel='ax_x_label')
# ax.add_call(call3)  # RAISES ERROR

ax.draw(show=True)
