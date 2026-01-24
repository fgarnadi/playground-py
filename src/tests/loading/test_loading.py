import asyncio
import io
import time

import pytest

from playground.loading import AsyncLoading, Loading


def test_loading_success(monkeypatch):
    buf = io.StringIO()
    monkeypatch.setattr("sys.stdout", buf)

    with Loading("Test", delay=0.001):
        time.sleep(0.02)

    out = buf.getvalue()
    assert "Test Complete!" in out


def test_loading_failure(monkeypatch):
    buf = io.StringIO()
    monkeypatch.setattr("sys.stdout", buf)

    with pytest.raises(RuntimeError):
        with Loading("ErrTest", delay=0.001):
            raise RuntimeError("boom")

    out = buf.getvalue()
    assert "ErrTest Failed!" in out


def test_async_loading_success(monkeypatch):
    buf = io.StringIO()
    monkeypatch.setattr("sys.stdout", buf)

    async def run():
        async with AsyncLoading("AAsync", delay=0.001):
            await asyncio.sleep(0.02)

    asyncio.run(run())
    out = buf.getvalue()
    assert "AAsync Complete!" in out


def test_async_loading_failure(monkeypatch):
    buf = io.StringIO()
    monkeypatch.setattr("sys.stdout", buf)

    async def run():
        async with AsyncLoading("AErr", delay=0.001):
            raise RuntimeError("boom")

    with pytest.raises(RuntimeError):
        asyncio.run(run())

    out = buf.getvalue()
    assert "AErr Failed!" in out
