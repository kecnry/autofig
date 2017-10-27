import autofig
import numpy as np

x = np.linspace(-10,10,101)
y = x**2

autofig.plot(x=x, y=y, i='x', marker='None', ls='solid', uncover=True, highlight=True)
autofig.animate(indeps=x, show=True)
