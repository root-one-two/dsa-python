# Recursion & Backtracking

> **Before you read this:** Comfortable with [trees](../../data_structures/trees/README.md) (recursive traversals) and basic functions. [Stacks](../../data_structures/stacks_queues/README.md) mirror the call stack.

---

## In Plain English

**Recursion** means a function **calls itself** on a smaller version of the problem until a simple **base case** stops it.

Example: factorial of 5 = 5 × factorial of 4 × … × 1.

**Backtracking** is recursion + **exploring choices**: try a path, and if it fails, **undo** the choice and try another — like walking a maze, marking dead ends, and returning to try a different turn.

---

## Real-World Examples

- **Recursion:** Size of a folder = size of files + size of subfolders.
- **Backtracking:** Sudoku — place a number, check rules, backtrack if stuck.
- **Backtracking:** All outfits from 3 shirts and 2 pants — try combinations.
- **Word search puzzle** — try each direction, undo if path wrong.

---

## Key Ideas

| Term | Simple definition | Example |
|:---|:---|:---|
| **Base case** | Simplest input — stop recursion | Empty list, one element |
| **Recursive case** | Break into smaller subproblem | `f(n) = n × f(n-1)` |
| **Call stack** | Memory of active recursive calls | Stack of "where to return" |
| **Backtrack** | Undo last choice and try another | Remove queen, try next column |
| **Prune** | Stop exploring hopeless branches early | Sum already exceeds target |
| **State** | Current partial solution | `[1, 3]` so far in subset |

---

## How It Works

**Subsets** — at each number, include it or skip it:

```text
                    []
           /                  \
        [1]                    []
       /   \                  /   \
   [1,2]   [1]            [2]      []
    |       |              |        |
 [1,2]    [1]            [2]       []
```

**Backtracking template:**

```text
choose → explore deeper → unchoose (undo)
```

**Word search** — mark cell visited, explore 4 directions, restore cell when returning.

<details>
<summary><strong>Go deeper — complexity & stack depth</strong></summary>

- Subsets: O(2^n) combinations.
- Permutations: O(n!).
- Call stack depth = recursion depth; very deep recursion can hit stack limits in Python.
- Pruning (e.g. skip when sum > target) dramatically cuts real runtime.
</details>

---

## What You Can Do With It

| Goal | Approach |
|:---|:---|
| Generate all subsets | Include/exclude each element |
| Generate all permutations | Swap / choose unused elements |
| Find all combinations with sum | Reduce target, backtrack |
| Place N queens | Try each column, track conflicts |
| Path in grid | DFS + mark/unmark cells |

---

## Complexity (quick reference)

| Problem type | Typical time | Space |
|:---|:---|:---|
| Subsets | O(n × 2^n) | O(n) stack |
| Permutations | O(n × n!) | O(n) |
| Combination sum | O(2^target/min) | O(target) |
| N-Queens | O(n!) | O(n) |
| Word search | O(M×N×4^L) | O(L) |

---

## Common Interview Patterns

| When the problem says… | Think… |
|:---|:---|
| "All subsets / power set" | Include/exclude recursion |
| "All permutations" | Swap or used-set backtracking |
| "Combination sum" | Target reduction + prune |
| "N queens / sudoku" | Constraint tracking + backtrack |
| "Word search in grid" | DFS + temporary mark |

---

## Practice Problems

| Problem | What it's really asking | Pattern |
|:---|:---|:---|
| Subsets | List every possible subset | Include/exclude |
| Permutations | List every ordering | Swap backtracking |
| Combination Sum | Ways to sum to target from candidates | Target reduction |
| N-Queens | Place N queens with no attacks | Constraint sets |
| Word Search | Does word exist as adjacent path? | Grid DFS + undo |

---

## Code

- **Python:** [`solutions.py`](./solutions.py)
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Dynamic Programming](../dynamic_programming/README.md) — when subproblems overlap, cache instead of re-explore
- [Graphs](../../data_structures/graphs/README.md) — DFS is backtracking on graphs
- [Trees](../../data_structures/trees/README.md) — natural recursive structure
