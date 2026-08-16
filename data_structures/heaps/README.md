# Heaps & Priority Queues

## What It Is

A **heap** is a complete binary tree satisfying the **heap property**:

- **Min-heap:** parent ≤ children (root is minimum)
- **Max-heap:** parent ≥ children (root is maximum)

Binary heaps are typically stored in a **flat array** — no pointer overhead. A **priority queue** is the abstract ADT; a heap is a common implementation.

---

## ASCII: Min-Heap as Array

```text
Tree view:        Array index mapping:
      1              index:  0  1  2  3  4
     / \            value: [1, 3, 2, 7, 5]
    3   2
   / \
  7   5

parent(i) = (i-1)/2    left(i) = 2i+1    right(i) = 2i+2
```

---

## Complexity

| Operation | Time | Space |
|:---|:---|:---|
| Peek min/max | O(1) | O(1) |
| Insert | O(log n) | O(1) |
| Extract min/max | O(log n) | O(1) |
| Search arbitrary element | O(n) | O(1) |
| Build heap from array | O(n) | O(1) |

---

## Pros & Cons

**Pros**

- O(1) access to min or max element
- O(log n) insert and extract; efficient array layout

**Cons**

- O(n) search for non-extreme elements
- Heap iteration does not yield fully sorted order

---

## When to Use

- Job scheduling and task prioritization
- Dijkstra's and Prim's algorithms (graph min-selection)
- K-th largest/smallest in streaming data

**Pattern cues:** "k-th largest", "merge k lists", "top k frequent" → heap or bucket sort.

---

## Top 5 Essential Problems

| Problem | Pattern | Complexity | Focus |
|:---|:---|:---|:---|
| Min-Heap (core ADT) | Array-backed heap | O(log n) insert/extract | `sift_up` / `sift_down` |
| Kth Largest Element | Size-k min-heap | O(n log k) | Keep k largest via heap top |
| Merge K Sorted Lists | Priority queue | O(N log k) | Pop smallest across k heads |
| Top K Frequent Elements | Heap on frequencies | O(n log k) | Count then heap-select |
| Find Median from Data Stream (concept) | Two heaps | O(log n) per add | Max-heap left + min-heap right |

---

## Implementations

- **Python:** [`solutions.py`](./solutions.py) — `MinHeap`, `find_kth_largest`, `merge_k_sorted_lists`
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Trees](../trees/README.md) — heaps are specialized trees
- [Sorting](../../algorithms/sorting/README.md) — heap sort uses heap structure
- [Graphs](../graphs/README.md) — Dijkstra uses a priority queue
