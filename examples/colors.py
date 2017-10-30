import autofig
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1,101)
y = x*2
c = x**2

print("constant color")
# constant color can be passed to c or color (color has priority over c)
autofig.plot(x=x, y=y, c='blue', marker='s', ls='none', show=True)

print("different line and marker color")
# separate calls must be made to differentiate line from marker color
autofig.reset()
autofig.plot(x=x, y=y, c='blue', marker='s', ls='None')
autofig.plot(x=x, y=y, c='red', marker='None', ls='solid', show=True)

print("color as markers")
# cmap can be sent as the matplotlib cmap instance, or as a string
autofig.reset()
autofig.plot(x=x, y=y, c=c, cmap='afmhot', marker='s', ms=6, ls='none', show=True)

print("color as lines")
autofig.reset()
autofig.plot(x=x, y=y, c=c, cmap='brg', marker='none', ls='solid', show=True)

print("color as markers and lines")
autofig.reset()
autofig.plot(x=x, y=y, c=c, cmap='rainbow', marker='s', ms=10, ls='solid', show=True)

print("multiple color scales")
autofig.reset()
autofig.plot(x=x, y=+2*x, c=+2*x, clabel='+2x', cmap='cool', marker='s', ms=6, ls='none')
autofig.plot(x=x, y=-2*x, c=-2*x, clabel='-2x', cmap='winter', marker='none', ls='solid', show=True)
