import sys
import threading
from concurrent.futures import Future, ThreadPoolExecutor
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
        self._executor: ThreadPoolExecutor | None = None
        self._future: Future | None = None

    def _spinner(self):
        spinner = ["|", "/", "-", "\\"]
        i = 0
        while not self._stop_event.is_set():
            current_char = spinner[i % len(spinner)]
            sys.stdout.write(f"\r{self.message} {current_char}")
            sys.stdout.flush()

            i += 1
            self._stop_event.wait(self.delay)

    def __enter__(self) -> Self:
        self._executor = ThreadPoolExecutor(max_workers=1)
        self._future = self._executor.submit(self._spinner)

        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> bool | None:
        self._stop_event.set()

        if self._future:
            self._future.result(timeout=1)
        if self._executor:
            self._executor.shutdown(wait=True)

        sys.stdout.write(f"\r{' ' * (len(self.message) + 5)}\r")
        sys.stdout.flush()

        if exc_type is None:
            sys.stdout.write(f"{self.message} Complete!\n")
        else:
            sys.stdout.write(f"{self.message} Failed!\n")
