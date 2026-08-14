# ⚡ Dynamic Programming (DP)

Dynamic Programming is an optimization technique that solves complex problems by breaking them down into simpler, overlapping subproblems. It caches the results of subproblems to avoid redundant calculations, transforming exponential time complexities ($O(2^n)$) into polynomial time ($O(n)$ or $O(n^2)$).

---

## 📌 Features

- **Optimal Substructure**: The optimal solution to the overall problem contains optimal solutions to its subproblems.
- **Overlapping Subproblems**: The same subproblems are solved repeatedly throughout execution.
- **Two Approaches**:
  - **Top-Down (Memoization)**: Recursive approach with a cache/memo dictionary.
  - **Bottom-Up (Tabulation)**: Iterative approach filling a DP table in topological dependency order, often allowing space optimization to $O(1)$ or $O(n)$.

---

## ⚖️ Pros & Cons

| Approach | Pros | Cons |
| :--- | :--- | :--- |
| **Top-Down (Memoization)** | • Natural transition from recursive thinking<br>• Only computes subproblems that are actually reachable | • Function call stack overhead<br>• Risk of recursion depth limits in Python |
| **Bottom-Up (Tabulation)** | • No recursion call stack overhead<br>• Easily optimized for space (e.g., keeping only the previous 2 rows) | • Requires pre-determining exact evaluation order (topological order) |

---

## 🎯 When to Use

- **Use Dynamic Programming when:**
  - You need to find minimum/maximum costs, longest/shortest sequences, or count total number of valid ways.
  - Decisions made at step $i$ depend strictly on optimal outcomes of previous steps $0 \dots i-1$.
- **Avoid Dynamic Programming when:**
  - Subproblems do not overlap (use Divide and Conquer, e.g., Merge Sort).
  - The problem has a greedy choice property (where local optimal choices guarantee global optimum).

---

## 🛠️ Essential Hands-On Problems

### 1. Climbing Stairs / Fibonacci Sequence
- **Pattern:** 1D DP State Transition
- **State Transition:** $dp[i] = dp[i-1] + dp[i-2]$
- **Complexity:** Time: $O(n)$, Space: $O(1)$
- **Key Takeaway:** The simplest linear state recurrence, optimized from $O(n)$ space down to two variables.

### 2. Coin Change (Fewest Coins)
- **Pattern:** Unbounded Knapsack (Minimization)
- **State Transition:** $dp[i] = \min(dp[i], dp[i - \text{coin}] + 1)$
- **Complexity:** Time: $O(\text{amount} \cdot \text{len(coins)})$, Space: $O(\text{amount})$
- **Key Takeaway:** Building answers bottom-up for all amounts from $1 \dots \text{amount}$ with base case $dp[0] = 0$.

### 3. Longest Increasing Subsequence (LIS)
- **Pattern:** Subsequence Matching / Patience Sorting
- **Complexity:** $O(n^2)$ Tabulation $\rightarrow$ Optimized to $O(n \log n)$ with Binary Search / Patience Sorting
- **Key Takeaway:** Maintain an active tails array and replace the smallest element $\ge nums[i]$ using binary search.

### 4. 0/1 Knapsack & Partition Equal Subset Sum
- **Pattern:** Bounded Knapsack State Compression
- **State Transition:** $dp[w] = dp[w] \lor dp[w - \text{num}]$ (iterating backwards to prevent re-use)
- **Complexity:** Time: $O(n \cdot \text{target})$, Space: $O(\text{target})$
- **Key Takeaway:** Reverse iteration over the target array compresses 2D table $O(n \times W)$ to 1D $O(W)$.

### 5. Longest Common Subsequence (LCS) / Edit Distance
- **Pattern:** 2D String DP Grid
- **State Transition:** If $s1[i] == s2[j]$: $dp[i][j] = dp[i-1][j-1] + 1$; else $\max(dp[i-1][j], dp[i][j-1])$
- **Complexity:** Time: $O(m \cdot n)$, Space: $O(m \cdot n)$ (optimizable to $O(\min(m, n))$)
- **Key Takeaway:** Classic matrix grid state evolution for matching and alignment metrics.
