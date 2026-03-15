from dataclasses import dataclass, field


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


@dataclass
class Cage:
    id: int
    animals: list[Animal] = field(default_factory=list)

    def add_animals(self, *animals: Animal):
        self.animals.extend(animals)

    def __repr__(self):
        return f"Cage {self.id}\n" + "\n".join(
            "\t" + str(animal) for animal in self.animals
        )

if __name__ == "__main__":
    wolf = Wolf("black")
    sheep = Sheep("white")
    snake = Snake("brown")
    parrot = Parrot("green")

    cage1 = Cage(1)
    cage1.add_animals(wolf, sheep)

    cage2 = Cage(2)
    cage2.add_animals(snake, parrot)

    print(cage1)
    print(cage2)
