"""Tests for data structure primer implementations."""

from data_structures.arrays.solutions import (
    two_sum,
    max_profit,
    max_subarray,
    max_area,
    trap,
    subarray_product_less_than_k,
)
from data_structures.linked_lists.solutions import ListNode, reverse_list, merge_two_lists
from data_structures.stacks_queues.solutions import is_valid_parentheses, MinStack
from data_structures.trees.solutions import TreeNode, max_depth, is_valid_bst
from data_structures.graphs.solutions import num_islands, can_finish
from data_structures.heaps.solutions import find_kth_largest
from data_structures.hash_tables.solutions import group_anagrams, contains_duplicate
from data_structures.tries.solutions import Trie, replace_words
from data_structures.union_find.solutions import (
    UnionFind,
    find_circle_num,
    valid_tree,
    equations_possible,
)


def _list_to_nodes(values):
    head = None
    for val in reversed(values):
        head = ListNode(val, head)
    return head


def _nodes_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def test_two_sum():
    assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]


def test_max_profit():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5


def test_max_subarray():
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_max_area():
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_trap():
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


def test_subarray_product_less_than_k():
    assert subarray_product_less_than_k([10, 5, 2, 6], 100) == 8


def test_reverse_list():
    head = _list_to_nodes([1, 2, 3])
    assert _nodes_to_list(reverse_list(head)) == [3, 2, 1]


def test_merge_two_lists():
    l1 = _list_to_nodes([1, 2, 4])
    l2 = _list_to_nodes([1, 3, 4])
    assert _nodes_to_list(merge_two_lists(l1, l2)) == [1, 1, 2, 3, 4, 4]


def test_valid_parentheses():
    assert is_valid_parentheses("()[]{}") is True
    assert is_valid_parentheses("(]") is False


def test_min_stack():
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    assert stack.get_min() == -3
    stack.pop()
    assert stack.top() == 0
    assert stack.get_min() == -2


def test_max_depth():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(root) == 3


def test_is_valid_bst():
    valid = TreeNode(2, TreeNode(1), TreeNode(3))
    invalid = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), None))
    assert is_valid_bst(valid) is True
    assert is_valid_bst(invalid) is False


def test_num_islands():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert num_islands(grid) == 3


def test_can_finish():
    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False


def test_find_kth_largest():
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5


def test_group_anagrams():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    normalized = sorted([sorted(g) for g in result])
    assert normalized == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]


def test_contains_duplicate():
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False


def test_trie_insert_search_prefix():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.starts_with("app") is True
    trie.insert("app")
    assert trie.search("app") is True


def test_replace_words():
    assert replace_words(["cat", "bat", "rat"], "the cattle was rattled by the battery") == (
        "the cat was rat by the bat"
    )


def test_union_find_connected():
    uf = UnionFind(4)
    assert uf.union(0, 1) is True
    assert uf.union(2, 3) is True
    assert uf.connected(0, 1) is True
    assert uf.connected(0, 2) is False
    assert uf.union(1, 2) is True
    assert uf.connected(0, 3) is True
    assert uf.union(0, 3) is False


def test_find_circle_num():
    assert find_circle_num([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2


def test_valid_tree():
    assert valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) is True
    assert valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) is False


def test_equations_possible():
    assert equations_possible(["a==b", "b!=a"]) is False
    assert equations_possible(["b==a", "a==b"]) is True
