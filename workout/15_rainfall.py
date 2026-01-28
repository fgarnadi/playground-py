import operator as op
from collections import defaultdict


def get_rainfall():
    records: dict[str, int] = defaultdict(int)
    while True:
        city = input("Enter city name: ").strip()
        if not city:
            break

        rain = input("Enter mm rain: ").strip()
        try:
            mm_rain = int(rain)
        except ValueError:
            print("You didn't enter a valid integer; try again.")
            continue

        records[city] += mm_rain

    for city, rain in sorted(records.items(), key=op.itemgetter(0)):
        print(f"{city}: {rain}")


if __name__ == "__main__":
    get_rainfall()
