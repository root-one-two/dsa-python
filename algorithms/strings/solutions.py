"""Strings — two pointers and sliding window."""

from typing import List


def is_palindrome(s: str) -> bool:
    """Valid Palindrome — ignore non-alphanumeric, case-insensitive. O(n)."""
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


def three_sum(nums: List[int]) -> List[List[int]]:
    """3Sum — unique triplets that add to 0. O(n²) after sort."""
    nums = sorted(nums)
    result: List[List[int]] = []
    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result


def length_of_longest_substring(s: str) -> int:
    """Longest substring without repeating characters. O(n) window."""
    last: dict[str, int] = {}
    left = best = 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        best = max(best, right - left + 1)
    return best


def character_replacement(s: str, k: int) -> int:
    """Longest same-letter window after at most k replacements. O(n)."""
    count: dict[str, int] = {}
    left = best = max_freq = 0
    for right, ch in enumerate(s):
        count[ch] = count.get(ch, 0) + 1
        max_freq = max(max_freq, count[ch])
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best


def reverse_words(s: str) -> str:
    """Reverse word order and collapse extra spaces. O(n)."""
    words = s.split()
    words.reverse()
    return " ".join(words)
