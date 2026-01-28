import operator as op

COUNTRIES = [
    {"name": "Canada", "size": 9984670, "population": 38250000},
    {"name": "Italy", "size": 301340, "population": 59110000},
    {"name": "United Kingdom", "size": 242495, "population": 67220000},
    {"name": "France", "size": 551695, "population": 67390000},
    {"name": "Germany", "size": 357022, "population": 83200000},
    {"name": "Japan", "size": 377975, "population": 125700000},
    {"name": "United States", "size": 9833517, "population": 331900000},
]


def alphabetize_countries(
    dicts: list[dict[str, object]],
) -> list[dict[str, object]]:
    return sorted(dicts, key=op.itemgetter("name"))


if __name__ == "__main__":
    from pprint import pprint

    print("Before:")
    pprint(COUNTRIES)

    print("\nAfter:")
    pprint(alphabetize_countries(COUNTRIES))
