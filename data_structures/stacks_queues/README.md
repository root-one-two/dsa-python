# Stacks & Queues

> **Before you read this:** Comfortable with [arrays](../arrays/README.md) or [linked lists](../linked_lists/README.md).

---

## In Plain English

A **stack** is like a **stack of plates** — you add and remove only from the **top** (Last In, First Out — **LIFO**).

A **queue** is like a **line at a ticket counter** — newcomers join at the **back**, service happens at the **front** (First In, First Out — **FIFO**).

Neither lets you grab an item from the middle without removing items around it.

---

## Real-World Examples

- **Stack:** Undo button in a text editor (last action reversed first).
- **Stack:** Matching parentheses `()` — open on stack, pop when closed.
- **Queue:** Printer job queue — first document sent prints first.
- **Queue:** People waiting in line — BFS explores graph "level by level" using a queue.

---

## Key Ideas

| Term | Simple definition | Example |
|:---|:---|:---|
| **Stack (LIFO)** | Last added is first removed | Plate stack |
| **Queue (FIFO)** | First added is first removed | Ticket line |
| **Push** | Add to stack top | `stack.push(5)` |
| **Pop** | Remove from stack top | `stack.pop()` |
| **Enqueue** | Add to queue rear | `queue.enqueue(5)` |
| **Dequeue** | Remove from queue front | `queue.dequeue()` |

---

## How It Works

```text
STACK (LIFO)              QUEUE (FIFO)
  push/pop here           dequeue ◄── front    back ──► enqueue
       │                    ┌───┬───┬───┐
    ┌─────┐                 │ 1 │ 2 │ 3 │
    │  3  │ ← top           └───┴───┴───┘
    ├─────┤
    │  2  │
    ├─────┤
    │  1  │
    └─────┘
```

**Valid parentheses** with a stack:

```text
"( ) [ ] { }"  → push opens, pop when close matches
"( ]"          → mismatch → invalid
```

---

## What You Can Do With It

| Structure | Best for… |
|:---|:---|
| **Stack** | Undo/redo, DFS, parsing nested structures |
| **Queue** | BFS, task scheduling, buffering |
| **Min stack** | Stack that also tracks current minimum in O(1) |
| **Queue via two stacks** | Simulate queue using stack operations |

---

## Complexity (quick reference)

*n = number of items*

| Operation | Stack | Queue |
|:---|:---|:---|
| Add | O(1) push | O(1) enqueue |
| Remove | O(1) pop | O(1) dequeue |
| Peek top/front | O(1) | O(1) |
| Search | O(n) | O(n) |

---

## Common Interview Patterns

| When the problem says… | Think… |
|:---|:---|
| "Valid parentheses" | Stack of open brackets |
| "Next greater element" | Monotonic stack |
| "Implement queue using stacks" | Two stacks (`in` / `out`) |
| "Level order traversal" | Queue (see [Trees](../trees/README.md)) |
| "BFS shortest path" | Queue (see [Graphs](../graphs/README.md)) |

---

## Practice Problems

| Problem | What it's really asking | Pattern |
|:---|:---|:---|
| Valid Parentheses | Are brackets properly nested? | Stack matching |
| Min Stack | Stack with O(1) minimum | Auxiliary stack |
| Implement Queue using Stacks | Queue behavior from stacks only | Two-stack transfer |
| Stack (ADT) | Core LIFO operations | Foundation |
| Queue (ADT) | Core FIFO operations | Foundation |

---

## Code

- **Python:** [`solutions.py`](./solutions.py)
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Graphs](../graphs/README.md) — BFS uses queue, DFS uses stack
- [Trees](../trees/README.md) — level-order uses queue
- [Concurrency](../../concurrency_parallelism/README.md) — blocking queues for threads
