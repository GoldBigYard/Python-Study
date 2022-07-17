import timeit
import random

unsorted_list = [random.randint(1,10000) for i in range(10_000_000)]
sorted_list = sorted(unsorted_list)

def timeit_and_print(exec_target, setup, repeat):
    t = timeit.Timer(exec_target, setup)
    elapsed_time = t.timeit(repeat)
    print(f"{exec_target}: {elapsed_time}")


def bad_branch_predict():
    sum = 0
    for num in unsorted_list:
        if num >= 5000:
            sum += num
    return sum


def good_branch_predict():
    sum = 0
    for num in sorted_list:
        if num >= 5000:
            sum += num
    return sum


if __name__ == '__main__':
    count = 20
    timeit_and_print(
        "bad_branch_predict()",
        "from __main__ import bad_branch_predict",
        count
    )
    timeit_and_print(
        "good_branch_predict()",
        "from __main__ import good_branch_predict",
        count
    )
