# Linked Lists

## What It Is

A **linked list** is a linear structure of **nodes** linked by pointers. Each node holds data and a reference to the next node (singly linked), optionally to the previous node (doubly linked). Nodes are **not** stored in contiguous memory.

---

## ASCII: Singly Linked List

```text
  head
   │
   ▼
┌──────┬───┐   ┌──────┬───┐   ┌──────┬───┐
│  3   │ ●─┼──►│  7   │ ●─┼──►│  11  │ ∅ │
└──────┴───┘   └──────┴───┘   └──────┴───┘
  data next      data next      data next
```

---

## Complexity

| Operation | Time | Space | Notes |
|:---|:---|:---|:---|
| Access by index | O(n) | O(1) | Must traverse |
| Search | O(n) | O(1) | Sequential scan |
| Insert / delete (known node) | O(1) | O(1) | Pointer rewiring |
| Insert / delete (by index) | O(n) | O(1) | Find node first |

---

## Pros & Cons

**Pros**

- O(1) insert/delete when you hold a pointer to the node
- Dynamic size without upfront allocation or full-array copy

**Cons**

- No O(1) random access
- Extra memory per node for pointers; poor cache locality

---

## When to Use

- Frequent insert/delete at head or middle
- Unknown or fluctuating dataset size
- No need for index-based access

**Pattern cues:** "reverse list", "cycle", "merge sorted lists", "k-th from end" → pointer manipulation and fast/slow pointers.

---

## Top 5 Essential Problems

| Problem | Pattern | Complexity | Focus |
|:---|:---|:---|:---|
| Reverse Linked List | Pointer reversal | O(n) time, O(1) space | `prev`, `curr`, `next` iteration |
| Linked List Cycle | Fast & slow pointers | O(n) time, O(1) space | Floyd's tortoise and hare |
| Merge Two Sorted Lists | Dummy head | O(n) time, O(1) space | Two-pointer merge with sentinel |
| Remove N-th Node From End | Offset two pointers | O(n) time, O(1) space | Lead pointer N steps ahead |
| Intersection of Two Lists | Path alignment | O(n) time, O(1) space | Switch lists when path ends |

---

## Implementations

- **Python:** [`solutions.py`](./solutions.py) — includes `ListNode` helper class
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Arrays](../arrays/README.md) — contrast contiguous vs. linked memory
- [Stacks & Queues](../stacks_queues/README.md) — often implemented with linked nodes
- [Trees](../trees/README.md) — hierarchical extension of linked nodes
