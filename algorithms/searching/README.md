# Searching Algorithms

Searching finds a target value or optimal answer in a data structure. **Linear search** scans every element in O(n). **Binary search** halves the search space each step in O(log n) when data is monotonic or sorted.

---

## ASCII: Binary Search Halving

```text
Sorted: [1, 3, 5, 7, 9, 11, 13, 15]
              mid=7
        lo              hi
After target > 7:  search right half only
              [9, 11, 13, 15]
```

---

## Features

- **Sequential vs. pruned:** Linear O(n) vs. binary O(log n)
- **Monotonicity:** Binary search needs sorted arrays or monotonic predicates
- **Search on answer space:** Bisect over `[low, high]` with a `can_finish(x)` helper

---

## Pros & Cons

| Approach | Pros | Cons |
|:---|:---|:---|
| Linear search | Works on unsorted data; no preprocessing | O(n) per query |
| Binary search | O(log n); O(1) space | Requires sorted/monotonic data |
| Binary search on answer | Solves min-max optimization problems | Must prove monotonic predicate |

---

## When to Use

- **Linear:** Small or unsorted data; single access
- **Standard binary search:** Static sorted array; `lower_bound` / `upper_bound`
- **Binary search on answer:** "Minimize the maximum" / "maximize the minimum" with fast feasibility check

**Pattern cues:** "sorted array", "rotated sorted", "minimum capacity", "eating speed" → binary search.

---

## Top 5 Essential Problems

| Problem | Pattern | Complexity | Focus |
|:---|:---|:---|:---|
| Binary Search / Lower Bound | Boundary finding | O(log n) time | `mid = lo + (hi-lo)//2`; watch off-by-one |
| Search in Rotated Sorted Array | Modified binary search | O(log n) time | Identify sorted half each step |
| Find Minimum in Rotated Array | Pivot detection | O(log n) time | Compare `nums[mid]` vs `nums[hi]` |
| Koko Eating Bananas | Answer-space bisection | O(n log max) | `can_finish(speed)` predicate |
| Median of Two Sorted Arrays | Partition bisection | O(log min(m,n)) | Align left/right partition sizes |

Also in repo: **Capacity To Ship Packages** (same answer-space pattern).

---

## Implementations

- **Python:** [`solutions.py`](./solutions.py)
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Sorting](../sorting/README.md) — O(n log n) preprocessing for binary search
- [Dynamic Programming](../dynamic_programming/README.md) — alternative when overlapping subproblems exist
- [Arrays](../../data_structures/arrays/README.md) — primary search substrate
