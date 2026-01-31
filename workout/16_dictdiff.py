from typing import Any


def dictdiff(a: dict, b: dict) -> dict:
    diff = {}
    for key in a.keys() | b.keys():
        if (left := a.get(key)) != (right := b.get(key)):
            diff[key] = [left, right]

    return diff


def map_of(*args: Any) -> dict:
    if len(args) % 2 != 0:
        raise ValueError("map_of requires an even number of arguments")

    it = iter(args)
    result = {}
    for k, v in zip(it, it):
        result[k] = v

    return result


if __name__ == "__main__":
    d1 = map_of("a", 1, "b", 2, "c", 3)
    d2 = map_of("a", 1, "b", 2, "c", 4)
    print(dictdiff(d1, d1))
    print(dictdiff(d1, d2))

    d3 = map_of("a", 1, "b", 2, "d", 3)
    d4 = map_of("a", 1, "b", 2, "c", 4)
    print(dictdiff(d3, d4))

    d5 = map_of("a", 1, "b", 2, "d", 4)
    print(dictdiff(d1, d5))
