# Arrays & Dynamic Arrays

> **Before you read this:** No prerequisites — this is the best place to start.

---

## In Plain English

An **array** is a **fixed row of slots**, each with a **number** (index). You can jump directly to slot 3 without visiting slots 0, 1, and 2 first.

A **dynamic array** (Python `list`, Java `ArrayList`) is the same idea, but the row **grows automatically** when you run out of space — like adding more lockers to the end of a hallway.

---

## Real-World Examples

- **Playlist track numbers** — song #5 is always at position 5 in an ordered list.
- **Seating chart** — seat 12 in row 4 maps to a specific spot.
- **Shopping cart items** — append new items at the end; rarely insert in the middle.

---

## Key Ideas

| Term | Simple definition | Example |
|:---|:---|:---|
| **Index** | Position number (usually starts at 0) | `arr[0]` is the first item |
| **Contiguous memory** | Items stored next to each other in memory | Like consecutive lockers |
| **Dynamic array** | Array that resizes when full | Python `list.append()` |
| **Random access** | Reach any index in one step | Open locker #7 directly |
| **Two pointers** | Two indices moving through the array | Start from both ends and meet in the middle |
| **Sliding window** | A sub-range that slides across the array | Track sum of last 3 elements while moving |

---

## How It Works

```text
Index:   0    1    2    3    4
       ┌────┬────┬────┬────┬────┐
       │ 10 │ 20 │ 30 │ 40 │ 50 │
       └────┴────┴────┴────┴────┘
         ↑
    arr[0] = 10  (first item)
    arr[4] = 50  (last item)
```

**Two pointers** (e.g. Container With Most Water):

```text
height: [1, 8, 6, 2, 5, 4, 8, 3, 7]
         L                       R   ← move the shorter side inward
```

---

## What You Can Do With It

| Action | Plain English |
|:---|:---|
| **Access by index** | "Give me item at position i" |
| **Search** | Walk from start until you find a value |
| **Append** | Add at the end (fast for dynamic arrays) |
| **Insert in middle** | Shift everything after the gap — slow |
| **Scan with two pointers** | Solve pair/window problems in one pass |

---

## Complexity (quick reference)

*n = number of items in the array*

| Operation | Time | Notes |
|:---|:---|:---|
| Access by index | O(1) | Direct jump |
| Search | O(n) | May scan entire array |
| Append (end) | O(1)* | *Usually fast; occasional O(n) resize |
| Insert/delete middle | O(n) | Must shift elements |

<details>
<summary><strong>Go deeper — cache locality & amortized append</strong></summary>

- **Cache locality:** Because items sit side-by-side in memory, the CPU reads nearby values efficiently when looping.
- **Amortized append:** Dynamic arrays allocate extra space (~1.125x–1.5x growth) so most appends are O(1); occasionally the whole array is copied when resizing.
</details>

---

## Common Interview Patterns

| When the problem says… | Think… |
|:---|:---|
| "Two numbers that sum to target" | Hash map while scanning |
| "Maximum profit from prices" | Track running minimum |
| "Maximum subarray sum" | Kadane's algorithm |
| "Subarray with condition (sum/product)" | Sliding window |
| "Pair from both ends" | Two pointers |

---

## Practice Problems

| Problem | What it's really asking | Pattern |
|:---|:---|:---|
| Two Sum | Find two indices whose values add to target | Hash map |
| Best Time to Buy and Sell Stock | Max profit from one buy and one sell | Track min price |
| Maximum Subarray | Largest sum of any contiguous chunk | Kadane's |
| Container With Most Water | Max area between two vertical lines | Two pointers |
| Trapping Rain Water | How much water sits between bars | Two pointers |
| Subarray Product Less Than K | Count subarrays with product below k | Sliding window |

---

## Code

- **Python:** [`solutions.py`](./solutions.py)
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Hash Tables](../hash_tables/README.md) — Two Sum with a map
- [Sorting](../../algorithms/sorting/README.md) — often preprocess arrays
- [Searching](../../algorithms/searching/README.md) — binary search on sorted arrays
