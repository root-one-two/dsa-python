# Dynamic Programming (DP)

> **Before you read this:** Comfortable with [recursion & backtracking](../recursion_backtracking/README.md). DP is recursion + **remembering** answers you've already computed.

---

## In Plain English

Some problems ask you to solve the **same smaller problem many times**.

**Dynamic Programming** means: **solve each subproblem once, save the answer, reuse it**.

Instead of computing "ways to climb 3 steps" hundreds of times in a naive tree, you store: step 1 = 1 way, step 2 = 2 ways, step 3 = 3 ways — then build up.

---

## Real-World Examples

- **Climbing stairs** — ways to reach step N depend on ways to reach N-1 and N-2 (like Fibonacci).
- **Coin change** — fewest coins to make ₹11 using ₹1, ₹2, ₹5 coins.
- **Spell checker** — edit distance: fewest edits to turn "cat" into "cut".
- **Route planning** — shortest path when sub-routes are reused.

---

## Key Ideas

| Term | Simple definition | Example |
|:---|:---|:---|
| **Subproblem** | Smaller version of main question | "Ways to reach step 5" |
| **Overlapping subproblems** | Same subproblem needed many times | Fibonacci: F(3) needed twice |
| **Optimal substructure** | Best full answer uses best sub-answers | Best path to 5 uses best path to 4 or 3 |
| **Memoization** | Cache results (top-down / recursive) | `memo[5] = 8` |
| **Tabulation** | Fill table bottom-up (iterative) | `dp[0], dp[1], … dp[n]` |
| **State** | What you track in `dp[i]` | Min coins for amount i |

---

## How It Works

**Climbing stairs** — to reach step 5, you came from step 4 or step 3:

```text
step:  1   2   3   4   5
ways:  1   2   3   5   8
       ↑   ↑   ↑   ↑   ↑
      base 1+1 1+2 2+3 3+5
```

**2D grid (LCS)** — match characters → diagonal +1; else max(up, left):

```text
  ""  a  b  c
""  0  0  0  0
a   0  1  1  1
b   0  1  2  2
c   0  1  2  3   ← longest common subsequence length = 3
```

<details>
<summary><strong>Go deeper — top-down vs bottom-up</strong></summary>

- **Top-down:** Write recursion + `memo` dict — natural but stack overhead.
- **Bottom-up:** Fill `dp` array in dependency order — often faster, easier to optimize space (e.g. only keep last 2 rows for Fibonacci).
- **0/1 Knapsack trick:** Iterate target **backwards** when each item can be used once.
</details>

---

## What You Can Do With It

| Question | DP approach |
|:---|:---|
| "How many ways?" | Count subproblems |
| "Minimum / maximum cost?" | Min/max recurrence |
| "Longest subsequence?" | 1D or 2D table |
| "Can we partition equally?" | Subset sum boolean DP |
| "Fewest edits between strings?" | 2D edit distance grid |

---

## Complexity (quick reference)

| Problem | Time | Space |
|:---|:---|:---|
| Climbing stairs | O(n) | O(1) optimized |
| Coin change | O(amount × coins) | O(amount) |
| LIS | O(n log n) optimized | O(n) |
| Partition / 0/1 knapsack | O(n × target) | O(target) |
| LCS / edit distance | O(m × n) | O(m × n) |

---

## Common Interview Patterns

| When the problem says… | Think… |
|:---|:---|
| "Count ways to…" | 1D DP recurrence |
| "Fewest coins / min cost" | Unbounded knapsack min |
| "Longest increasing subsequence" | Patience sorting / tails |
| "Equal subset sum" | 0/1 knapsack boolean |
| "Longest common subsequence" | 2D string grid |

---

## Practice Problems

| Problem | What it's really asking | Pattern |
|:---|:---|:---|
| Climbing Stairs | How many ways to climb N steps (1 or 2 each)? | 1D DP |
| Coin Change | Fewest coins to make amount? | Unbounded knapsack |
| Longest Increasing Subsequence | Longest strictly increasing subsequence | Patience / binary search |
| Partition Equal Subset Sum | Split into two equal sums? | 0/1 knapsack |
| LCS / Edit Distance | How similar are two strings? | 2D grid |

---

## Code

- **Python:** [`solutions.py`](./solutions.py)
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Recursion & Backtracking](../recursion_backtracking/README.md) — DP adds a cache
- [Greedy](../greedy/README.md) — try greedy first when it provably works (faster)
- [Searching](../searching/README.md) — LIS uses binary search optimization
- [Bit Manipulation](../bit_manipulation/README.md) — bitmask DP for small subsets
