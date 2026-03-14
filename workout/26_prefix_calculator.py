import operator as op
from functools import reduce


def calc(expr: str) -> int:
    operations = {
        "+": op.add,
        "-": op.sub,
        "*": op.mul,
        "/": op.floordiv,
        "**": op.pow,
        "%": op.mod,
    }

    ops, numbers = expr.split(maxsplit=1)

    return reduce(operations[ops], map(int, numbers.split()))


if __name__ == "__main__":
    # simple
    print("Simple operations:")
    print(f"+ 3 2 = {calc('+ 3 2')}")
    print(f"- 3 2 = {calc('- 3 2')}")
    print(f"* 3 2 = {calc('* 3 2')}")
    print(f"/ 3 2 = {calc('/ 3 2')}")
    print(f"** 3 2 = {calc('** 3 2')}")
    print(f"% 3 2 = {calc('% 3 2')}")

    # multiple numbers
    print("\nMultiple numbers:")
    print(f"+ 3 2 1 = {calc('+ 3 2 1')}")
    print(f"- 3 2 1 = {calc('- 3 2 1')}")
