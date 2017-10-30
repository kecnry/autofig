import autofig
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1,101)
y = x*2
c = x**2

print("color as markers")
# cmap can be sent as the matplotlib cmap instance, or as a string
autofig.plot(x=x, y=y, c=c, cmap='brg', marker='s', ms=6, ls='none', show=True)

print("color as lines")
autofig.reset()
autofig.plot(x=x, y=y, c=c, cmap='afmhot', marker='none', ls='solid', show=True)

print("color as markers and lines")
autofig.reset()
autofig.plot(x=x, y=y, c=c, cmap='rainbow', marker='s', ms=10, ls='solid', show=True)
