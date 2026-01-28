MENU: dict[str, int] = {
    "sandwich": 10,
    "tea": 7,
}


def restaurant():
    total = 0
    while True:
        item = input("Order: ").strip()
        if not item:
            break

        if item in MENU:
            total += MENU[item]
            print(f"{item} costs {MENU[item]}, total is {total}")
        else:
            print(f"Sorry, we are fresh out of {item} today.")

    print(f"Your total is {total}")


if __name__ == "__main__":
    restaurant()
