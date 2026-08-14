"""Stack & Queue — Core Data Structure Implementations."""

from collections import deque
from typing import Deque, List, Optional


class Stack:
    """LIFO stack with O(1) push/pop/peek."""

    def __init__(self) -> None:
        self._items: List[int] = []

    def push(self, val: int) -> None:
        self._items.append(val)

    def pop(self) -> int:
        return self._items.pop()

    def peek(self) -> int:
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0


class Queue:
    """FIFO queue with O(1) enqueue/dequeue."""

    def __init__(self) -> None:
        self._items: Deque[int] = deque()

    def enqueue(self, val: int) -> None:
        self._items.append(val)

    def dequeue(self) -> int:
        return self._items.popleft()

    def is_empty(self) -> bool:
        return len(self._items) == 0


def is_valid_parentheses(s: str) -> bool:
    """Balanced parenthesis parsing using a stack. O(n) time."""
    stack: List[str] = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack


class MinStack:
    """Stack supporting O(1) push, pop, top, and getMin."""

    def __init__(self) -> None:
        self._stack: List[int] = []
        self._mins: List[int] = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if not self._mins or val <= self._mins[-1]:
            self._mins.append(val)

    def pop(self) -> None:
        if self._stack.pop() == self._mins[-1]:
            self._mins.pop()

    def top(self) -> int:
        return self._stack[-1]

    def get_min(self) -> int:
        return self._mins[-1]


class MyQueue:
    """Implement queue using two stacks. Amortized O(1) enqueue/dequeue."""

    def __init__(self) -> None:
        self._in_stack: List[int] = []
        self._out_stack: List[int] = []

    def push(self, x: int) -> None:
        self._in_stack.append(x)

    def pop(self) -> int:
        self._transfer()
        return self._out_stack.pop()

    def peek(self) -> int:
        self._transfer()
        return self._out_stack[-1]

    def empty(self) -> bool:
        return not self._in_stack and not self._out_stack

    def _transfer(self) -> None:
        if not self._out_stack:
            while self._in_stack:
                self._out_stack.append(self._in_stack.pop())
