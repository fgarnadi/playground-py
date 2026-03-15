from freedonia import calculate_tax

if __name__ == "__main__":
    price = 500
    print(f"Chico : {calculate_tax(price, 'Chico', 12)}")
    print(f"Groucho : {calculate_tax(price, 'Groucho', 6)}")
    print(f"Harpo : {calculate_tax(price, 'Harpo', 18)}")
    print(f"Zeppo : {calculate_tax(price, 'Zeppo', 24)}")
