import os
from contextlib import suppress


def all_lines(path: str):
    for file in os.listdir(path):
        with suppress(OSError):
            with open(os.path.join(path, file)) as f:
                yield from f.readlines()
