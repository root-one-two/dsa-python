# 🔄 Recursion & Backtracking

Recursion is a computational paradigm where a function solves a problem by invoking itself with smaller sub-instances until reaching a base case. **Backtracking** extends recursion to systematically explore a state space tree, building a candidate solution step-by-step and **undoing choices** (pruning) when constraints are violated.

---

## 📌 Features

- **Base Case & Recursive Step**: Guarantees termination while decomposing the problem into identical, smaller subproblems.
- **State Space Tree Exploration**: Explores potential solution paths using Depth-First Search (DFS).
- **Pruning & State Rollback**: Aborts dead ends early and reverses state mutations (`choose` $\rightarrow$ `explore` $\rightarrow$ `unchoose`) to conserve memory.

---

## ⚖️ Pros & Cons

| Paradigm | Pros | Cons |
| :--- | :--- | :--- |
| **Recursion** | • Clean, declarative, and elegant code<br>• Naturally maps to hierarchical structures (Trees, Graphs, ASTs) | • Call stack memory overhead ($O(h)$ space)<br>• Risk of StackOverflow for deep recursion |
| **Backtracking** | • Finds all valid combinations/permutations<br>• Pruning significantly reduces combinatorial search space | • Exponential worst-case time complexity ($O(k^n)$ or $O(n!)$)<br>• Sensitive to choice ordering |

---

## 🎯 When to Use

- **Use Recursion when:** The problem decomposes into identical subproblems with clean structural boundaries (e.g., Tree traversals, Divide-and-Conquer).
- **Use Backtracking when:** You need to generate all permutations, combinations, subsets, or solve constraint satisfaction puzzles (e.g., N-Queens, Sudoku, Maze pathfinding).
- **Avoid when:** Overlapping subproblems exist without state changes (use Dynamic Programming instead to prevent exponential redundant work).

---

## 🛠️ Essential Hands-On Problems

### 1. Subsets / Power Set
- **Pattern:** Decision Tree (Include / Exclude)
- **Complexity:** Time: $O(n \cdot 2^n)$, Space: $O(n)$
- **Key Takeaway:** At each index, branch into two decisions: include current element or exclude it, backtracking state along the way.

### 2. Permutations
- **Pattern:** State-Tracked Backtracking (`visited` set or in-place swap)
- **Complexity:** Time: $O(n \cdot n!)$, Space: $O(n)$
- **Key Takeaway:** Build arrangements of length $n$ by choosing from unused elements and undoing the choice upon return.

### 3. Combination Sum (Unbounded / Bounded)
- **Pattern:** Backtracking with Remaining Target Reduction
- **Complexity:** Time: $O(2^t)$ where $t = \text{target} / \min(\text{candidates})$, Space: $O(\text{target})$
- **Key Takeaway:** Prune branches where candidate values exceed the remaining target; control index progression to avoid duplicate combinations.

### 4. N-Queens
- **Pattern:** Constraint Propagation & Diagonal Collision Tracking
- **Complexity:** Time: $O(n!)$, Space: $O(n)$
- **Key Takeaway:** Use hash sets to track occupied columns, positive diagonals ($r + c$), and negative diagonals ($r - c$) for $O(1)$ conflict checks.

### 5. Word Search
- **Pattern:** 2D Grid DFS with Grid State Rollback
- **Complexity:** Time: $O(M \cdot N \cdot 4^L)$ where $L = \text{len(word)}$, Space: $O(L)$
- **Key Takeaway:** Traverse grid in 4 directions while marking cells visited in-place (e.g., replacing character with `'#'`) and restoring them post-recursion.
