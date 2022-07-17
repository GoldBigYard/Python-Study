# Example 7-9. Annotated numpy version of the julia calculation function
import numpy as np
cimport numpy as np

def calculate_z_serial_purepython(int maxiter, double complex[:] zs, double complex[:] cs):
    cdef unsigned int i, n
    cdef double complex z, c
    cdef int[:] output = np.empty(len(zs), dtype=np.int32)

    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while n < maxiter and (z.real * z.real + z.imag * z.imag) < 4:
            z = z * z + c
            n += 1
        output[i] = n
    return output
