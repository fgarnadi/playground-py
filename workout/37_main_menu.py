from menu import menu

if __name__ == "__main__":
    res = menu(a=lambda: "A", b=lambda: 123, c=lambda: 3.14)

    print(f"Result: {res}")
