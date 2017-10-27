import autofig
import numpy as np

x = np.linspace(0,1,101)
y = x*2
c = x**2

print("color as markers")
autofig.plot(x=x, y=y, c=c, marker='s', ms=6, ls='none', show=True)

print("color as lines")
autofig.reset()
autofig.plot(x=x, y=y, c=c, marker='none', ls='solid', show=True)

print("color as markers and lines")
autofig.reset()
autofig.plot(x=x, y=y, c=c, marker='s', ms=10, ls='solid', show=True)
