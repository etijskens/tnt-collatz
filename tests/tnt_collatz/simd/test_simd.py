#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for C++ module tnt_collatz.simd.
"""

import sys
sys.path.insert(0,'.')

import numpy as np

import tnt_collatz.simd


def test_stoppingTime():
    """Test for tnt_collatz.stoppingTime()."""
    n  = np.array(list(range(1,11)))
    st = np.zeros_like(n)
    n_expected = np.array([ 3, 1, 7, 2, 5, 8, 16, 3, 19, 6 ])
    #   (see the caveat in simd.cpp for the initial 3 in n_expected)
    tnt_collatz.simd.stoppingTime(n, st)
    print(f'n ={n}')
    print(f'st={st}')
    assert np.all( st == n_expected )


#===============================================================================
# The code below is for debugging a particular test in eclipse/pydev.
# (normally all tests are run with pytest)
#===============================================================================
if __name__ == "__main__":
    the_test_you_want_to_debug = test_stoppingTime

    print(f"__main__ running {the_test_you_want_to_debug} ...")
    the_test_you_want_to_debug()
    print('-*# finished #*-')
#===============================================================================
