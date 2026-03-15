from dataclasses import dataclass


@dataclass
class Animal:
    color: str
    number_of_legs: int

    @property
    def species(self) -> str:
        return self.__class__.__name__

    def __repr__(self):
        return f"{self.color} {self.species}, {self.number_of_legs} legs"


@dataclass(repr=False)
class Wolf(Animal):
    number_of_legs: int = 4


@dataclass(repr=False)
class Sheep(Animal):
    number_of_legs: int = 4


@dataclass(repr=False)
class Snake(Animal):
    number_of_legs: int = 0


@dataclass(repr=False)
class Parrot(Animal):
    number_of_legs: int = 2


if __name__ == "__main__":
    wolf = Wolf("black")
    sheep = Sheep("white")
    snake = Snake("brown")
    parrot = Parrot("green")

    print(wolf)
    print(sheep)
    print(snake)
    print(parrot)
