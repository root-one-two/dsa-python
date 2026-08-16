# Recursion & Backtracking

**Recursion** solves a problem by calling itself on smaller subproblems until a base case is reached. **Backtracking** extends recursion to explore a **state-space tree**, building candidates step-by-step and **undoing choices** when constraints fail.

---

## ASCII: Backtracking State Tree (Subsets of [1,2])

```text
                    []
           /                  \
        [1]                    []
       /   \                  /   \
   [1,2]   [1]            [2]      []
    |       |              |        |
 [1,2]    [1]            [2]       []
```

Each level: include or exclude the next element.

---

## Features

- **Base case + recursive step** — guarantees termination
- **State-space exploration** — DFS over decision tree
- **Prune & rollback** — `choose` → `explore` → `unchoose`

---

## Pros & Cons

| Paradigm | Pros | Cons |
|:---|:---|:---|
| Recursion | Clean code; maps to trees and graphs | O(h) stack space; depth limits |
| Backtracking | Finds all valid solutions; pruning cuts search | Exponential worst case O(2^n)–O(n!) |

---

## When to Use

- **Recursion:** Tree/graph DFS, divide-and-conquer decomposition
- **Backtracking:** Permutations, combinations, subsets, constraint puzzles (N-Queens, Sudoku)
- **Avoid when:** Overlapping subproblems without state change → use DP instead

**Pattern cues:** "all subsets", "all permutations", "place queens", "word search" → backtracking.

---

## Top 5 Essential Problems

| Problem | Pattern | Complexity | Focus |
|:---|:---|:---|:---|
| Subsets / Power Set | Include / exclude | O(n × 2^n) | Branch at each index |
| Permutations | Swap backtracking | O(n × n!) | Build length-n arrangements |
| Combination Sum | Target reduction | O(2^t) | Prune when candidate > remaining |
| N-Queens | Constraint propagation | O(n!) | Track cols and diagonals in sets |
| Word Search | Grid DFS + rollback | O(M×N×4^L) | Mark visited in-place, restore |

---

## Implementations

- **Python:** [`solutions.py`](./solutions.py)
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Dynamic Programming](../dynamic_programming/README.md) — when subproblems overlap
- [Trees](../../data_structures/trees/README.md) — recursive traversals
- [Graphs](../../data_structures/graphs/README.md) — DFS is recursive backtracking on graphs
