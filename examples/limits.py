import autofig

call1 = autofig.Plot(x=[0,10], y=[0,10])
call2 = autofig.Plot(x=[-5,5], y=[-5,5])
call3 = autofig.Plot(x=[-30,30], y=[-30,30], consider_for_limits=False)

ax = autofig.Axes(call1, call2, call3)

# xlimits should be (-5, 10) to encompass call1 and call2 (but ignoring call3)
print('x limits: {}'.format(ax.x.lim))


# now let's set padding to 10%
print("---set ax.pad=0.1---")
ax.pad = 0.1

# xlimits should now be (-6.5, 11.5)
print('x limits with {} padding: {}'.format(ax.x.pad, ax.x.lim))
# ylimits should be the same
print('y limits with {} padding: {}'.format(ax.y.pad, ax.y.lim))

# we can pad x and y differently by overriding the per-dimension padding
print("---set ax.y.pad=0---")
ax.y.pad = 0.0

# xlimits should stil be (-6.5, 11.5)
print('x limits with {} padding: {}'.format(ax.x.pad, ax.x.lim))
# ylimits should return back to (-5, 10)
print('y limits with {} padding: {}'.format(ax.y.pad, ax.y.lim))


# we can enable consider_for_limits for call3
print("---enable call3 consider_for_limits---")
call3.consider_for_limits = True

# xlimits should now be (-36,36)
print('x limits with {} padding: {}'.format(ax.x.pad, ax.x.lim))
# ylimits should now be (-30, 30)
print('y limits with {} padding: {}'.format(ax.y.pad, ax.y.lim))
