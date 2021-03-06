import bisect
import random


def find_closest(haystack, needle):
    i = bisect.bisect_left(haystack, needle)
    if i == len(haystack):
        return i - 1
    elif haystack[i] == needle:
        return i
    elif i > 0:
        j = i - 1
        if haystack[i] - needle > needle - haystack[j]:
            return j
    return i


if __name__ == '__main__':
    important_numbers = []
    for i in range(10):
        new_number = random.randint(0, 1000)
        bisect.insort(important_numbers, new_number)

    print(important_numbers)

    closest_index = find_closest(important_numbers, -250)
    print(f"{closest_index}")

    closest_index = find_closest(important_numbers, 500)
    print(f"{closest_index}")

    closest_index = find_closest(important_numbers, 1100)
    print(f"{closest_index}")
