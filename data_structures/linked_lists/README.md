# Linked Lists

> **Before you read this:** Comfortable with [arrays](../arrays/README.md) — linked lists are the alternative when you don't need index access.

---

## In Plain English

A **linked list** is a **chain of boxes** (nodes). Each box holds a **value** and a **pointer** to the next box. Unlike an array, the boxes are **not** in one continuous row in memory — they can be scattered, linked by pointers.

To reach item #5, you must start at the head and follow the chain — you cannot jump directly.

---

## Real-World Examples

- **Treasure hunt** — each clue points to the location of the next clue.
- **Browser back/forward** (doubly linked) — each page knows previous and next.
- **Music playlist** where you only have "next track" — no random jump to track 50.

---

## Key Ideas

| Term | Simple definition | Example |
|:---|:---|:---|
| **Node** | One box: value + pointer(s) | `(7) →` |
| **Head** | Pointer to the first node | Start of every traversal |
| **Singly linked** | Each node points only to next | One-way chain |
| **Doubly linked** | Node points to next and previous | Browser history |
| **Pointer reversal** | Change `next` to point backward | Reverse a list in place |
| **Fast/slow pointers** | Two pointers at different speeds | Detect a cycle |

---

## How It Works

```text
  head
   │
   ▼
┌──────┬───┐   ┌──────┬───┐   ┌──────┬───┐
│  3   │ ●─┼──►│  7   │ ●─┼──►│  11  │ ∅ │
└──────┴───┘   └──────┴───┘   └──────┴───┘
 value  next     value  next     value  next
```

**Fast/slow pointers** (cycle detection):

```text
slow moves 1 step, fast moves 2 steps
If they meet → there's a loop in the chain
```

---

## What You Can Do With It

| Action | Plain English |
|:---|:---|
| **Traverse** | Walk from head to end, one node at a time |
| **Insert after a node** | Rewire pointers — no shifting like arrays |
| **Delete a node** | Point previous node to skip the deleted one |
| **Reverse** | Flip each `next` pointer to point backward |

---

## Complexity (quick reference)

*n = number of nodes*

| Operation | Time | Notes |
|:---|:---|:---|
| Access by index | O(n) | Must walk the chain |
| Search | O(n) | Linear scan |
| Insert/delete (if you have the node) | O(1) | Just rewire pointers |
| Insert/delete by index | O(n) | Find position first |

<details>
<summary><strong>Go deeper — memory layout</strong></summary>

- **Pointer overhead:** Each node stores extra memory for the link(s).
- **Poor cache locality:** Nodes may live far apart in memory, so CPU cache is less helpful than with arrays.
</details>

---

## Common Interview Patterns

| When the problem says… | Think… |
|:---|:---|
| "Reverse linked list" | `prev`, `curr`, `next` walk |
| "Detect cycle" | Fast & slow pointers |
| "Merge two sorted lists" | Dummy head + two pointers |
| "Remove nth from end" | Two pointers with n-gap |
| "Find intersection" | Align path lengths, walk together |

---

## Practice Problems

| Problem | What it's really asking | Pattern |
|:---|:---|:---|
| Reverse Linked List | Flip the chain direction | Pointer reversal |
| Linked List Cycle | Is there a loop? | Floyd's algorithm |
| Merge Two Sorted Lists | Combine into one sorted chain | Dummy head |
| Remove Nth From End | Delete node n steps from tail | Offset pointers |
| Intersection of Two Lists | Where do two chains meet? | Path alignment |

---

## Code

- **Python:** [`solutions.py`](./solutions.py) — includes `ListNode` helper
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Arrays](../arrays/README.md) — contrast: index access vs. pointer walk
- [Stacks & Queues](../stacks_queues/README.md) — often built from linked nodes
- [Trees](../trees/README.md) — nodes with two children instead of one next link
