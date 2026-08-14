"""Recursion & Backtracking — Essential Problem Solutions."""

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    """Power Set — include/exclude decision tree. O(n * 2^n)."""
    result: List[List[int]] = []

    def backtrack(start: int, path: List[int]) -> None:
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


def permutations(nums: List[int]) -> List[List[int]]:
    """All permutations via in-place swap backtracking. O(n * n!)."""
    result: List[List[int]] = []

    def backtrack(start: int) -> None:
        if start == len(nums):
            result.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return result


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """Combination Sum — backtrack with remaining target reduction."""
    result: List[List[int]] = []
    candidates.sort()

    def backtrack(start: int, remaining: int, path: List[int]) -> None:
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            backtrack(i, remaining - candidates[i], path)
            path.pop()

    backtrack(0, target, [])
    return result


def solve_n_queens(n: int) -> List[List[str]]:
    """N-Queens — constraint propagation with diagonal tracking."""
    result: List[List[str]] = []
    cols: set[int] = set()
    pos_diag: set[int] = set()
    neg_diag: set[int] = set()
    board = ["." * n for _ in range(n)]

    def backtrack(row: int) -> None:
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                continue
            cols.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)
            board[row] = "." * col + "Q" + "." * (n - col - 1)
            backtrack(row + 1)
            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)

    backtrack(0)
    return result


def word_search(board: List[List[str]], word: str) -> bool:
    """Word Search — 2D grid DFS with in-place state rollback."""
    rows, cols = len(board), len(board[0])

    def dfs(r: int, c: int, idx: int) -> bool:
        if idx == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
            return False
        temp = board[r][c]
        board[r][c] = "#"
        found = (
            dfs(r + 1, c, idx + 1)
            or dfs(r - 1, c, idx + 1)
            or dfs(r, c + 1, idx + 1)
            or dfs(r, c - 1, idx + 1)
        )
        board[r][c] = temp
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False
