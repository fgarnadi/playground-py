def how_many_different_numbers(numbers: list[int]) -> int:
    return len(set(numbers))


if __name__ == "__main__":
    numbers = [1, 2, 3, 1, 2, 3, 4, 1]
    print(how_many_different_numbers(numbers))
