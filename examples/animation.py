import autofig
import numpy as np

x = np.linspace(-10,10,101)
y = x**2

print("animate fixed_limits=True, pad=0")
autofig.reset()
autofig.plot(x=x, y=y, i='x', marker='None', ls='solid', uncover=True, highlight=True)
autofig.gcf().axes[0].fixed_limits=True  # will be by default
autofig.animate(indeps=x, show=True)

print("animate fixed_limits=False, pad=0.1")
autofig.reset()
autofig.plot(x=x, y=y, i='x', marker='None', ls='solid', uncover=True, highlight=True)
autofig.gcf().axes[0].fixed_limits=False
autofig.gcf().axes[0].pad=0.1
autofig.animate(indeps=x, show=True)


print("external independent-variable")
time = np.linspace(0, 2*np.pi, 101)
x = np.cos(time)
y = np.sin(time)

autofig.reset()
autofig.plot(x=x, y=y, i=time, marker='None', ls='solid', uncover=True, highlight=True, xlabel='x', ylabel='y')
autofig.gcf().axes[0].pad=0.1
autofig.animate(indeps=np.linspace(0, 2*np.pi, 21), show=True)

print("animation with colorscale and colorbar")
x = np.linspace(-10,10,101)
y = 2*x
c = x**2

autofig.reset()
autofig.plot(x=x, xlabel='x', y=y, ylabel='y', i='x', c=c, clabel='c', marker='None', ls='solid', uncover=True, highlight=True)
autofig.gcf().axes[0].fixed_limits = True # will be by default
autofig.animate(indeps=x[::5], show=True)
