def add_number(input: str) -> int:
    return sum(int(num) for num in input.split() if num.isdigit())
