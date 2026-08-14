"""Greedy Algorithms — Essential Problem Solutions."""

from typing import List


def can_jump(nums: List[int]) -> bool:
    """Jump Game I — furthest reachable index tracking. O(n) time."""
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)
    return True


def jump(nums: List[int]) -> int:
    """Jump Game II — minimum jumps to reach end. O(n) time."""
    jumps = 0
    current_end = farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    """Gas Station — running deficit & reset sweep. O(n) time."""
    if sum(gas) < sum(cost):
        return -1
    tank = start = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    return start


def least_interval(tasks: List[str], n: int) -> int:
    """Task Scheduler — frequency bottleneck math. O(n) time."""
    from collections import Counter

    count = Counter(tasks)
    max_freq = max(count.values())
    max_count = sum(1 for v in count.values() if v == max_freq)
    part_count = max_freq - 1
    part_length = n + 1
    empty_slots = part_count * part_length
    available = len(tasks) - max_freq * max_count
    idle = max(0, empty_slots - available)
    return len(tasks) + idle


def candy(ratings: List[int]) -> int:
    """Candy — two-way pass (left-to-right & right-to-left). O(n) time."""
    n = len(ratings)
    candies = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    return sum(candies)


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    """Non-overlapping Intervals — earliest deadline first. O(n log n)."""
    intervals.sort(key=lambda x: x[1])
    count = 0
    prev_end = float("-inf")
    for start, end in intervals:
        if start >= prev_end:
            prev_end = end
        else:
            count += 1
    return count
