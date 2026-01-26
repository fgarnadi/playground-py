import string


def pl_sentence(sentence: str) -> str:
    output = []
    for word in sentence.split():
        punct = word[-1] if word[-1] in string.punctuation else ""
        if punct:
            word = word[:-1]

        if word.lower()[0] in "aiueo":
            output.append(word + "way" + punct)
        else:
            output.append(word[1:] + word[0] + "ay" + punct)

    return " ".join(output)


if __name__ == "__main__":
    sentence = "this is a test"

    print(f"Sentence: {sentence} -> pig latin: {pl_sentence(sentence)}")