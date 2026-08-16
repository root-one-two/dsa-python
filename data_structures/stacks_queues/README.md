# Stacks & Queues

## What It Is

- **Stack (LIFO):** Push and pop at the **same end** (top). Last in, first out.
- **Queue (FIFO):** Enqueue at the **rear**, dequeue from the **front**. First in, first out.

Both restrict access to endpoints — no arbitrary middle access without removing elements.

---

## ASCII: Stack vs Queue

```text
Stack (LIFO)          Queue (FIFO)
  push/pop here         dequeue here    enqueue here
       │                     │                │
       ▼                     ▼                ▼
    ┌─────┐              ┌─────┐  ──►  ┌─────┐  ──►  ┌─────┐
    │  3  │              │  1  │       │  2  │       │  3  │
    ├─────┤              └─────┘       └─────┘       └─────┘
    │  2  │
    ├─────┤
    │  1  │
    └─────┘
```

---

## Complexity

| Operation | Stack | Queue | Notes |
|:---|:---|:---|:---|
| Push / enqueue | O(1) | O(1) | Add at endpoint |
| Pop / dequeue | O(1) | O(1) | Remove from endpoint |
| Peek | O(1) | O(1) | View top/front |
| Search | O(n) | O(n) | Must pop/dequeue sequentially |

---

## Pros & Cons

**Pros**

- O(1) endpoint operations
- Enforces predictable ordering (call stacks, task queues, BFS/DFS)

**Cons**

- No random access to interior elements
- O(n) search

---

## When to Use

- **Stack:** Call stacks, undo/redo, balanced parentheses, DFS traversal
- **Queue:** Task scheduling, rate limiting, BFS traversal, producer-consumer buffering

**Pattern cues:** "valid parentheses", "next greater element", "BFS level order" → stack or queue.

---

## Top 5 Essential Problems

| Problem | Pattern | Complexity | Focus |
|:---|:---|:---|:---|
| Valid Parentheses | Stack matching | O(n) time | Push opens, pop on closes |
| Min Stack | Auxiliary stack | O(1) per op | Track running minimum |
| Implement Queue using Stacks | Two-stack amortization | O(1) amortized | `in` stack + `out` stack |
| Stack (core ADT) | LIFO implementation | O(1) push/pop | Foundation for DFS |
| Queue (core ADT) | FIFO implementation | O(1) enqueue/dequeue | Foundation for BFS |

---

## Implementations

- **Python:** [`solutions.py`](./solutions.py) — `Stack`, `Queue`, `MinStack`, `MyQueue`, `is_valid_parentheses`
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Graphs](../graphs/README.md) — BFS uses queues; DFS uses stacks
- [Trees](../trees/README.md) — level-order traversal uses a queue
- [Concurrency](../../concurrency_parallelism/README.md) — blocking queues for producer-consumer
