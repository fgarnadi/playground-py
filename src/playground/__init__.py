from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("playground")
except PackageNotFoundError:
    __version__ = "unknown"

from playground.collections import LinkedMap
from playground.loading import AsyncLoading, Loading

__all__ = [
    "LinkedMap",
    "Loading",
    "AsyncLoading",
]
