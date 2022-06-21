# -*- coding: utf-8 -*-

"""
Package tnt_collatz
===================

Studying the collatz conjecture.
"""

__version__ = "0.0.0"

try:
    import tnt_collatz.simd
except ModuleNotFoundError as e:
    # Try to build this binary extension:
    from pathlib import Path
    import click
    from et_micc2.project import auto_build_binary_extension
    msg = auto_build_binary_extension(Path(__file__).parent, 'simd')
    if not msg:
        import tnt_collatz.simd
    else:
        click.secho(msg, fg='bright_red')

def stoppingTime(n: int) -> int:
    """Get the stopping time of n. 
    
    For this we perform the Collatz iteration on n until n=1.

    :param n: a strictly positive number 
    :returns: the stopping time of n
    """
    stopping_time: int = 0
    while n > 1:
        if n % 2 == 0:  # even
            n /= 2
        else:           # odd
            n = 3 * n + 1
        stopping_time += 1
        
    return stopping_time
    
        