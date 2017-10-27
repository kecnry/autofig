import autofig
import numpy as np
import astropy.units as u

x = np.linspace(-10,10,101)
autofig.plot(x=x, y=x**2, i='x', marker='None', ls='solid', highlight=True, uncover=False)
autofig.plot(x=x, y=2*x, i='x', marker='None', ls='solid', highlight=True, uncover=True)

autofig.draw(i=7.123, show=True)
