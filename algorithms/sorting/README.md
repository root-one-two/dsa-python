# Sorting Algorithms

Sorting arranges a collection into a specific order (usually ascending). It underpins binary search, duplicate detection, interval merging, and many divide-and-conquer optimizations.

---

## ASCII: Merge Sort Divide & Conquer

```text
       [38, 27, 43, 3]
          /        \
    [38, 27]    [43, 3]
     /    \      /    \
  [38]  [27]  [43]   [3]
     \    /      \    /
    [27, 38]    [3, 43]
          \        /
       [3, 27, 38, 43]
```

---

## Features

- **Comparison vs. non-comparison:** Comparison sorts lower bound is O(n log n); counting/radix can achieve O(n + k) on bounded keys.
- **Stability:** Stable sorts preserve relative order of equal elements.
- **In-place vs. out-of-place:** In-place uses O(1) auxiliary space; merge sort needs O(n).

---

## Pros & Cons

| Category | Pros | Cons |
|:---|:---|:---|
| Divide & conquer (Merge / Quick) | O(n log n) average; scalable | Quick sort O(n²) worst case; merge sort O(n) space |
| Elementary (Insertion / Bubble) | Simple; O(1) space | O(n²) on large inputs |
| Linear (Counting / Radix) | O(n) on bounded integers | High space if key range k >> n |

---

## When to Use

- **Merge sort:** Stability required or sorting linked lists / external data
- **Quick sort:** In-place average-case performance matters
- **Insertion sort:** Small n or nearly sorted data
- **Counting / radix:** Bounded integer or string keys

**Pattern cues:** "merge intervals", "k-th largest", "sort colors", "meeting rooms" → sorting or partitioning.

---

## Top 5 Essential Problems

| Problem | Pattern | Complexity | Focus |
|:---|:---|:---|:---|
| Merge Intervals | Sort + merge | O(n log n) time | Sort by start; single-pass overlap merge |
| Kth Largest (Quickselect) | Partitioning | O(n) average | Partial sort via Hoare/Lomuto partition |
| Sort Colors (Dutch Flag) | Three-way partition | O(n) time | `low`, `mid`, `high` pointers |
| Meeting Rooms II | Sort + sweep | O(n log n) time | Peak overlap from start/end timelines |
| Custom Sort String | Bucket / frequency | O(n + k) time | Build output from frequency map |

Also in repo: **Merge Sort** reference implementation.

---

## Implementations

- **Python:** [`solutions.py`](./solutions.py)
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Searching](../searching/README.md) — requires sorted input for binary search
- [Greedy](../greedy/README.md) — interval scheduling after sorting by end time
- [Arrays](../../data_structures/arrays/README.md) — most sorting problems use arrays
