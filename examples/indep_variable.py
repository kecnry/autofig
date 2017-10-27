import autofig
import numpy as np
import astropy.units as u

print("x as independent-variable")
x = np.linspace(-10,10,101)
autofig.plot(x=x, y=x**2, i='x', marker='None', ls='solid', highlight=True, uncover=False)
autofig.plot(x=x, y=2*x, i='x', marker='None', ls='solid', highlight=True, uncover=True)

autofig.draw(i=7.123, show=True)


print("'external' independent-variable")
time = np.linspace(0,2*np.pi,101)
x = np.cos(time)
y = np.sin(time)

autofig.reset()
autofig.plot(x=x, y=y, i=time, marker='None', ls='solid', highlight=True, uncover=True)
autofig.draw(i=3./2*np.pi, show=True)

print("padding on ALL data (fixed_limits=True)")
autofig.reset()

x = np.linspace(-10,10,101)
y = x**2

autofig.plot(x=x, y=y, i='x', marker='None', ls='solid', uncover=True)
print("xlimits with fixed_limits=True: {}".format(autofig.gcf().axes[0].x.get_lim(i=5)))
autofig.draw(i=5, show=True)


print("padding only on VISIBLE data (fixed_limits=False)")
autofig.gcf().axes[0].fixed_limits = False
print("xlimits with fixed_limits=False: {}".format(autofig.gcf().axes[0].x.get_lim(i=5)))
autofig.draw(i=5, show=True)
