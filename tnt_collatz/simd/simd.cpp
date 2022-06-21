/*
 *  C++ source file for module tnt_collatz.simd
 */


// See http://people.duke.edu/~ccc14/cspy/18G_C++_Pythost_pybind11.html for examples on how to use pybind11.
// The example below is modified after http://people.duke.edu/~ccc14/cspy/18G_C++_Pythost_pybind11.html#More-on-working-with-numpy-arrays
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

#include "my_array_t.hpp"

// caveat: this algorithm only tests for n=1 after the iteration. 
// As a consequence, the stopping time for n=1 is mistakenly reported as 3. 
void
stoppingTime
  ( py::array_t<int64_t> n_ // numpy array with the input values, updated by the algorithm until all are 1
  , py::array_t<int64_t> st_ // numpy array with the iteration count. initially all 0
  )
{
    my::array_t<int64_t,1> n__(n_);   // my::array is a wrapper for py::array_t that 
    my::array_t<int64_t,1> st__(st_); // provides easy read/write access to the raw data Of
                                      // the numpy arrays through a data() member function
    int const length = n__.shape(0);  // the length of the array
    int64_t* ptr_n = n__.data();      // pointer to the beginning of the array of input values
    int64_t* ptr_st = st__.data();    // pointer to the beginning of the array of input values

 // define work arrays whose length corresponds to a vector register (4 64-bit words)
    int const N = 4;
    assert( N <= length && "Expecting at least N input values" ); 
    int64_t xv[N], stv[N];
    int     jv[N]; 
 // initialize them with the first N items in the input array n_
    int j = 0;
    for( ; j < N; ++j ) {
        xv[j] = ptr_n[j]; // copy an element from the ptr_n array to the work array
        stv[j] = 0;       // reset the iteration counter 
        jv[j] = j;        // remember which element of the ptr_n array is being treated here
    }

    bool done = false;
    while( !done )
    {
        for( int i = 0; i < N; ++i ) 
        {// Perform a single collatz iteration:
            xv[i] = ( xv[i] % 2 == 0 ? xv[i] / 2 : 3 * xv[i] + 1 );
            stv[i] += 1;
         // check which elements of xv have reached 1, and replace them with the next value from the ptr_n array:
            if( xv[i] == 1 )
            {// store the result in the output array:
                ptr_st[jv[i]] = stv[i];
                //std::cout<<"2: i="<<i<<", jv[i]="<<jv[i]<<", n[jv[i]]="<<n[jv[i]]<<std::endl;
                if( j < length ) {    // not all ptr_n values have been processed so far.
                    xv[i] = ptr_n[j]; // fetch a new ptr_n value
                    stv[i] = 0;       // reset the corresponding iteration count
                    jv[i] = j;        // remember which element we are treating here
                    ++j;              // increment j,to point to the next element to be processed.
                }
                // else 
                // {// there are no values left to copy to the work array. We put a zero instead, so, the
                // // entry is no longer processed nor stored again in the output array.
                //     xv[i] = 0;
                // }
            }
        }
     // we are done if we exhausted the ptr_n array:
        done = (j == length);
    }
 // iterate the last N entries

    int st_left = N;
    for( int i=0; i<N; ++i ) {
        if( xv[i] == 1 ) 
            st_left -= 1;
        // std::cout<<"end0: ptr_n="<<xv[i]<<" j="<<jv[i]<<std::endl;
    }
    while (st_left > 0) 
    {
        for( int i=0; i<N; ++i )
        {
            // std::cout<<"end : "<<i<<":"<<xv[i]<<std::endl;
            if( xv[i] > 1 ) // otherwise the entry is already converged
            {// Perform a single collatz iteration:
                xv[i] = ( xv[i] % 2 == 0 ? xv[i] / 2 : 3 * xv[i] + 1 );
                stv[i] += 1;
            // test again for convergence
                if( xv[i] == 1 ) 
                {// store the result in the output array:
                    ptr_st[jv[i]] = stv[i];
                    st_left -= 1;
                }
            }
        }
    }
}


PYBIND11_MODULE(simd, m)
{// optional module doc-string
    m.doc() = "pybind11 cpp plugin"; // optional module docstring
 // list the functions you want to expose:
 // m.def("exposed_name", functiost_pointer, "doc-string for the exposed function");
    m.def("stoppingTime", &stoppingTime);
}
