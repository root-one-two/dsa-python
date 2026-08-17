"""Union-Find — disjoint set with path compression and union by rank."""

from typing import List


class UnionFind:
    """Disjoint set. Find/union are effectively O(1) amortized."""

    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        """Merge groups. Returns False if a and b were already connected."""
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.components -= 1
        return True

    def connected(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)


def find_circle_num(is_connected: List[List[int]]) -> int:
    """Number of Provinces — friend circles in an n×n matrix. O(n²)."""
    n = len(is_connected)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i + 1, n):
            if is_connected[i][j] == 1:
                uf.union(i, j)
    return uf.components


def valid_tree(n: int, edges: List[List[int]]) -> bool:
    """Graph Valid Tree — n-1 edges, no cycle, one component. O(n)."""
    if len(edges) != n - 1:
        return False
    uf = UnionFind(n)
    for a, b in edges:
        if not uf.union(a, b):
            return False
    return uf.components == 1


def equations_possible(equations: List[str]) -> bool:
    """Satisfiability of Equality Equations over letters a–z. O(n)."""
    uf = UnionFind(26)
    for eq in equations:
        if eq[1] == "=":
            uf.union(ord(eq[0]) - ord("a"), ord(eq[3]) - ord("a"))
    for eq in equations:
        if eq[1] == "!":
            a, b = ord(eq[0]) - ord("a"), ord(eq[3]) - ord("a")
            if uf.connected(a, b):
                return False
    return True
