"""
Testing the integrate package
"""

import fommscool
import pytest
import sys
import numpy as np

def test_fommscool_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "fommscool" in sys.modules

def g(x):
    return 3.0 * x

def f(x):
    return np.power(x, 2)

def h(x):
    return np.ones(x.size)

def volume(x):
    squares = np.power(x, 2)
    return np.sum(squares, axis=1)

def test_trapz():
    x = np.array([0, 10])
    I = fommscool.newton_cotes.trapz(x, g)
    assert I == 150.00

def test_monte1d():
    x = np.array([0, 3])
    I = fommscool.stochastic.monte_1d(x, f, 100000)
    assert np.allclose(I, 9.00, 1e-2)
