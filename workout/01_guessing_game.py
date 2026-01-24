from random import randint


def guessing_game() -> None:
    answer = randint(0, 100)
    chance = 3
    while (guess := int(input("What is your guess? "))) and (chance > 1):
        if guess == answer:
            print(f"Right! The answer is {guess}")
            break

        if guess > answer:
            print(f"Your guess of {guess} is too high!")
        else:
            print(f"Your guess of {guess} is too low!")

        chance -= 1

    print("You're out of chance. Try again!")


if __name__ == "__main__":
    guessing_game()
