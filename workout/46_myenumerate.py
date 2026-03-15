from typing import Iterable, Iterator, Sequence


class MyEnumerateIterator(Iterator):
    def __init__(self, data: Sequence, start: int = 0):
        self.data = iter(data)
        self.index = start

    def __next__(self):
        try:
            value = (self.index, next(self.data))
            self.index += 1

            return value
        except StopIteration:
            raise


class MyEnumerate(Iterable):
    def __init__(self, data: Sequence, start: int = 0):
        self.data = data
        self.start = start

    def __iter__(self):
        return MyEnumerateIterator(self.data, self.start)


if __name__ == "__main__":
    for idx, letter in MyEnumerate("abc"):
        print(idx, letter)
