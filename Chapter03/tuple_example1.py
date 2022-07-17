import time
import random

if __name__ == '__main__':
    size_of_array = 100000
    a = [random.randint(1, 100) for i in range(size_of_array)]

    b = tuple(random.randint(1, 100) for i in range(size_of_array))

    t1 = time.time()
    a.append(0)
    t2 = time.time()
    print(f"list append: {t2 - t1} seconds")

    t1 = time.time()
    b = b + (0,)
    t2 = time.time()
    print(f"tuple append: {t2 - t1} seconds")
