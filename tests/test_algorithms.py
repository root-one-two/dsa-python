"""Tests for algorithm primer implementations."""

from algorithms.sorting.solutions import merge_intervals, find_kth_largest, sort_colors, min_meeting_rooms
from algorithms.searching.solutions import binary_search, search_rotated, find_min_rotated, min_eating_speed
from algorithms.recursion_backtracking.solutions import subsets, permutations, combination_sum
from algorithms.dynamic_programming.solutions import climb_stairs, coin_change, can_partition, longest_common_subsequence
from algorithms.greedy.solutions import can_jump, jump, can_complete_circuit, erase_overlap_intervals


def test_merge_intervals():
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]


def test_find_kth_largest_sorting():
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5


def test_sort_colors():
    nums = [2, 0, 2, 1, 1, 0]
    sort_colors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]


def test_min_meeting_rooms():
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2


def test_binary_search():
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1


def test_search_rotated():
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4


def test_find_min_rotated():
    assert find_min_rotated([3, 4, 5, 1, 2]) == 1


def test_min_eating_speed():
    assert min_eating_speed([3, 6, 7, 11], 8) == 4


def test_subsets():
    assert sorted(subsets([1, 2, 3]), key=lambda x: (len(x), x)) == [
        [],
        [1],
        [2],
        [3],
        [1, 2],
        [1, 3],
        [2, 3],
        [1, 2, 3],
    ]


def test_permutations():
    result = permutations([1, 2, 3])
    assert len(result) == 6
    assert sorted(result) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]


def test_combination_sum():
    assert combination_sum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]


def test_climb_stairs():
    assert climb_stairs(5) == 8


def test_coin_change():
    assert coin_change([1, 2, 5], 11) == 3


def test_can_partition():
    assert can_partition([1, 5, 11, 5]) is True
    assert can_partition([1, 2, 3, 5]) is False


def test_longest_common_subsequence():
    assert longest_common_subsequence("abcde", "ace") == 3


def test_can_jump():
    assert can_jump([2, 3, 1, 1, 4]) is True
    assert can_jump([3, 2, 1, 0, 4]) is False


def test_jump():
    assert jump([2, 3, 1, 1, 4]) == 2


def test_can_complete_circuit():
    assert can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3


def test_erase_overlap_intervals():
    assert erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
