from collections.abc import Callable
from typing import Any


def menu(**options: Callable[[], Any]) -> Any:
    while True:
        choices = "/".join(sorted(options.keys()))
        choice = input(f"Enter an option {choices}: ")
        if choice in options:
            return options[choice]()

        print(f"Invalid option: {choice}")
