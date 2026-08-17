# Concurrency & Parallelism: From Sequential to Multithreaded

## In Plain English

In **sequential** code, one thing happens after another — predictable and easy to reason about.

In **multi-threaded** code, several tasks run **at the same time** (or overlap) and often **share the same data**. Without rules, they can **step on each other** — like two people editing the same document without seeing each other's changes.

This guide shows **what breaks** when you add threads, and **what built-in tools fix it**.

**Implementations:** [solutions.py](./solutions.py) · [Solutions.java](./Solutions.java) · [README](./README.md)

---

## What Breaks & How Languages Fix It

### 1. Race condition (shared counter)

**What breaks:** Two threads both run `count += 1`. Both read `5`, both write `6`. Correct answer should be `7`.

**Fix:** Only one thread at a time may update — **lock** — or use a **single atomic** hardware operation.

| Language | Tool |
|:---|:---|
| Python | `threading.Lock()` |
| Java | `synchronized` or `AtomicInteger` |

### 2. Unsafe collections

**What breaks:** Two threads modify a normal `list` / `ArrayList` at once → corrupted structure, crashes, or infinite loops.

**Fix:** Thread-safe collections.

| Language | Tool |
|:---|:---|
| Python | `queue.Queue` |
| Java | `ConcurrentHashMap`, `CopyOnWriteArrayList` |

### 3. Producer-consumer coordination

**What breaks:** Consumer loops `while list empty` — wastes CPU (**busy waiting**) or crashes on empty access.

**Fix:** **Blocking queue** — consumer **sleeps** until producer adds work.

| Language | Tool |
|:---|:---|
| Python | `queue.Queue.get()` blocks until `put()` |
| Java | `ArrayBlockingQueue.take()` blocks until `put()` |

---

## ASCII: Producer-Consumer

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
| Uses multiple CPU cores | Bugs are hard to reproduce |
| UI stays responsive during I/O | Too many threads → slowdown |
| Higher throughput for parallel work | Deadlocks can freeze the app |

---

## Built-in Solutions Comparison

| Problem | Sequential failure | Python | Java |
|:---|:---|:---|:---|
| Mutual exclusion | Corrupted shared data | `threading.Lock()` | `ReentrantLock` / `synchronized` |
| Atomic update | Lost increment | `threading.Lock()` | `AtomicInteger` |
| Safe queue | Busy wait / crash | `queue.Queue` | `ArrayBlockingQueue` |
| Concurrent map | Corrupted map | Lock on `dict` | `ConcurrentHashMap` |

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

- [Concurrency README](./README.md) — overview and practice topics
- [Stacks & Queues](../data_structures/stacks_queues/README.md) — queues in concurrent pipelines
