"""Searching Algorithms — Essential Problem Solutions."""

from typing import List


def binary_search(nums: List[int], target: int) -> int:
    """Standard binary search. O(log n) time, O(1) space."""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def lower_bound(nums: List[int], target: int) -> int:
    """First index where nums[i] >= target."""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def search_rotated(nums: List[int], target: int) -> int:
    """Search in Rotated Sorted Array. O(log n) time."""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


def find_min_rotated(nums: List[int]) -> int:
    """Find Minimum in Rotated Sorted Array. O(log n) time."""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]


def min_eating_speed(piles: List[int], h: int) -> int:
    """Koko Eating Bananas — binary search on answer. O(n log max)."""
    def can_finish(speed: int) -> bool:
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed
        return hours <= h

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if can_finish(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def ship_within_days(weights: List[int], days: int) -> int:
    """Capacity To Ship Packages — binary search on answer."""
    def can_ship(capacity: int) -> bool:
        current = days_left = 1
        for w in weights:
            if w > capacity:
                return False
            if current + w > capacity:
                days_left += 1
                current = 0
            current += w
        return days_left <= days

    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if can_ship(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """Median of Two Sorted Arrays — binary search on partition. O(log min(m,n))."""
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    lo, hi = 0, m
    half = (m + n + 1) // 2
    while lo <= hi:
        i = lo + (hi - lo) // 2
        j = half - i
        max_left1 = float("-inf") if i == 0 else nums1[i - 1]
        min_right1 = float("inf") if i == m else nums1[i]
        max_left2 = float("-inf") if j == 0 else nums2[j - 1]
        min_right2 = float("inf") if j == n else nums2[j]
        if max_left1 <= min_right2 and max_left2 <= min_right1:
            if (m + n) % 2 == 1:
                return float(max(max_left1, max_left2))
            return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
        if max_left1 > min_right2:
            hi = i - 1
        else:
            lo = i + 1
    return 0.0
