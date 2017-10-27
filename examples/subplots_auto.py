import autofig

call1 = autofig.Call(x=[1,2,3], xunit='solRad', xlabel='call1_x_label', y=[4,5,6], ylabel='call1_y_label')
call2 = autofig.Call(x=[2,4,6], xunit='solRad', y=[4,5,6], ylabel='call2_y_label')
call3 = autofig.Call(x=[3,4,5], xunit='kg', y=[9,3,5], ylabel='call3_y_label')

# call1 & call2 have consistent units on all axes so will be on the same subplot
# call3 has different xunits so will get its own subplot
fig = autofig.Figure(call1, call2, call3)
fig.draw(show=True)
