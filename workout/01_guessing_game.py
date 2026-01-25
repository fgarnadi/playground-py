from random import randint


def guessing_game() -> None:
    answer = randint(0, 100)
    chances = 3
    while chances > 0:
        raw = input("What is your guess? ")
        try:
            guess = int(raw)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if guess == answer:
            print(f"Right! The answer is {guess}")
            return

        if guess > answer:
            print(f"Your guess of {guess} is too high!")
        else:
            print(f"Your guess of {guess} is too low!")

        chances -= 1

    print(f"You're out of chance! The answer is {answer}.")


if __name__ == "__main__":
    guessing_game()
