This file documents a python module built from C++ code with pybind11.
You should document the Python interfaces, *NOT* the C++ interfaces.

Module tnt_collatz.simd
**************************

Module :py:mod:`simd` built from C++ code in :file:`tnt_collatz/simd/simd.cpp`.

.. function:: add(x,y,z)
   :module: tnt_collatz.simd
   
   Compute the sum of *x* and *y* and store the result in *z* (overwrite).

   :param x: 1D Numpy array with ``dtype=numpy.float64`` (input)
   :param y: 1D Numpy array with ``dtype=numpy.float64`` (input)
   :param z: 1D Numpy array with ``dtype=numpy.float64`` (output)
   