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
