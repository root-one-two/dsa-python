"""Array & Dynamic Array — Essential Problem Solutions."""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """Return indices of two numbers that add up to target. O(n) time."""
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def max_profit(prices: List[int]) -> int:
    """Best Time to Buy and Sell Stock — single-pass greedy. O(n) time."""
    min_price = float("inf")
    best = 0
    for price in prices:
        min_price = min(min_price, price)
        best = max(best, price - min_price)
    return best


def max_subarray(nums: List[int]) -> int:
    """Maximum Subarray (Kadane's Algorithm). O(n) time, O(1) space."""
    current = best = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        best = max(best, current)
    return best


def max_area(height: List[int]) -> int:
    """Container With Most Water — two pointers. O(n) time."""
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        best = max(best, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best


def trap(height: List[int]) -> int:
    """Trapping Rain Water — two pointers. O(n) time, O(1) space."""
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1
    return water


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    """Sliding Window Maximum using monotonic deque. O(n) time."""
    from collections import deque

    dq: deque[int] = deque()
    result: List[int] = []
    for i, num in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= num:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result


def subarray_product_less_than_k(nums: List[int], k: int) -> int:
    """Count subarrays with product < k. O(n) sliding window."""
    if k <= 1:
        return 0
    left = 0
    product = 1
    count = 0
    for right, num in enumerate(nums):
        product *= num
        while product >= k:
            product //= nums[left]
            left += 1
        count += right - left + 1
    return count
