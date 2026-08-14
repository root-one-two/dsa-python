# 🎯 Greedy Algorithms

A **Greedy Algorithm** builds a solution step by step, always choosing the option that offers the most immediate (local) benefit. It relies on the heuristic that locally optimal choices lead to a globally optimal solution without ever backtracking or re-evaluating past choices.

---

## 📌 Features

- **Greedy Choice Property**: A global optimum can be arrived at by selecting a local optimum without looking back.
- **Optimal Substructure**: An optimal solution to the problem contains optimal solutions to its subproblems.
- **Single Pass / Irreversible**: Once a choice is made, it is never changed, making greedy algorithms exceptionally fast ($O(n)$ or $O(n \log n)$).

---

## ⚖️ Pros & Cons

| Aspect | Pros | Cons |
| :--- | :--- | :--- |
| **Performance** | • Extremely fast runtime (often $O(n)$ or $O(n \log n)$)<br>• Minimal memory footprint ($O(1)$ auxiliary) | • Only applies to problems with mathematical greedy proof |
| **Design** | • Simple and intuitive logic<br>• Straightforward implementation | • Does not guarantee optimal solution for general cases (fails on 0/1 Knapsack, Coin Change with arbitrary denominations) |

---

## 🎯 When to Use

- **Use Greedy when:**
  - The problem has provable greedy choice and optimal substructure properties (e.g., Interval Scheduling, Huffman Coding, Minimum Spanning Tree, Dijkstra).
  - You need a fast, high-quality approximation for NP-hard problems.
- **Avoid Greedy when:**
  - Future choices depend on accumulated state or multiple concurrent constraints where local greed traps the algorithm into a suboptimal dead end.

---

## 🛠️ Essential Hands-On Problems

### 1. Jump Game I & II
- **Pattern:** Furthest Reachable Index Tracking
- **Complexity:** Time: $O(n)$, Space: $O(1)$
- **Key Takeaway:** Maintain a `max_reach` variable at each index. For Jump Game II, advance jump counters whenever reaching the boundary of the current jump window.

### 2. Gas Station
- **Pattern:** Running Deficit & Reset Sweep
- **Complexity:** Time: $O(n)$, Space: $O(1)$
- **Key Takeaway:** If total gas $\ge$ total cost, a solution is guaranteed. Reset starting station whenever the running tank drops below zero.

### 3. Task Scheduler
- **Pattern:** Frequency Bottleneck Math & Idle Slot Filling
- **Complexity:** Time: $O(n)$, Space: $O(1)$ (constant alphabet size)
- **Key Takeaway:** Calculate total cycles needed based on the most frequent task's cooldown intervals: $(\text{max\_freq} - 1) \times (n + 1) + \text{count\_max\_freq}$.

### 4. Candy
- **Pattern:** Two-Way Pass (Left-to-Right & Right-to-Left)
- **Complexity:** Time: $O(n)$, Space: $O(n)$
- **Key Takeaway:** Satisfy left-neighbor constraints with a forward pass, then satisfy right-neighbor constraints with a backward pass taking $\max(\text{candy}[i], \text{candy}[i+1] + 1)$.

### 5. Non-overlapping Intervals (Interval Scheduling)
- **Pattern:** Earliest Deadline First (Sort by End Time)
- **Complexity:** Time: $O(n \log n)$, Space: $O(1)$
- **Key Takeaway:** Always select the interval that finishes earliest to leave maximum room for subsequent intervals, greedily minimizing removals.
