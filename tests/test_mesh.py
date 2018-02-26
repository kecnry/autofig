import autofig
import numpy as np
from nose.tools import assert_raises

def test_mesh(show=False):
    autofig.reset()

    x = np.array([np.array([0,1,1.5])])
    y = np.array([np.array([0,0,1])])
    z = np.array([np.array([0,0,0])])

    autofig.mesh(x=x, y=y, z=z, linestyle='dashed')

    autofig.draw(show=show)

if __name__ == '__main__':
    test_mesh(show=True)
