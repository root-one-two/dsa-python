"""Trees & Binary Search Trees — Core Implementations."""

from collections import deque
from typing import Deque, List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    """Binary Search Tree with O(log n) average search/insert/delete."""

    def __init__(self) -> None:
        self.root: Optional[TreeNode] = None

    def insert(self, val: int) -> None:
        self.root = self._insert(self.root, val)

    def _insert(self, node: Optional[TreeNode], val: int) -> TreeNode:
        if not node:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        return node

    def search(self, val: int) -> bool:
        return self._search(self.root, val)

    def _search(self, node: Optional[TreeNode], val: int) -> bool:
        if not node:
            return False
        if val == node.val:
            return True
        return self._search(node.left if val < node.val else node.right, val)

    def delete(self, val: int) -> None:
        self.root = self._delete(self.root, val)

    def _delete(self, node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not node:
            return None
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            successor = node.right
            while successor.left:
                successor = successor.left
            node.val = successor.val
            node.right = self._delete(node.right, successor.val)
        return node


def inorder(root: Optional[TreeNode]) -> List[int]:
    """In-order traversal yields sorted order for BST. O(n) time."""
    result: List[int] = []

    def dfs(node: Optional[TreeNode]) -> None:
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)

    dfs(root)
    return result


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """BFS level-order traversal. O(n) time."""
    if not root:
        return []
    result: List[List[int]] = []
    queue: Deque[TreeNode] = deque([root])
    while queue:
        level: List[int] = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


def max_depth(root: Optional[TreeNode]) -> int:
    """Maximum depth of a binary tree. O(n) time."""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """Validate BST ordering constraint. O(n) time."""
    def dfs(node: Optional[TreeNode], low: float, high: float) -> bool:
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

    return dfs(root, float("-inf"), float("inf"))
