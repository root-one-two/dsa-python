"""Bit manipulation — set bits, XOR uniqueness, powers of two."""


def hamming_weight(n: int) -> int:
    """Number of 1 bits. O(number of set bits)."""
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


def single_number(nums: list[int]) -> int:
    """Every value appears twice except one. XOR cancels pairs. O(n)."""
    unique = 0
    for num in nums:
        unique ^= num
    return unique


def is_power_of_two(n: int) -> bool:
    """True iff n is a positive power of two. O(1)."""
    return n > 0 and (n & (n - 1)) == 0


def missing_number(nums: list[int]) -> int:
    """Missing value in 0..n where n = len(nums). XOR indices with values."""
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing


def reverse_bits(n: int) -> int:
    """Reverse the lowest 32 bits. O(32)."""
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
