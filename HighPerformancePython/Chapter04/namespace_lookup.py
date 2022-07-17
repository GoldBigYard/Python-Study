import math
from math import sin
import dis
import timeit


def test1(x):
    print("test1")
    res = 1
    for _ in range(1000):
        res += math.sin(x)
    return res


def test2(x):
    res = 1
    for _ in range(1000):
        res += sin(x)
    return res


def test3(x, sin=math.sin):
    res = 1
    for _ in range(1000):
        res += sin(x)
    return res


def test4(x):
    res = 1
    sin = math.sin
    for _ in range(1000):
        res += sin(x)
    return res


if __name__ == '__main__':
    print("1"*40)
    dis.dis(test1)
    print("2"*40)
    dis.dis(test2)
    print("3"*40)
    dis.dis(test3)
    print("4"*40)
    dis.dis(test4)

    test_time1 = timeit.repeat(
        "test1(23_456)",
        setup="from __main__ import test1",
        repeat=5,
    )
    test_time2 = timeit.repeat(
        "test2(23_456)",
        setup="from __main__ import test2",
        repeat=5,
    )
    test_time3 = timeit.repeat(
        "test3(23_456)",
        setup="from __main__ import test3",
        repeat=5,
    )
    test_time4 = timeit.repeat(
        "test4(23_456)",
        setup="from __main__ import test4",
        repeat=5,
    )

    print(f"test_time1 = {test_time1}")
    print(f"test_time2 = {test_time2}")
    print(f"test_time3 = {test_time3}")
    print(f"test_time4 = {test_time4}")
