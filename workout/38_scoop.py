from dataclasses import dataclass


@dataclass
class Scoop:
    flavor: str


def create_scoops():
    scoops = [
        Scoop("chocolate"),
        Scoop("vanilla"),
        Scoop("persimmon"),
    ]

    for scoop in scoops:
        print(scoop.flavor)
