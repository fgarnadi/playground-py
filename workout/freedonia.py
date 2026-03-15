TAX_RATES = {
    "Chico": 0.5,
    "Groucho": 0.7,
    "Harpo": 0.5,
    "Zeppo": 0.4,
}


def calculate_tax(amount: int, province: str, hour: int) -> float:
    if hour < 0 or hour > 24:
        raise ValueError("Hour must be between 0 and 24")

    percentage = hour / 24
    rate = TAX_RATES.get(province, 0.0)

    return amount + (amount * rate * percentage)
