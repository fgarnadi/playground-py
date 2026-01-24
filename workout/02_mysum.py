def mysum(*numbers: int) -> int:
    total = 0
    for num in numbers:
        total += num

    return total


def mymean(*numbers: int) -> int:
    total = mysum(*numbers)

    return total // len(numbers)


def mystats(*words: str) -> tuple[int, int, int]:
    lengths = []
    _max = -1
    _min = 10**100
    for word in words:
        length = len(word)
        lengths.append(length)

        if length >= _max:
            _max = length
        if length <= _min:
            _min = length

    return _min, _max, mymean(*lengths)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]

    print(f"nums: {nums}")
    print(f"mysum: {mysum(*nums)}")
    print(f"mymean: {mymean(*nums)}")

    words = ["the", "quick", "brown", "fox"]
    print(f"words: {words}")
    print(f"mystats: {mystats(*words)}")
