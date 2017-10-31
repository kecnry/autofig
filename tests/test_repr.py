import autofig
from nose.tools import assert_raises

def test_repr():
    autofig.reset()

    autofig.plot(x=[1,2,3], y=[1,2,3], c=[1,2,3], s=[1,2,3])

    print(autofig.gcf())
    print(autofig.gcf().axes)
    print(autofig.gcf().axes[0])
    print(autofig.gcf().axes[0].i)
    print(autofig.gcf().axes[0].x)
    print(autofig.gcf().axes[0].cs)
    print(autofig.gcf().axes[0].cs[0])
    print(autofig.gcf().axes[0].ss)
    print(autofig.gcf().axes[0].ss[0])
    print(autofig.gcf().axes[0].calls)
    print(autofig.gcf().axes[0].calls[0])
    print(autofig.gcf().axes[0].calls[0].i)
    print(autofig.gcf().axes[0].calls[0].x)
    print(autofig.gcf().axes[0].calls[0].c)
    print(autofig.gcf().axes[0].calls[0].s)


if __name__ == '__main__':
    test_repr()
