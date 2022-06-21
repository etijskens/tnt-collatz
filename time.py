from re import I
from et_stopwatch import Stopwatch
import numpy as np
from tnt_collatz import stoppingTime, simd

import numba
stoppingTimeJit = numba.jit(stoppingTime)

if __name__ == "__main__":
    N = 100000
    n0 = 2 * N + 1
    print(f"range: [{n0}, {n0+N}[")
    with Stopwatch(f"stoppingTime         "):
        for n in range(n0,n0 + N):
            st = stoppingTime(n)    
        
    with Stopwatch("build stoppingTimeJit"):
        st: int = stoppingTimeJit(1)
    
    with Stopwatch(f"stoppingTimeJit      "):
        for n in range(n0,n0 + N):
            st = stoppingTimeJit(n)    
        
    n  = np.arange(n0, n0 + N)
    st = np.zeros_like(n)
    with Stopwatch(f"stoppingTimeSimd     "):
        simd.stoppingTime(n, st)    
