import pytest

from playground.collections import LinkedMap


def test_insert_and_iteration_order():
    m = LinkedMap[str, int]()
    m["a"] = 1
    m["b"] = 2
    m["c"] = 3

    assert len(m) == 3
    assert list(m) == ["a", "b", "c"]
    assert list(m.keys()) == ["a", "b", "c"]
    assert list(m.values()) == [1, 2, 3]
    assert list(m.items()) == [("a", 1), ("b", 2), ("c", 3)]
    assert "b" in m
    assert "x" not in m


def test_getitem_moves_to_end():
    m = LinkedMap[str, int]()
    m["a"] = 1
    m["b"] = 2
    m["c"] = 3

    assert m["b"] == 2
    assert list(m) == ["a", "c", "b"]
    assert list(m.values()) == [1, 3, 2]

    assert m["b"] == 2
    assert list(m) == ["a", "c", "b"]


def test_setitem_updates_without_moving():
    m = LinkedMap[str, int]()
    m["a"] = 1
    m["b"] = 2
    m["c"] = 3

    m["b"] = 20
    assert len(m) == 3
    assert list(m.items()) == [("a", 1), ("b", 20), ("c", 3)]


def test_delete_behavior_and_empty():
    m = LinkedMap[str, int]()
    m["a"] = 1
    m["b"] = 2
    m["c"] = 3

    del m["b"]
    assert len(m) == 2
    assert list(m) == ["a", "c"]
    assert "b" not in m

    del m["a"]
    del m["c"]
    assert len(m) == 0
    assert list(m) == []
    assert list(m.items()) == []
    assert list(m.keys()) == []
    assert list(m.values()) == []

    with pytest.raises(KeyError):
        del m["x"]


def test_move_to_end_noop_for_tail():
    m = LinkedMap[str, int]()
    m["a"] = 1
    m["b"] = 2
    m["c"] = 3

    m.move_to_end("c")
    assert list(m) == ["a", "b", "c"]


def test_move_to_end_on_head():
    m = LinkedMap[str, int]()
    m["a"] = 1
    m["b"] = 2
    m["c"] = 3

    m.move_to_end("a")
    assert list(m) == ["b", "c", "a"]


def test_move_to_end_on_middle():
    m = LinkedMap[str, int]()
    m["a"] = 1
    m["b"] = 2
    m["c"] = 3

    m.move_to_end("b")
    assert list(m) == ["a", "c", "b"]


def test_move_to_end_on_single_element():
    m = LinkedMap[str, int]()
    m["a"] = 1

    m.move_to_end("a")
    assert list(m) == ["a"]


def test_empty_linkedmap():
    m = LinkedMap()
    assert len(m) == 0
    assert list(m) == []
    assert list(m.items()) == []
    assert list(m.keys()) == []
    assert list(m.values()) == []
    assert "anykey" not in m


def test_missing_key_errors():
    m = LinkedMap()
    with pytest.raises(KeyError):
        _ = m["missing"]
    with pytest.raises(KeyError):
        m.move_to_end("missing")
