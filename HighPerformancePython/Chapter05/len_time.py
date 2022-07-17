import timeit

SIZE = 1000
a = [i for i in range(SIZE)]
b = (i for i in range(SIZE))


def len_by_list():
    global a
    return len(a)


def len_by_gen():
    # print(f"a:{type((1 for i in range(SIZE)))}")
    result = sum((1 for i in range(SIZE)))
    # print(f"len_by_gen: {result}")
    return result


if __name__ == '__main__':
    NUMBER = 1_000
    test_time1 = timeit.repeat(
        "len_by_list()",
        setup="from __main__ import len_by_list",
        repeat=5,
        number=NUMBER,
    )
    test_time2 = timeit.repeat(
        "len_by_gen()",
        setup="from __main__ import len_by_gen",
        repeat=5,
        number=NUMBER,
    )
    print(f"{test_time1}")
    print(f"{test_time2}")
