from collections import defaultdict


def wordcount(path: str):
    result = defaultdict(int)
    unique = set()
    with open(path, "r") as f:
        for line in f:
            result["lines"] += 1
            result["characters"] += len(line)
            word = line.split()
            result["words"] += len(word)
            unique.update(word)

    result["uniques"] = len(unique)
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    wordcount("files/wcfile.txt")
