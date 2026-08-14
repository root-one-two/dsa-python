"""Hash Tables — Chaining Hash Map & Essential Patterns."""

from typing import Any, List, Optional


class HashMap:
    """Hash map with chaining collision resolution. Average O(1) operations."""

    def __init__(self, capacity: int = 16) -> None:
        self._capacity = capacity
        self._buckets: List[List[tuple[Any, Any]]] = [[] for _ in range(capacity)]
        self._size = 0

    def _hash(self, key: Any) -> int:
        return hash(key) % self._capacity

    def put(self, key: Any, value: Any) -> None:
        idx = self._hash(key)
        for i, (k, _) in enumerate(self._buckets[idx]):
            if k == key:
                self._buckets[idx][i] = (key, value)
                return
        self._buckets[idx].append((key, value))
        self._size += 1

    def get(self, key: Any) -> Optional[Any]:
        idx = self._hash(key)
        for k, v in self._buckets[idx]:
            if k == key:
                return v
        return None

    def remove(self, key: Any) -> bool:
        idx = self._hash(key)
        for i, (k, _) in enumerate(self._buckets[idx]):
            if k == key:
                self._buckets[idx].pop(i)
                self._size -= 1
                return True
        return False

    def __len__(self) -> int:
        return self._size


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """Group strings by sorted character signature. O(n * k log k)."""
    from collections import defaultdict

    groups: dict[str, List[str]] = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        groups[key].append(s)
    return list(groups.values())


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """Top K frequent elements using hash map + bucket sort. O(n) average."""
    from collections import Counter

    count = Counter(nums)
    buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        buckets[freq].append(num)
    result: List[int] = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
    return result


def contains_duplicate(nums: List[int]) -> bool:
    """Duplicate detection using a hash set. O(n) time."""
    seen: set[int] = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
