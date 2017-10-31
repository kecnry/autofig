import autofig
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,101)
y = x*2
s = np.sin(x)

print("constant size")
autofig.plot(x=x, y=y, s=1, marker='s', ls='solid', show=True)

print("different line and marker sizes")
# separate calls must be made to differentiate line from marker color
autofig.reset()
autofig.plot(x=x, y=y, s=3, marker='s', ls='None')
autofig.plot(x=x, y=y, s=1, marker='None', ls='solid', show=True)

print("size as markers")
autofig.reset()
autofig.plot(x=x, y=y, s=s, slabel='mass', sunit='kg', marker='s', ls='None', show=True)

print("size as lines")
autofig.reset()
autofig.plot(x=x, y=y, s=s, marker='None', ls='solid', show=True)

print("size as markers and lines")
autofig.reset()
autofig.plot(x=x, y=y, s=s, marker='s', ls='dashed', show=True)

print("multiple size scales")
autofig.reset()
autofig.plot(x=x, y=+2*x, s=+2*x, slabel='+2x', marker='s', ls='None')
autofig.plot(x=x, y=-2*x, s=-2*x, slabel='-2x', marker='o', ls='None', show=True)
