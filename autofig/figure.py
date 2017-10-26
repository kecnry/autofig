import numpy as np
import astropy.units as u
from . import common

class Figure(object):
    def __init__(self, axs=[]):
        self._axs = []

    @property
    def axs(self):
        return self._axs
