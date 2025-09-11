from dataclasses import dataclass
from typing import Generic, Iterator, Optional, TypeVar

K = TypeVar("K")
V = TypeVar("V")


@dataclass
class Node(Generic[K, V]):
    """
    Node in a doubly-linked list for LinkedMap.

    Attributes:
        key: The key associated with the node.
        value: The value stored in the node.
        next: Reference to the next node in the list.
        prev: Reference to the previous node in the list.
    """

    key: K
    value: V
    next: "Optional[Node[K, V]]" = None
    prev: "Optional[Node[K, V]]" = None


class LinkedMap(Generic[K, V]):
    """
    Dictionary-like container with linked list ordering.

    Maintains insertion order and allows moving accessed items to the end.
    Supports constant-time access, insertion, deletion, and iteration.
    """

    def __init__(self) -> None:
        self._map: dict[K, Node[K, V]] = {}
        self._head: Optional[Node[K, V]] = None
        self._tail: Optional[Node[K, V]] = None

    def __contains__(self, key: K) -> bool:
        return key in self._map

    def __len__(self) -> int:
        return len(self._map)

    def __getitem__(self, key: K) -> V:
        value = self._map[key].value
        self.move_to_end(key)

        return value

    def __setitem__(self, key: K, value: V) -> None:
        if key in self._map:
            self._map[key].value = value
            return

        node = Node(key=key, value=value)
        self._map[key] = node
        if self._tail is None:
            self._head = self._tail = node
        else:
            node.prev = self._tail
            self._tail.next = node
            self._tail = node

    def __delitem__(self, key: K) -> None:
        node = self._map.pop(key)

        if node.prev:
            node.prev.next = node.next
        else:
            self._head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self._tail = node.prev

        node.prev = node.next = None

    def __iter__(self) -> Iterator[K]:
        cur = self._head
        while cur:
            yield cur.key
            cur = cur.next

    def items(self) -> Iterator[tuple[K, V]]:
        cur = self._head
        while cur:
            yield (cur.key, cur.value)
            cur = cur.next

    def keys(self) -> Iterator[K]:
        return iter(self)

    def values(self) -> Iterator[V]:
        for k in self:
            yield self._map[k].value

    def move_to_end(self, key: K) -> None:
        node = self._map[key]
        if node is self._tail:
            return

        # unlink
        if node.prev:
            node.prev.next = node.next
        else:
            self._head = node.next
        if node.next:
            node.next.prev = node.prev

        # append to tail
        node.prev = self._tail
        node.next = None
        if self._tail:
            self._tail.next = node
        self._tail = node
        if self._head is None:
            self._head = node
