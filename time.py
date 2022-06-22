from et_stopwatch import Stopwatch
import numpy as np
from tnt_collatz import stoppingTime, simd

import numba
stoppingTimeJit = numba.jit(stoppingTime)

if __name__ == "__main__":
    N = 100000
    n0 = 2 * N + 10
    print(f"range: [{n0}, {n0+N}[")

    for i in range(10):
        with Stopwatch(f"stoppingTime         ") as sw:
            for n in range(n0,n0 + N):
                st = stoppingTime(n)    
        t0 = sw.time

        if i == 0:
            with Stopwatch("build stoppingTimeJit"):
                st: int = stoppingTimeJit(1)
        
        with Stopwatch(f"stoppingTimeJit      ") as sw:
            for n in range(n0,n0 + N):
                st = stoppingTimeJit(n)    
        t1 = sw.time

        n  = np.arange(n0, n0 + N)
        st = np.zeros_like(n)
        with Stopwatch(f"stoppingTimeSimd     ") as sw:
            simd.stoppingTime(n, st)    
        t2 = sw.time

        print(t0/t1)
        print(t1/t2)
        print(t0/t2)