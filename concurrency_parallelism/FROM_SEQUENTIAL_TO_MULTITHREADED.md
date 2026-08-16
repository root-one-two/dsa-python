# Concurrency & Parallelism: From Sequential to Multithreaded

## Overview

In sequential code, operations run one after another in a deterministic order. In multi-threaded environments, threads run concurrently and compete for shared resources.

Without synchronization, sequential algorithms break due to **race conditions**, **memory visibility issues**, and **deadlocks**. This guide explains *why* single-threaded code fails under concurrency and *how* language primitives address it.

**Implementations:** [solutions.py](./solutions.py) · [Solutions.java](./Solutions.java)

---

## Sequential vs. Concurrent: What Breaks & How Languages Fix It

### 1. The Race Condition Problem (Shared Counter)

- **What breaks:** Two threads executing `count += 1` may read the same value and overwrite each other (lost update).
- **Fix:** Mutexes/locks or atomic operations.
  - **Python:** `threading.Lock()`
  - **Java:** `synchronized` or `AtomicInteger`

### 2. The Unsafe Collection Problem (Dynamic Resizing)

- **What breaks:** Concurrent writes to `list` / `ArrayList` or hash tables can corrupt internal structure.
- **Fix:** Thread-safe or lock-free collections.
  - **Python:** `queue.Queue`
  - **Java:** `ConcurrentHashMap`, `CopyOnWriteArrayList`

### 3. The Producer-Consumer Coordination Problem

- **What breaks:** Polling a list in a `while` loop wastes CPU (busy waiting) or raises index errors.
- **Fix:** Blocking queues that sleep consumers until work arrives.
  - **Python:** `queue.Queue` (`get()` blocks until `put()`)
  - **Java:** `ArrayBlockingQueue` (`take()` blocks until `put()`)

---

## ASCII: Producer-Consumer Flow

```text
  Producer Thread          Blocking Queue           Consumer Thread
  ───────────────         ──────────────          ───────────────
  put(task)  ──────────►  [ task-0 ]              take() ──► process
  put(task)  ──────────►  [ task-1 ]  (blocks     take() ──► process
  put(task)  ──────────►  [ task-2 ]   if full)   ...
```

---

## Pros & Cons of Multithreading

| Pros | Cons |
|:---|:---|
| Maximizes CPU utilization on multi-core hardware | Race conditions are hard to reproduce and debug |
| Keeps UI responsive during I/O | Context-switching overhead with too many threads |
| Higher throughput for independent tasks | Deadlocks can freeze the application |

---

## Built-in Solutions & Complexity

| Pattern | Sequential Failure | Python | Java | Complexity |
|:---|:---|:---|:---|:---|
| Mutual exclusion | Data corruption | `threading.Lock()` | `ReentrantLock` / `synchronized` | O(1) + wait time |
| Atomic updates | Lost updates | `threading.Lock()` | `AtomicInteger` | O(1) CAS |
| Safe queueing | Busy wait / corruption | `queue.Queue` | `ArrayBlockingQueue` | O(1) per op |
| Concurrent map | Pointer corruption | Lock on `dict` | `ConcurrentHashMap` | O(1) average |

---

## Code Walkthrough: Thread-Safe Counter

Two threads each increment a shared counter 100,000 times. Without synchronization the result is often below 200,000.

<details>
<summary>Python — safe counter with Lock</summary>

```python
import threading

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.value += 1

counter = Counter()
threads = [
    threading.Thread(target=lambda: [counter.increment() for _ in range(100000)])
    for _ in range(2)
]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(counter.value)  # 200000
```

</details>

<details>
<summary>Java — safe counter with AtomicInteger</summary>

```java
import java.util.concurrent.atomic.AtomicInteger;

public class ThreadSafeCounter {
    private static final AtomicInteger counter = new AtomicInteger(0);

    public static void main(String[] args) throws InterruptedException {
        Runnable task = () -> {
            for (int i = 0; i < 100000; i++) {
                counter.incrementAndGet();
            }
        };
        Thread t1 = new Thread(task);
        Thread t2 = new Thread(task);
        t1.start();
        t2.start();
        t1.join();
        t2.join();
        System.out.println(counter.get()); // 200000
    }
}
```

</details>

---

## Related Reading

- [Concurrency & Parallelism README](./README.md) — overview, use cases, and producer-consumer reference
- [Stacks & Queues](../data_structures/stacks_queues/README.md) — queues underpin many concurrent patterns
