# Heaps & Priority Queues

> **Before you read this:** Comfortable with [trees](../trees/README.md) helps (a heap is tree-shaped), but you can start with the analogy below.

---

## In Plain English

A **priority queue** answers: **"Who is most important right now?"** — not "who arrived first" (that's a regular [queue](../stacks_queues/README.md)).

A **heap** is a common way to build a priority queue. It always keeps the **smallest** (min-heap) or **largest** (max-heap) item at the top, ready to remove in one step.

Think of an **ER waiting room**: the most urgent patient is seen next, regardless of arrival order.

---

## Real-World Examples

- **Hospital triage** — critical cases first (priority queue).
- **Task scheduler** — highest-priority job runs next.
- **"Top K" problems** — keep track of the K largest numbers seen so far.
- **Dijkstra's shortest path** — always extend the cheapest known route next ([graphs](../graphs/README.md)).

---

## Key Ideas

| Term | Simple definition | Example |
|:---|:---|:---|
| **Priority queue** | Queue where importance beats arrival time | ER triage |
| **Min-heap** | Smallest value always at top | Always get minimum quickly |
| **Max-heap** | Largest value always at top | Always get maximum quickly |
| **Heap property** | Parent is ≤ children (min) or ≥ children (max) | Rule that keeps top correct |
| **Extract-min/max** | Remove and return top element | Serve highest-priority patient |
| **Binary heap** | Heap stored as a flat array | No pointer overhead |

---

## How It Works

**Min-heap as a tree** — parent is always smaller than children:

```text
        1          ← smallest (root) — always here
       / \
      3   2
     / \
    7   5
```

**Same heap as an array** `[1, 3, 2, 7, 5]`:

```text
index:  0   1   2   3   4
value: [1,  3,  2,  7,  5]
```

When you insert or remove, values **bubble** up or down to restore the heap rule.

<details>
<summary><strong>Go deeper — index formulas</strong></summary>

For index `i` in the array:

- Parent: `(i - 1) / 2`
- Left child: `2i + 1`
- Right child: `2i + 2`

Operations `sift_up` and `sift_down` swap with parent/child until the heap property holds — O(log n) per insert/extract.
</details>

---

## What You Can Do With It

| Action | Plain English |
|:---|:---|
| **Peek** | See min/max without removing |
| **Insert** | Add item; heap fixes itself |
| **Extract min/max** | Remove and return top priority item |
| **K-th largest** | Keep a heap of size K while scanning |

---

## Complexity (quick reference)

*n = number of items*

| Operation | Time | Notes |
|:---|:---|:---|
| Peek min/max | O(1) | Top of heap |
| Insert | O(log n) | Bubble up |
| Extract min/max | O(log n) | Bubble down |
| Find arbitrary element | O(n) | Not sorted for full scan |
| Build heap from array | O(n) | Bottom-up construction |

---

## Common Interview Patterns

| When the problem says… | Think… |
|:---|:---|
| "Kth largest / smallest" | Size-K heap |
| "Merge K sorted lists" | Heap of list heads |
| "Top K frequent" | Count then heap or bucket |
| "Median from stream" (concept) | Two heaps (max left, min right) |
| "Shortest path" (weighted) | Priority queue in Dijkstra |

---

## Practice Problems

| Problem | What it's really asking | Pattern |
|:---|:---|:---|
| Min-Heap (ADT) | Core insert/extract operations | `sift_up` / `sift_down` |
| Kth Largest Element | What's the Kth biggest number? | Size-K min-heap |
| Merge K Sorted Lists | Combine many sorted chains | Heap of smallest heads |
| Top K Frequent Elements | Which values appear most? | Frequency + heap |
| Median from Stream (concept) | Running median of incoming numbers | Two heaps |

---

## Code

- **Python:** [`solutions.py`](./solutions.py)
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Trees](../trees/README.md) — heap is a specialized tree shape
- [Graphs](../graphs/README.md) — Dijkstra uses a priority queue
- [Sorting](../../algorithms/sorting/README.md) — heap sort uses same structure
