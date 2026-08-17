# Searching Algorithms

> **Before you read this:** Comfortable with [arrays](../../data_structures/arrays/README.md). [Sorting](../sorting/README.md) first if data isn't already ordered.

---

## In Plain English

**Searching** means finding something: a specific value, a position, or the **best answer** to a question.

- **Linear search** — check every item one by one (works on any list).
- **Binary search** — on **sorted** data, eliminate half the remaining items each step (much faster).
- **Binary search on the answer** — when the question is "what is the smallest X that still works?" and you can test X with a yes/no check.

---

## Real-World Examples

- **Dictionary** — open to middle, compare, go left or right (binary search idea).
- **Guessing game** — "I'm thinking of 1–100" — each guess halves possibilities.
- **Shipping capacity** — "What's the minimum ship size that can deliver all packages in D days?"
- **Eating speed** — "What's the slowest banana-eating speed that still finishes in time?"

---

## Key Ideas

| Term | Simple definition | Example |
|:---|:---|:---|
| **Linear search** | Scan from start to end | Find sock in messy drawer |
| **Binary search** | Halve search space each step | Sorted list only |
| **Monotonic** | Answer flips from "no" to "yes" (or vice versa) as value increases | Speed 3 fails, speed 4 works → try between |
| **Predicate** | Yes/no test: "Can we finish with speed k?" | `can_finish(k)` |
| **Lower bound** | First index where value ≥ target | Insert position in sorted array |

---

## How It Works

**Binary search** on sorted array `[1, 3, 5, 7, 9, 11, 13, 15]`, find 7:

```text
Step 1:  lo=0  mid=7  hi=15  →  mid value 7 = target ✓

If target were 9:
Step 1: mid=7, 9>7 → search right half [9,11,13,15]
Step 2: mid=11, 9<11 → search left of mid → found at index 4
```

**Binary search on answer** — find minimum speed that works:

```text
Try speed 4 → too slow? no → works
Try speed 2 → works
Try speed 1 → fails
Answer: smallest speed that works is between 1 and 2 → narrow with binary search
```

<details>
<summary><strong>Go deeper — loop templates</strong></summary>

Avoid overflow: `mid = lo + (hi - lo) // 2`

Two common templates:

- `while lo <= hi` — standard search
- `while lo < hi` — lower bound style

Off-by-one errors are the #1 bug in binary search — always trace with a tiny example.
</details>

---

## What You Can Do With It

| Question | Method |
|:---|:---|
| "Is X in the array?" | Binary search (if sorted) |
| "Where to insert X?" | Lower bound |
| "Find in rotated sorted array" | Modified binary search |
| "Minimum value that still works?" | Binary search on answer |
| "Median of two sorted arrays?" | Partition bisection (advanced) |

---

## Complexity (quick reference)

*n = array length, R = answer range size*

| Method | Time | When |
|:---|:---|:---|
| Linear search | O(n) | Unsorted or tiny |
| Binary search | O(log n) | Sorted array |
| Binary search on answer | O(n log R) | Monotonic yes/no test costs O(n) |

---

## Common Interview Patterns

| When the problem says… | Think… |
|:---|:---|
| "Sorted array, find target" | Standard binary search |
| "Rotated sorted array" | Which half is sorted? |
| "Minimum in rotated array" | Compare mid vs right |
| "Minimize maximum" / "maximize minimum" | Binary search on answer |
| "Koko eating bananas" | `can_finish(speed)` predicate |

---

## Practice Problems

| Problem | What it's really asking | Pattern |
|:---|:---|:---|
| Binary Search | Find index of target (or -1) | Standard bisection |
| Search Rotated Sorted Array | Find target in rotated list | Modified binary search |
| Find Minimum in Rotated Array | Where does rotation start? | Pivot detection |
| Koko Eating Bananas | Slowest eating speed that works? | Answer-space search |
| Median of Two Sorted Arrays | Median without merging | Partition bisection |

Also in repo: **Capacity To Ship Packages** (same answer-space pattern).

---

## Code

- **Python:** [`solutions.py`](./solutions.py)
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Sorting](../sorting/README.md) — O(n log n) preprocess for repeated binary search
- [Dynamic Programming](../dynamic_programming/README.md) — different optimization lens
- [Strings, Two Pointers & Sliding Window](../strings/README.md) — two indices, but not binary search
- [Arrays](../../data_structures/arrays/README.md) — search substrate
