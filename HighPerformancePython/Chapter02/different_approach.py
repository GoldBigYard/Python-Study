import dis


def fn_expressive(upper=1_000_000):
    total = 0
    for n in range(upper):
        total += n
    return total


def fn_terse(upper=1_000_000):
    return sum(range(upper))


if __name__ == "__main__":
    dis.dis(fn_terse)
    print("===========================")
    dis.dis(fn_expressive)
