from collections import Counter


def most_repeating_word(words: list[str]) -> str:
    def most_repeating_letter(word: str) -> int:
        return Counter(word).most_common(1)[0][1]

    return max(words, key=most_repeating_letter)


if __name__ == "__main__":
    words = ["this", "is", "an", "elementary", "test", "example"]

    print(
        f"Words: {words} -> most repeating word: {most_repeating_word(words)}"
    )
