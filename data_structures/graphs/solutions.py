"""Graphs — Adjacency List, BFS, and DFS Implementations."""

from collections import deque
from typing import Deque, Dict, List, Set


class Graph:
    """Undirected graph using adjacency list representation."""

    def __init__(self, n: int) -> None:
        self.adj: Dict[int, List[int]] = {i: [] for i in range(n)}

    def add_edge(self, u: int, v: int) -> None:
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs(self, start: int) -> List[int]:
        """Breadth-First Search using a queue. O(V + E) time."""
        visited: Set[int] = {start}
        order: List[int] = []
        queue: Deque[int] = deque([start])
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    def dfs(self, start: int) -> List[int]:
        """Depth-First Search using a stack. O(V + E) time."""
        visited: Set[int] = set()
        order: List[int] = []
        stack: List[int] = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            order.append(node)
            for neighbor in reversed(self.adj[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
        return order


def num_islands(grid: List[List[str]]) -> int:
    """Count connected components in a 2D grid. O(M * N) time."""
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                dfs(r, c)
                count += 1
    return count


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """Course Schedule — cycle detection via topological sort. O(V + E)."""
    adj: Dict[int, List[int]] = {i: [] for i in range(num_courses)}
    indegree = [0] * num_courses
    for course, prereq in prerequisites:
        adj[prereq].append(course)
        indegree[course] += 1

    queue: Deque[int] = deque(i for i in range(num_courses) if indegree[i] == 0)
    visited = 0
    while queue:
        node = queue.popleft()
        visited += 1
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return visited == num_courses
