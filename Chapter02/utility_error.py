import time

def test_some_fn():
    assert some_fn(2) == 4
    assert some_fn(1) == 1
    assert some_fn(-1) == 1


@profile
def some_fn(useful_input):
    time.sleep(1)
    return useful_input ** 2


if __name__ == "__main__":
    print(f"Example call `some_fn(2)` == {some_fn(2)}")
