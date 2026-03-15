from typing import Iterable, Iterator, Sequence


class CircleIterator(Iterator):
    def __init__(self, data: Sequence, count: int):
        self.data = data
        self.length = len(data)
        self.count = count
        self.index = 0

    def __next__(self):
        if self.count >= self.count:
            raise StopIteration

        value = self.data[self.index % self.length]

        self.index += 1

        return value


class Circle(Iterable):
    def __init__(self, data: Sequence, count: int):
        self.data = data
        self.count = count

    def __iter__(self):
        return CircleIterator(self.data, self.count)


if __name__ == "__main__":
    c = Circle("abc", 10)
    print(list(c))
