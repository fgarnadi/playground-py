from typing import Any, Sequence


def firstlast(seq: Sequence[Any]) -> Sequence[Any]:
    return [seq[0], seq[-1]]


if __name__ == "__main__":
    seq = [1, 2, 3, 4, 5]

    print(f"Sequence: {seq} -> first and last: {firstlast(seq)}")

    seq = "python"

    print(f"Sequence: {seq} -> first and last: {firstlast(seq)}")
