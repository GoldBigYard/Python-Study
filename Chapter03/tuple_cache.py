import dis


def func_for_dis():
    a = [1, 2, 3, 4]
    print(f"{a[1]}")

    b = (1, 2, 3, 4)
    print(f"{b[1]}")

    c = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22)
    print(f"{c[20]}")


if __name__ == '__main__':
    dis.dis(func_for_dis)
