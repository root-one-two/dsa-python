# Arrays & Dynamic Arrays

## What It Is

An **array** stores elements of the same type in **contiguous memory**, enabling O(1) index access. A **dynamic array** (Python `list`, Java `ArrayList`) grows automatically when capacity is exceeded, using a growth factor (~1.125x–1.5x) to amortize append cost.

---

## ASCII: Contiguous Memory Layout

```text
Index:   0    1    2    3    4
       ┌────┬────┬────┬────┬────┐
       │ 10 │ 20 │ 30 │ 40 │ 50 │  ← single memory block
       └────┴────┴────┴────┴────┘
```

---

## Complexity

| Operation | Time | Space | Notes |
|:---|:---|:---|:---|
| Access by index | O(1) | O(1) | Random access |
| Search | O(n) | O(1) | Linear scan |
| Insert / delete (end) | O(1)* | O(1) | *Amortized for dynamic arrays |
| Insert / delete (middle) | O(n) | O(1) | Must shift elements |

---

## Pros & Cons

**Pros**

- O(1) random access and strong cache locality
- Low per-element memory overhead

**Cons**

- O(n) resize when capacity is exceeded
- O(n) insert/delete away from the end

---

## When to Use

- Frequent lookup or access by index
- Dataset size is known or growth happens at the end
- Sequential iteration with minimal pointer overhead

**Pattern cues:** "subarray", "contiguous", "sorted pair", "window of size k" → think arrays + two pointers / sliding window.

---

## Top 5 Essential Problems

| Problem | Pattern | Complexity | Focus |
|:---|:---|:---|:---|
| Two Sum | Hash mapping | O(n) time | Trade space for single-pass pair lookup |
| Best Time to Buy and Sell Stock | Greedy / tracking | O(n) time | Track running min and max profit |
| Maximum Subarray (Kadane's) | Kadane's algorithm | O(n) time | Extend or restart subarray at each index |
| Container With Most Water | Two pointers | O(n) time | Inward sweep on height array |
| Trapping Rain Water | Two pointers | O(n) time | Track left/right max water levels |
| Subarray Product Less Than K | Sliding window | O(n) time | Variable window on running product |

Also in repo: **Sliding Window Maximum** (monotonic deque).

---

## Implementations

- **Python:** [`solutions.py`](./solutions.py)
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Hash Tables](../hash_tables/README.md) — Two Sum hash-map variant
- [Sorting](../../algorithms/sorting/README.md) — often preprocesses array data
- [Searching](../../algorithms/searching/README.md) — binary search on sorted arrays
