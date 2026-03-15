from dataclasses import dataclass, field


@dataclass
class Scoop:
    flavor: str


@dataclass
class Bowl:
    scoops: list[Scoop] = field(default_factory=list)

    def add_scoops(self, *scoops: Scoop):
        self.scoops.extend(scoops)

    def __repr__(self):
        return "\n".join(s.flavor for s in self.scoops)


if __name__ == "__main__":
    s1 = Scoop("chocolate")
    s2 = Scoop("vanilla")
    s3 = Scoop("persimmon")

    b = Bowl()
    b.add_scoops(s1, s2)
    b.add_scoops(s3)
    print(b)
