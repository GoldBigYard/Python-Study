import random
import time

from functools import wraps


def print_time(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f"@timefn: {fn.__name__} took {t2 - t1} seconds")
        return result
    return measure_time


def linear_search(needle, array):
    for i, item in enumerate(array):
        if item == needle:
            return i
    return -1


@print_time
def binary_search(needle, haystack):
    imin, imax = 0, len(haystack)
    while True:
        if imin > imax:
            return -1
        midpoint = (imin + imax) // 2
        if haystack[midpoint] > needle:
            imax = midpoint-1
        elif haystack[midpoint] < needle:
            imin = midpoint+1
        else:
            return midpoint


@print_time
def transform_dict(needle, haystack):
    haydict = {num: idx for idx, num in enumerate(haystack)}
    if needle not in haydict:
        return -1
    return haydict[needle]




if __name__ == '__main__':
    size_of_array = 1000000000
    haystack = [random.randint(1, size_of_array) for i in range(size_of_array)]
    haystack.sort()

    binary_search(100, haystack)
    transform_dict(100, haystack)
