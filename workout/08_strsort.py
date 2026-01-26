def strsort(text: str) -> str:
    return "".join(sorted(text))


if __name__ == "__main__":
    text = "python"

    print(f"Text: {text} -> sorted: {strsort(text)}")
