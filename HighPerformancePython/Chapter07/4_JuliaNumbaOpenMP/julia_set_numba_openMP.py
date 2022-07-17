from numba import jit, prange
import time
import numpy as np


x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193


def timefn(fn):
    # @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f"@timefn: {fn.__name__} took {t2 - t1} seconds")
        return result
    return measure_time


@timefn
def calc_pure_python(desired_width, max_iterations):
    x_step = (x2 - x1) / desired_width
    y_step = (y1 - y2) / desired_width

    x = []
    y = []
    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step
    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step

    zs = []

    cs = []
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))
    print("Length of x: ", len(x))
    print("Total elements: ", len(zs))

    output = calculate_z(max_iterations, np.array(zs), np.array(cs))

    assert sum(output) == 33219980


@jit(nopython=False, parallel=True)
def calculate_z(maxiter, zs, cs):
    output = [0] * len(zs)
    for i in prange(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while abs(z) < 2 and n < maxiter:
            z = z * z + c
            n += 1
        output[i] = n
    return output


if __name__ == "__main__":
    calc_pure_python(desired_width=1000, max_iterations=300)
    calc_pure_python(desired_width=1000, max_iterations=300)
    calc_pure_python(desired_width=1000, max_iterations=300)
    # print(calculate_z.inspect_types())
