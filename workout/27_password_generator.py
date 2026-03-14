import random
from typing import Callable


def create_password_generator(chars: str) -> Callable[[int], str]:
    def create_password(length: int) -> str:
        return "".join(random.choice(chars) for _ in range(length))

    return create_password


if __name__ == "__main__":
    alpha_generator = create_password_generator("abcdefghijklmnopqrstuvwxyz")
    print(f"Alpha password: {alpha_generator(10)}")
    symbol_generator = create_password_generator("!@#$%^&*()")
    print(f"Symbol password: {symbol_generator(10)}")
