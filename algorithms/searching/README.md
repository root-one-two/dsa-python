# 🔍 Searching Algorithms

Searching algorithms locate the position or existence of a target value within a data structure. While linear scans examine each element sequentially, binary search and binary search on the answer space achieve logarithmic time complexity $O(\log n)$ by discarding half of the search space at each step.

---

## 📌 Features

- **Sequential vs. Pruned Search**: Linear Search examines every element ($O(n)$), whereas Binary Search halves the remaining candidates per iteration ($O(\log n)$).
- **Monotonicity Requirement**: Binary search requires monotonic behavior (sorted arrays or monotonic boolean functions $f(x) \in \{\text{False}, \text{True}\}$).
- **Search on Answer Space (Bisection)**: Binary search can optimize discrete or continuous values by testing feasibility over a bounded range $[\text{low}, \text{high}]$.

---

## ⚖️ Pros & Cons

| Algorithm | Pros | Cons |
| :--- | :--- | :--- |
| **Linear Search** | • Works on unsorted and unstructured data<br>• Zero preprocessing required | • Inefficient for repeated queries ($O(n)$ per query) |
| **Binary Search (Sorted Array)** | • Logarithmic time ($O(\log n)$)<br>• $O(1)$ space overhead | • Requires monotonic/sorted data (sorting costs $O(n \log n)$ upfront) |
| **Binary Search on Answer (Bisection)** | • Solves complex min-max optimization problems in $O(f(n) \log(\text{range}))$ | • Requires proving monotonic property for the predicate condition |

---

## 🎯 When to Use

- **Use Linear Search when:** The collection is small, unsorted, or accessed only once.
- **Use Standard Binary Search when:** You have a static, sorted array and need rapid lookups, boundary positions (`lower_bound` / `upper_bound`), or insert locations.
- **Use Binary Search on Answer when:** The problem asks to "minimize the maximum" or "maximize the minimum" and verifying a proposed answer takes polynomial time $O(n)$.

---

## 🛠️ Essential Hands-On Problems

### 1. Binary Search (`lower_bound` & `upper_bound`)
- **Pattern:** Boundary Finding
- **Complexity:** Time: $O(\log n)$, Space: $O(1)$
- **Key Takeaway:** Avoid off-by-one errors using invariant templates (`low <= high` vs. `low < high`) and proper mid-point calculation (`mid = low + (high - low) // 2`).

### 2. Search in Rotated Sorted Array
- **Pattern:** Modified Binary Search with Inflection Point
- **Complexity:** Time: $O(\log n)$, Space: $O(1)$
- **Key Takeaway:** Determine which half of the array (left or right) is strictly sorted, then check if the target lies within that sorted range.

### 3. Find Minimum in Rotated Sorted Array
- **Pattern:** Pivot / Inflection Point Detection
- **Complexity:** Time: $O(\log n)$, Space: $O(1)$
- **Key Takeaway:** Compare `nums[mid]` against `nums[high]` to systematically discard the sorted half and converge on the pivot element.

### 4. Koko Eating Bananas / Capacity To Ship Packages
- **Pattern:** Binary Search on Answer (Monotonic Predicate)
- **Complexity:** Time: $O(n \log(\max - \min))$, Space: $O(1)$
- **Key Takeaway:** Formulate a helper function `can_finish(speed)` that returns boolean truth values monotonically across the search bounds.

### 5. Median of Two Sorted Arrays
- **Pattern:** Binary Search on Partition Cuts
- **Complexity:** Time: $O(\log(\min(m, n)))$, Space: $O(1)$
- **Key Takeaway:** Partition both arrays simultaneously such that left halves equal right halves in length and all left elements are $\le$ all right elements.
