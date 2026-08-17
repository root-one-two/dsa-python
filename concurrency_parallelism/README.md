# Concurrency & Parallelism

> **Before you read this:** Comfortable with [queues](../../data_structures/stacks_queues/README.md). Read [From Sequential to Multithreaded](./FROM_SEQUENTIAL_TO_MULTITHREADED.md) for why single-threaded code breaks.

---

## In Plain English

**Concurrency** means **multiple tasks in progress** — not necessarily at the exact same instant, but overlapping in time.

**Parallelism** means **multiple tasks actually running at the same time** (e.g. on different CPU cores).

When two threads **share the same variable or collection**, you need **rules** so they don't corrupt data — that's **thread safety**.

---

## Real-World Examples

- **Web server** — many HTTP requests handled by different worker threads.
- **Producer-consumer** — one thread produces tasks, another processes them ([queue](../../data_structures/stacks_queues/README.md)).
- **Bank account** — two ATMs withdrawing at once must not lose an update.
- **Game engine** — physics on one thread, rendering on another.

---

## Key Ideas

| Term | Simple definition | Example |
|:---|:---|:---|
| **Thread** | Independent flow of execution | One worker handling requests |
| **Race condition** | Two threads update same data; result depends on timing | Both read 5, both write 6 → should be 7 |
| **Lock / mutex** | Only one thread inside critical section | Bathroom key — one person at a time |
| **Atomic operation** | Update that hardware completes as one step | `AtomicInteger.increment()` |
| **Blocking queue** | Queue that waits when empty/full | Consumer sleeps until item arrives |
| **Producer-consumer** | One side adds work, other side processes | Task queue between threads |

---

## How It Works

**Race condition** — two threads increment `count`:

```text
Without lock:
  Thread A reads 5 → Thread B reads 5 → both write 6 → lost update

With lock:
  Thread A locks → reads 5 → writes 6 → unlocks
  Thread B locks → reads 6 → writes 7 → unlocks ✓
```

**Producer-consumer:**

```text
  Producer ──put()──►  [ queue ]  ──take()──► Consumer
              blocks if full              blocks if empty
```

<details>
<summary><strong>Go deeper — overhead & debugging</strong></summary>

| Primitive | Average time | Trade-off |
|:---|:---|:---|
| Mutex / lock | O(1) + wait | Simple; threads may block |
| Blocking queue | O(1) per op | Clean producer-consumer |
| Lock-free (CAS) | O(1) amortized | Complex; possible livelock |

Concurrent bugs are **non-deterministic** — hard to reproduce. Always test under contention.
</details>

---

## What You Can Do With It

| Need | Tool |
|:---|:---|
| Protect shared counter | `Lock` or `AtomicInteger` |
| Safe task handoff | `queue.Queue` / `ArrayBlockingQueue` |
| Many readers, few writers | `ConcurrentHashMap` (Java) |
| Limit parallel workers | Thread pool + bounded queue |

---

## Complexity (quick reference)

Logical operations stay O(1); real time includes **waiting** for locks and **context switching**.

---

## Common Patterns

| When the system needs… | Think… |
|:---|:---|
| Hand off tasks between threads | Producer-consumer queue |
| Safe increment of shared state | Lock or atomic |
| Multiple threads on same map | Concurrent hash map |
| "Why is my count wrong?" | Race condition demo |
| Pool of workers | Bounded queue + fixed threads |

---

## Practice Topics

| Topic | What it's really asking | Pattern |
|:---|:---|:---|
| Producer-Consumer | How do threads share work safely? | Blocking queue |
| Thread-Safe Counter | Why does `count += 1` fail? | Lock / atomic |
| Concurrent Hash Map (concept) | Safe parallel map access | Lock striping |
| Race Condition Demo | Lost update under concurrency | Mutual exclusion |
| Worker Pool (concept) | Bounded parallelism | Queue + thread pool |

---

## Code

- **Python:** [`solutions.py`](./solutions.py) — run with `python concurrency_parallelism/solutions.py`
- **Java:** [`Solutions.java`](./Solutions.java)

**Deep dive:** [From Sequential to Multithreaded](./FROM_SEQUENTIAL_TO_MULTITHREADED.md)

---

## Related Topics

- [Stacks & Queues](../../data_structures/stacks_queues/README.md) — FIFO queues underpin concurrent pipelines
- [Hash Tables](../../data_structures/hash_tables/README.md) — concurrent maps need special implementations
- [Graphs](../../data_structures/graphs/README.md) — parallel graph algorithms on multi-core CPUs
