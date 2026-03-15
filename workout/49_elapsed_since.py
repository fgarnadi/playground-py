from time import perf_counter, sleep
from typing import Iterable


def elapsed_since(data: Iterable):
    prev = None
    for item in data:
        curr = perf_counter()
        delta = curr - (prev or curr)
        prev = perf_counter()

        yield delta, item


if __name__ == "__main__":
    for t, _ in elapsed_since(range(5)):
        print(t)
        sleep(1)
