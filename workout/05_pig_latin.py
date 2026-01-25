import string


def pig_latin(word: str) -> str:
    punct = word[-1] if word[-1] in string.punctuation else ""
    if punct:
        word = word[:-1]

    if word.lower()[0] in "aiueo":
        return word + "way" + punct

    return word[1:] + word[0] + "ay" + punct


if __name__ == "__main__":
    word = "python"

    print(f"Word: {word} -> pig latin: {pig_latin(word)}")

    word = "hello!"

    print(f"Word: {word} -> pig latin: {pig_latin(word)}")
