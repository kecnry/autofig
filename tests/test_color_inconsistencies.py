import autofig
from nose.tools import assert_raises

def test_unit_inconsistencies():
    autofig.reset()
    autofig.plot(x=[1,2,3], y=[1,2,3], c=[1,2,3], cunit='solRad')
    autofig.plot(x=[1,2,3], y=[1,2,3], c=[1,2,3], cunit='m')
    assert(len(autofig.gcf().axes[0].cs)==1)

    autofig.reset()
    autofig.plot(x=[1,2,3], y=[1,2,3], c=[1,2,3], cunit='solRad')
    autofig.plot(x=[1,2,3], y=[1,2,3], c=[1,2,3], cunit='kg')
    assert(len(autofig.gcf().axes[0].cs)==2)

    autofig.reset()
    autofig.plot(x=[1,2,3], y=[1,2,3], c=[1,2,3])
    autofig.plot(x=[1,2,3], y=[1,2,3], c=[1,2,3], cunit='kg')
    assert(len(autofig.gcf().axes[0].cs)==2)

    autofig.reset()
    autofig.plot(x=[1,2,3], y=[1,2,3], c=[1,2,3], cunit='solRad')
    autofig.plot(x=[1,2,3], y=[1,2,3], c=[1,2,3])
    assert(len(autofig.gcf().axes[0].cs)==2)

def test_label_inconsistencies():
    autofig.reset()
    autofig.plot(x=[1,2,3], y=[1,2,3], c=[1,2,3], clabel='blah')
    autofig.plot(x=[1,2,3], y=[1,2,3], c=[1,2,3])
    # None shouldn't cause conflict when second
    assert(len(autofig.gcf().axes[0].cs)==1)

    autofig.reset()
    autofig.plot(x=[1,2,3], y=[1,2,3], c=[1,2,3])
    autofig.plot(x=[1,2,3], y=[1,2,3], c=[1,2,3], clabel='blah')
    # None shouldn't cause conflict when first
    assert(len(autofig.gcf().axes[0].cs)==1)

    autofig.reset()
    autofig.plot(x=[1,2,3], y=[1,2,3], c=[1,2,3], clabel='blah')
    autofig.plot(x=[1,2,3], y=[1,2,3], c=[1,2,3], clabel='OTHER')
    assert(len(autofig.gcf().axes[0].cs)==2)

def test_cmap_inconsistencies():

    autofig.reset()
    autofig.plot(x=[1,2,3], y=[1,2,3], c=[1,2,3])
    autofig.plot(x=[1,2,3], y=[1,2,3], c=[1,2,3])
    assert(len(autofig.gcf().axes[0].cs)==1)

    # TODO: not sure whether I think this should cause an inconsistency or not...
    autofig.reset()
    autofig.plot(x=[1,2,3], y=[1,2,3], c=[1,2,3], cmap='brg')
    autofig.plot(x=[1,2,3], y=[1,2,3], c=[1,2,3])
    assert(len(autofig.gcf().axes[0].cs)==1)


    autofig.reset()
    autofig.plot(x=[1,2,3], y=[1,2,3], c=[1,2,3])
    autofig.plot(x=[1,2,3], y=[1,2,3], c=[1,2,3], cmap='brg')
    assert(len(autofig.gcf().axes[0].cs)==2)


if __name__ == '__main__':
    test_unit_inconsistencies()
    test_label_inconsistencies()
    test_cmap_inconsistencies()
