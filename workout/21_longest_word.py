import os


def find_longest_word(path: str) -> str:
    longest = ""
    with open(path, "r") as f:
        for line in f:
            for word in line.split():
                if len(word) > len(longest):
                    longest = word

    return longest


def find_all_longest_words(path: str) -> dict:
    return {
        file: find_longest_word(filepath)
        for file in os.listdir(path)
        if os.path.isfile((filepath := os.path.join(path, file)))
    }

if __name__ == "__main__":
    findings = find_all_longest_words("files")
    for file, word in findings.items():
        print(f"{file}: {word}")