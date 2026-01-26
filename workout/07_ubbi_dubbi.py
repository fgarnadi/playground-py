def ubbi_dubbi(word: str):
    output = []
    for letter in word:
        if letter.lower() in "aiueo":
            output.append("ub" + letter)
        else:
            output.append(letter)

    return "".join(output)


if __name__ == "__main__":
    word = "octopus"

    print(f"Word: {word} -> ubbi dubbi: {ubbi_dubbi(word)}")
