import timeit
from array import array
import numpy


def timeit_and_print(exec_target, setup, repeat):
    t = timeit.Timer(exec_target, setup)
    elapsed_time = t.timeit(repeat)
    print(f"{exec_target}: {elapsed_time}")


def norm_square_list():
    vector = list(range(1_000_000))
    norm = 0
    for v in vector:
        norm += v * v
    return norm


def norm_square_list_comprehension():
    vector = list(range(1_000_000))
    return sum([v * v for v in vector])


def norm_square_array():
    vector = array('l', range(1_000_000))
    norm = 0
    for v in vector:
        norm += v * v
    return norm


def norm_square_numpy():
    vector = numpy.arange(1_000_000)
    return numpy.sum(vector * vector)


def norm_square_numpy_dot():
    vector = numpy.arange(1_000_000)
    return numpy.dot(vector, vector)


if __name__ == '__main__':
    count = 10
    timeit_and_print(
        "norm_square_list()",
        "from __main__ import norm_square_list",
        count
    )
    timeit_and_print(
        "norm_square_list_comprehension()",
        "from __main__ import norm_square_list_comprehension",
        count
    )
    timeit_and_print(
        "norm_square_array()",
        "from __main__ import norm_square_array",
        count
    )
    timeit_and_print(
        "norm_square_numpy()",
        "from __main__ import norm_square_numpy",
        count
    )
    timeit_and_print(
        "norm_square_numpy_dot()",
        "from __main__ import norm_square_numpy_dot",
        count
    )

