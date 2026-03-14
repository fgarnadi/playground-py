import string
from collections import defaultdict
from functools import lru_cache

DICTIONARY = "/usr/share/dict/words"


@lru_cache
def get_dict() -> dict[int, list[str]]:
    dictionary = defaultdict(list)
    with open(DICTIONARY) as f:
        for word in f:
            dictionary[gematria_for(word.strip())].append(word.strip())

    return dictionary


def gematria_dict():
    return {char: idx for idx, char in enumerate(string.ascii_lowercase, 1)}


def gematria_for(word: str) -> int:
    d = gematria_dict()
    return sum(d.get(char, 0) for char in word)


def gematria_equal_words(word: str) -> list[str]:
    return get_dict().get(gematria_for(word), [])


if __name__ == "__main__":
    print(gematria_equal_words("cat"))
