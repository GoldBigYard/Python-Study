# Example 7-10
from cython.parallel import prange
import numpy as np
cimport numpy as np

def calculate_z_serial_purepython(unsigned int maxiter, double complex[:] zs, double complex[:] cs):
    cdef unsigned int i, length
    cdef double complex z, c
    cdef int [:] output = np.empty(len(zs), dtype=np.int32)

    with nogil:
        for i in prange(length, schedule="guided"):
            z = zs[i]
            c = cs[i]
            output[i] = 0
            while output[i] < maxiter and (z.real * z.real + z.imag * z.imag) < 4:
                z = z * z + c
                output[i] += 1

    return output
