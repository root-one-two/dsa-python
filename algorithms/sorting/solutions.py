"""Sorting Algorithms — Essential Problem Solutions."""

from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """Stable divide-and-conquer sort. O(n log n) time, O(n) space."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    result: List[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr: List[int]) -> List[int]:
    """In-place quicksort with random pivot. O(n log n) average."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """Merge Intervals — sort by start, single-pass merge. O(n log n)."""
    intervals.sort(key=lambda x: x[0])
    merged: List[List[int]] = []
    for start, end in intervals:
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


def find_kth_largest(nums: List[int], k: int) -> int:
    """Kth Largest Element via Quickselect. O(n) average."""
    import random

    def partition(lo: int, hi: int) -> int:
        pivot_idx = random.randint(lo, hi)
        nums[pivot_idx], nums[hi] = nums[hi], nums[pivot_idx]
        pivot = nums[hi]
        store = lo
        for i in range(lo, hi):
            if nums[i] <= pivot:
                nums[store], nums[i] = nums[i], nums[store]
                store += 1
        nums[store], nums[hi] = nums[hi], nums[store]
        return store

    target = len(nums) - k
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        p = partition(lo, hi)
        if p == target:
            return nums[p]
        if p < target:
            lo = p + 1
        else:
            hi = p - 1
    return nums[lo]


def sort_colors(nums: List[int]) -> None:
    """Dutch National Flag — three-way in-place partition. O(n) time."""
    low = mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """Meeting Rooms II — sort starts/ends, two-pointer sweep. O(n log n)."""
    if not intervals:
        return 0
    starts = sorted(i[0] for i in intervals)
    ends = sorted(i[1] for i in intervals)
    rooms = max_rooms = 0
    s = e = 0
    while s < len(starts):
        if starts[s] < ends[e]:
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            s += 1
        else:
            rooms -= 1
            e += 1
    return max_rooms


def custom_sort_string(order: str, s: str) -> str:
    """Custom Sort String — frequency map + bucket ordering. O(n + k)."""
    from collections import Counter

    count = Counter(s)
    result: List[str] = []
    for ch in order:
        result.append(ch * count.pop(ch, 0))
    for ch, freq in count.items():
        result.append(ch * freq)
    return "".join(result)
