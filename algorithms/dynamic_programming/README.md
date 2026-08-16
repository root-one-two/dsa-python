# Dynamic Programming (DP)

Dynamic Programming solves problems with **overlapping subproblems** and **optimal substructure** by caching subproblem results — turning exponential brute force into polynomial time.

---

## ASCII: 2D DP Grid (LCS)

```text
  ""  a  b  c
""  0  0  0  0
a   0  1  1  1
b   0  1  2  2
c   0  1  2  3   ← LCS("abc","abc") = 3
```

Each cell builds from neighbors: match → diagonal + 1; else → max(left, up).

---

## Features

- **Optimal substructure** — global optimum contains optimal sub-solutions
- **Overlapping subproblems** — same subproblem solved many times in naive recursion
- **Top-down (memoization)** vs. **bottom-up (tabulation)** — same logic, different execution order

---

## Pros & Cons

| Approach | Pros | Cons |
|:---|:---|:---|
| Top-down memo | Natural from recursion; computes only reachable states | Stack overhead; Python depth limits |
| Bottom-up tabulation | No recursion stack; easy space optimization | Must determine evaluation order |

---

## When to Use

- Min/max cost, longest/shortest sequence, count of valid ways
- Decision at step i depends on optimal results from steps 0…i−1

**Avoid when:** No overlapping subproblems (use divide & conquer) or greedy proof exists.

**Pattern cues:** "fewest coins", "climbing stairs", "knapsack", "LCS", "edit distance" → DP.

---

## Top 5 Essential Problems

| Problem | Pattern | Complexity | Focus |
|:---|:---|:---|:---|
| Climbing Stairs / Fibonacci | 1D DP | O(n) time, O(1) space | `dp[i] = dp[i-1] + dp[i-2]` |
| Coin Change | Unbounded knapsack min | O(amount × coins) | Bottom-up from amount 0 |
| Longest Increasing Subsequence | Patience sorting | O(n log n) | Binary search on tails array |
| Partition Equal Subset Sum | 0/1 knapsack compress | O(n × target) | Reverse iteration prevents reuse |
| LCS / Edit Distance | 2D string grid | O(m × n) | Match → diagonal; else max neighbors |

---

## Implementations

- **Python:** [`solutions.py`](./solutions.py)
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Recursion & Backtracking](../recursion_backtracking/README.md) — DP adds memoization to recursive structure
- [Greedy](../greedy/README.md) — when local choice is provably optimal, skip DP
- [Searching](../searching/README.md) — LIS optimized with binary search
