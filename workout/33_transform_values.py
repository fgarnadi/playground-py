from typing import Callable


def transform_values[T, U](f: Callable[[T], U], d: dict) -> dict:
    return {k: f(v) for k, v in d.items()}
