import sys
import threading
from types import TracebackType
from typing import ContextManager, Self


class Loading(ContextManager):
    """
    Context manager for displaying a loading spinner in the terminal during a process.

    Args:
        message (`str`, *optional*, defaults to `"Loading..."`): The message to display alongside the spinner.
        delay (`float`, *optional*, defaults to `0.1`): Delay in seconds between spinner updates.
    """

    def __init__(self, message: str = "Loading...", delay: float = 0.1):
        self.message: str = message
        self.delay: float = delay
        self._stop_event: threading.Event = threading.Event()
        self._thread: threading.Thread | None = None

    def _spinner(self):
        spinner = ["|", "/", "-", "\\"]
        i = 0
        while not self._stop_event.is_set():
            char = spinner[i % len(spinner)]
            sys.stdout.write(f"\r{self.message} {char}")
            sys.stdout.flush()

            i += 1
            self._stop_event.wait(self.delay)

    def __enter__(self) -> Self:
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._spinner, daemon=True)
        self._thread.start()

        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> bool | None:
        self._stop_event.set()

        if self._thread:
            self._thread.join()

        sys.stdout.write(f"\r{' ' * (len(self.message) + 5)}\r")
        sys.stdout.flush()

        if exc_type is None:
            sys.stdout.write(f"{self.message} Complete!\n")
        else:
            sys.stdout.write(f"{self.message} Failed!\n")
