# Concurrency & Parallelism in Data Structures

## What It Is

Concurrency and parallelism design data structures and algorithms for **safe simultaneous access** by multiple threads. Sequential structures assume one executor; concurrent structures manage race conditions, scheduling, and memory visibility to prevent corruption and deadlocks.

**Deep dive:** [From Sequential to Multithreaded](./FROM_SEQUENTIAL_TO_MULTITHREADED.md)

---

## ASCII: Threads Sharing a Resource

```text
   Thread 1 ──┐
   Thread 2 ──┼──►  [ Lock / Queue / Atomic ]  ──►  Shared State
   Thread 3 ──┘         (synchronization)            (safe access)
```

---

## Complexity

| Primitive / Structure | Average Time | Worst Case | Space | Sync Overhead |
|:---|:---|:---|:---|:---|
| Mutex / Lock | O(1) | O(1) + wait | O(1) | High (blocking) |
| Blocking Queue | O(1) | O(n) under contention | O(n) | Moderate |
| Lock-Free Queue (CAS) | O(1) amortized | Livelock risk | O(n) | Low (spin/retry) |

---

## Pros & Cons

| Pros | Cons |
|:---|:---|
| Multi-core utilization for heavy workloads | Race conditions, deadlocks, starvation |
| High throughput under parallel load | Lock overhead and context switching |
| Lock-free designs avoid priority inversion | Non-deterministic bugs; harder to test |

---

## When to Use

- Web servers and API gateways managing connection pools
- Database connection pools and in-memory caches (Redis-style architectures)
- Producer-consumer task pipelines (Kafka, Celery, job queues)
- OS schedulers and game-engine parallel subsystems

---

## Essential Hands-On Topics

| Topic | Pattern | Focus |
|:---|:---|:---|
| Producer-Consumer Queue | Blocking bounded queue | `put()`/`take()` coordinate work without busy waiting |
| Thread-Safe Counter | Mutual exclusion / atomics | Locks vs. `AtomicInteger` for read-modify-write |
| Concurrent Hash Map | Lock striping | Safe concurrent reads/writes without corrupting structure |
| Race Condition Demo | Lost update | Why `count += 1` is not atomic across threads |
| Worker Pool | Fixed thread set + shared queue | Bounded parallelism for request handling |

---

## Implementations

- **Python:** [`solutions.py`](./solutions.py) — producer-consumer with `queue.Queue` and `threading`
- **Java:** [`Solutions.java`](./Solutions.java) — producer-consumer with `ArrayBlockingQueue`

Run the Python demo:

```bash
python concurrency_parallelism/solutions.py
```

---

## Related Topics

- [Stacks & Queues](../data_structures/stacks_queues/README.md) — FIFO queues used in BFS and task buffering
- [Graphs](../data_structures/graphs/README.md) — parallel graph algorithms on multi-core systems
