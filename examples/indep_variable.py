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
