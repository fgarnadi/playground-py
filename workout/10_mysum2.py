from typing import Any


def mysum(first: Any, *rest: Any) -> Any:
    output = first
    for item in rest:
        output += item

    return output


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]

    print(f"nums: {nums}")
    print(f"mysum: {mysum(*nums)}")
    print()

    words = ["the", "quick", "brown", "fox"]
    print(f"words: {words}")
    print(f"mysum: {mysum(*words)}")
    print()

    seq = [[1, 2, 3], [4, 5, 6]]
    print(f"seq: {seq}")
    print(f"mysum: {mysum(*seq)}")
    print()
