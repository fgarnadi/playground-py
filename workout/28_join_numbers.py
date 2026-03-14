from typing import Iterable

def join_numbers(numbers: Iterable[int]) -> str:
    return ", ".join(str(num) for num in numbers)