# -*- coding: utf-8 -*-

"""Tests for tnt_collatz package."""

import sys
sys.path.insert(0,'.')

import tnt_collatz


def test_stoppingTime():
    """Test for tnt_collatz.stoppingTime()."""
    n = list(range(1,11))
    n_expected = [ 0, 1, 7, 2, 5, 8, 16, 3, 19, 6 ]
    for i in range(10):
        assert tnt_collatz.stoppingTime(n[i]) == n_expected[i]

    

# ==============================================================================
# The code below is for debugging a particular test in eclipse/pydev.
# (otherwise all tests are normally run with pytest)
# Make sure that you run this code with the project directory as CWD, and
# that the source directory is on the path
# ==============================================================================
if __name__ == "__main__":
    the_test_you_want_to_debug = test_stoppingTime

    print("__main__ running", the_test_you_want_to_debug)
    the_test_you_want_to_debug()
    print('-*# finished #*-')

# eof