"""
Unit and regression test for the fommscool package.
"""

# Import package, test suite, and other packages as needed
import fommscool
import pytest
import sys

def test_fommscool_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "fommscool" in sys.modules
