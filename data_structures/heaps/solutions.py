"""Heaps & Priority Queues — Min-Heap Implementation."""

from typing import List


class MinHeap:
    """Binary min-heap backed by a flat array. O(log n) insert/extract."""

    def __init__(self) -> None:
        self._heap: List[int] = []

    def push(self, val: int) -> None:
        self._heap.append(val)
        self._sift_up(len(self._heap) - 1)

    def pop(self) -> int:
        if not self._heap:
            raise IndexError("pop from empty heap")
        self._swap(0, len(self._heap) - 1)
        val = self._heap.pop()
        if self._heap:
            self._sift_down(0)
        return val

    def peek(self) -> int:
        return self._heap[0]

    def __len__(self) -> int:
        return len(self._heap)

    def _sift_up(self, idx: int) -> None:
        while idx > 0:
            parent = (idx - 1) // 2
            if self._heap[idx] >= self._heap[parent]:
                break
            self._swap(idx, parent)
            idx = parent

    def _sift_down(self, idx: int) -> None:
        n = len(self._heap)
        while True:
            smallest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2
            if left < n and self._heap[left] < self._heap[smallest]:
                smallest = left
            if right < n and self._heap[right] < self._heap[smallest]:
                smallest = right
            if smallest == idx:
                break
            self._swap(idx, smallest)
            idx = smallest

    def _swap(self, i: int, j: int) -> None:
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]


def find_kth_largest(nums: List[int], k: int) -> int:
    """Find K-th largest element using a min-heap of size k. O(n log k)."""
    import heapq

    heap: List[int] = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    """Merge K sorted lists using a priority queue. O(N log k) time."""
    import heapq

    heap: List[tuple[int, int, int]] = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    result: List[int] = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        if elem_idx + 1 < len(lists[list_idx]):
            heapq.heappush(heap, (lists[list_idx][elem_idx + 1], list_idx, elem_idx + 1))
    return result
