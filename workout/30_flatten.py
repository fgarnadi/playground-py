from typing import Any


def flatten(input: list[Any] | Any) -> list[Any]:
    return [
        sub
        for item in input
        for sub in (flatten(item) if isinstance(item, list) else [item])
    ]
