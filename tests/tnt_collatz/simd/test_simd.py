#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for C++ module tnt_collatz.simd.
"""

import sys
sys.path.insert(0,'.')

import numpy as np

import tnt_collatz.simd
import tnt_collatz 


def test_simd_stoppingTime():
    """Test for tnt_collatz.simd.stoppingTime()."""
    n = np.random.randint(2,1000,20) # 20 random integers in the range [2,1000[
    st_expected = []
    for i in n:
        st_expected.append(tnt_collatz.stoppingTime(i)) # we already tested tnt_collatz.stoppingTime
    st_expected = np.array(st_expected)
    st = np.zeros_like(n)
    tnt_collatz.simd.stoppingTime(n, st)
    print(f'n ={n}')
    print(f'st={st}')
    assert np.all( st == st_expected )


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
