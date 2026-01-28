import operator as op
from collections import namedtuple

country = namedtuple("country", ["name", "size", "population"])

COUNTRIES: list[country] = [
    country("Canada", 9984670, 38250000),
    country("Italy", 301340, 59110000),
    country("United Kingdom", 242495, 67220000),
    country("France", 551695, 67390000),
    country("Germany", 357022, 83200000),
    country("Japan", 377975, 125700000),
    country("United States", 9833517, 331900000),
]


def format_sort_records(tuples: list[country]) -> str:
    template = "{0:15} {1:10,} {2:15,}"
    output = []
    for tup in sorted(tuples, key=op.attrgetter("name")):
        output.append(template.format(*tup))

    return "\n".join(output)


if __name__ == "__main__":
    print(format_sort_records(COUNTRIES))
