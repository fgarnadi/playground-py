from typing import Iterable


def mychain(*args: Iterable) -> Iterable:
    for arg in args:
        yield from arg


if __name__ == "__main__":
    for item in mychain([1, 2], [3, 4], [5]):
        print(item)
