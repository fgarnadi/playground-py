import importlib
import importlib.metadata
import sys


def _clear_playground_modules():
    for name in list(sys.modules):
        if name == "playground" or name.startswith("playground."):
            del sys.modules[name]


def test_version_falls_back_to_unknown(monkeypatch):
    def raise_not_found(name):
        raise importlib.metadata.PackageNotFoundError()

    monkeypatch.setattr(importlib.metadata, "version", raise_not_found)

    _clear_playground_modules()

    pkg = importlib.import_module("playground")
    assert getattr(pkg, "__version__") == "unknown"


def test_version_uses_metadata_when_present(monkeypatch):
    monkeypatch.setattr(importlib.metadata, "version", lambda name: "1.2.3")

    _clear_playground_modules()

    pkg = importlib.import_module("playground")
    assert getattr(pkg, "__version__") == "1.2.3"
