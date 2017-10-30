import autofig

def test_marker():
    autofig.reset()

    autofig.plot(x=[1,2,3], y=[1,2,3], marker=None)
    autofig.plot(x=[1,2,3], y=[1,2,3], marker='None')
    autofig.plot(x=[1,2,3], y=[1,2,3], marker='none')

def test_linestyle():
    autofig.reset()

    autofig.plot(x=[1,2,3], y=[1,2,3], linestyle=None)
    autofig.plot(x=[1,2,3], y=[1,2,3], linestyle='None')
    autofig.plot(x=[1,2,3], y=[1,2,3], linestyle='none')

    autofig.plot(x=[1,2,3], y=[1,2,3], ls=None)
    autofig.plot(x=[1,2,3], y=[1,2,3], ls='None')
    autofig.plot(x=[1,2,3], y=[1,2,3], ls='none')

if __name__ == '__main__':
    test_marker()
    test_linestyle()
