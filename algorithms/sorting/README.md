# Sorting Algorithms

> **Before you read this:** Comfortable with [arrays](../../data_structures/arrays/README.md) — sorting rearranges array elements.

---

## In Plain English

**Sorting** means putting items in order — usually **smallest to largest** (or reverse).

Once data is sorted, many problems become easier: finding duplicates, merging ranges, binary search, and picking the Kth item.

---

## Real-World Examples

- **Contact list** sorted by name.
- **Leaderboard** sorted by score.
- **Calendar** events sorted by start time → merge overlapping meetings.
- **E-commerce** products sorted by price or rating.

---

## Key Ideas

| Term | Simple definition | Example |
|:---|:---|:---|
| **Stable sort** | Equal items keep original order | Two "A" students stay in submission order |
| **In-place** | Sort using little extra memory | Swap inside the same array |
| **Comparison sort** | Decide order by comparing pairs | Quick sort, merge sort |
| **Partition** | Split array into "left group" and "right group" | Dutch flag: 0s, 1s, 2s |
| **Quickselect** | Find Kth item without full sort | Partition until Kth lands in place |

---

## How It Works

**Merge sort** — split in half, sort halves, merge:

```text
[38, 27, 43, 3]  →  [38,27] [43,3]  →  [27,38] [3,43]  →  [3, 27, 38, 43]
```

**Dutch National Flag** — three sections in one pass:

```text
[2, 0, 2, 1, 1, 0]  →  [0, 0, 1, 1, 2, 2]
 low↑  mid↑     high↑
```

<details>
<summary><strong>Go deeper — algorithm families</strong></summary>

| Family | Typical time | Notes |
|:---|:---|:---|
| Merge / Quick sort | O(n log n) | Workhorse comparison sorts |
| Insertion / Bubble | O(n²) | Simple; OK for tiny or nearly sorted data |
| Counting / Radix | O(n + k) | Integer keys with bounded range |

**Stability** matters when sorting records by multiple fields (e.g. sort by city, then by name within city).
</details>

---

## What You Can Do With It

| Goal | Approach |
|:---|:---|
| Full sort | Merge sort, quick sort |
| Kth largest without full sort | Quickselect |
| Three categories in one pass | Dutch flag partition |
| Merge overlapping intervals | Sort by start, then merge |
| Custom order | Frequency map + bucket build |

---

## Complexity (quick reference)

*n = number of items*

| Approach | Time | Space |
|:---|:---|:---|
| Merge sort | O(n log n) | O(n) |
| Quick sort (average) | O(n log n) | O(log n) stack |
| Quickselect (average) | O(n) | O(1) |
| Dutch flag | O(n) | O(1) |
| Merge intervals | O(n log n) | O(n) |

---

## Common Interview Patterns

| When the problem says… | Think… |
|:---|:---|
| "Merge overlapping intervals" | Sort by start + merge |
| "Kth largest element" | Quickselect or heap |
| "Sort colors / three values" | Dutch flag |
| "Most rooms needed at once" | Sort meeting starts/ends |
| "Custom character order" | Frequency + build string |

---

## Practice Problems

| Problem | What it's really asking | Pattern |
|:---|:---|:---|
| Merge Intervals | Combine overlapping time ranges | Sort + merge |
| Kth Largest Element | Find Kth biggest without full sort | Quickselect |
| Sort Colors | Sort 0, 1, 2 in one pass | Dutch flag |
| Meeting Rooms II | Max simultaneous meetings? | Sort + sweep |
| Custom Sort String | Order letters by given priority | Frequency map |

---

## Code

- **Python:** [`solutions.py`](./solutions.py)
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Searching](../searching/README.md) — binary search needs sorted data
- [Greedy](../greedy/README.md) — interval scheduling after sorting
- [Arrays](../../data_structures/arrays/README.md) — most sort problems use arrays
