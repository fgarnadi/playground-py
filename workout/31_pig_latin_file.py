import string


def pl_word(word: str) -> str:
    punct = word[-1] if word[-1] in string.punctuation else ""
    if punct:
        word = word[:-1]

    if word.lower()[0] in "aiueo":
        return word + "way" + punct

    return word[1:] + word[0] + "ay" + punct


def pl_file(file: str) -> str:
    return " ".join(
        pl_word(word) for line in open(file) for word in line.split()
    )
