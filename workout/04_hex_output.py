def hex_output():
    hex = input("Enter a hex number to convert: ")

    decimal = 0
    for power, digit in enumerate(reversed(hex)):
        decimal += int(digit, 16) * 16**power

    print(f"Hex: {hex} -> Decimal: {decimal}")


if __name__ == "__main__":
    hex_output()
