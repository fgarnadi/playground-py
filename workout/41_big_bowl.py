from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class Scoop:
    flavor: str


@dataclass
class Bowl:
    max_scoops: ClassVar[int] = 3
    scoops: list[Scoop] = field(default_factory=list)

    def add_scoops(self, *scoops: Scoop):
        for scoop in scoops:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(scoop)

    def __repr__(self):
        return "\n".join(s.flavor for s in self.scoops)


class BigBowl(Bowl):
    max_scoops: ClassVar[int] = 5


if __name__ == "__main__":
    s1 = Scoop("chocolate")
    s2 = Scoop("vanilla")
    s3 = Scoop("persimmon")
    s4 = Scoop("strawberry")
    s5 = Scoop("mint")

    bb = BigBowl()
    bb.add_scoops(s1, s2)
    bb.add_scoops(s3)
    bb.add_scoops(s4, s5)
    print(bb)
