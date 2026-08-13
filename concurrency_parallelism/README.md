# Concurrency & Parallelism in Data Structures

## 📌 Overview & Core Features
Concurrency and parallelism involve designing data structures and algorithms that can be safely accessed and modified by multiple execution threads simultaneously. While sequential data structures assume single-threaded execution, concurrent data structures manage race conditions, thread scheduling, and memory visibility to prevent data corruption and deadlocks.

### Key Features
* **Thread Safety:** Guarantees structural integrity under concurrent access using locks or atomic instructions.
* **Synchronization & Lock-Free Design:** Utilizes synchronization primitives (e.g., Mutexes, Semaphores) or hardware-level atomic operations (e.g., Compare-And-Swap/CAS).
* **High Throughput:** Minimizes thread contention to maximize parallel instruction execution across CPU cores.

---

## ⚖️ Pros & Cons

| Pros (Advantages) 🟢 | Cons (Disadvantages) 🔴 |
| :--- | :--- |
| **Multi-Core Utilization:** Fully leverages modern multi-core processors for heavy workloads. | **Implementation Complexity:** Susceptible to race conditions, deadlocks, livelocks, and thread starvation. |
| **Improved Scalability:** High throughput under heavy parallel read/write demands. | **Synchronization Overhead:** Locking mechanisms introduce overhead and context-switching costs. |
| **Non-blocking Operations:** Lock-free structures avoid thread blocking, preventing priority inversion. | **Difficult Debugging:** Heavier memory footprints and non-deterministic behavior make testing hard. |

---

## 🚀 Top 5 Real-World Applications & Use Cases

1. **Web Servers & API Gateways:** Managing incoming connection pools and thread workers (e.g., Netty, Tokio, Nginx).
2. **Database Connection Pools & Caching:** Thread-safe memory caches and shared state pools (e.g., Redis internal architecture, HikariCP).
3. **Producer-Consumer Queues:** Asynchronous task processing across distributed or multithreaded systems (e.g., Kafka consumers, Celery workers).
4. **Operating System Schedulers:** Managing thread execution queues and process synchronization primitives in OS kernels.
5. **Game Engine Systems:** Parallel rendering, physics calculations, and state synchronization across engine components.

---

## ⏱️ Complexity Analysis

| Primitive / Structure | Average Time Complexity | Worst Case Complexity | Space Complexity | Synchronization Overhead |
| :--- | :--- | :--- | :--- | :--- |
| **Mutex / Lock Guard** | $O(1)$ | $O(1)$ (plus waiting time) | $O(1)$ | High (Thread Blocking) |
| **Concurrent Queue (Blocking)** | $O(1)$ | $O(n)$ (under extreme contention) | $O(n)$ | Moderate |
| **Lock-Free Queue (CAS)** | $O(1)$ amortized | $O(\infty)$ (Livelock potential) | $O(n)$ | Low (Spin/Retry) |

---

## 💻 Implementations

<details>
<summary>Solution (Producer-Consumer Queue)</summary>

```python
import queue
import threading
import time

# Thread-safe Queue handling producer-consumer synchronization
work_queue = queue.Queue(maxsize=5)

def producer():
    for i in range(5):
        item = f"task-{i}"
        work_queue.put(item)  # Blocks if queue is full
        print(f"[Producer] Produced {item}")
        time.sleep(0.1)

def consumer():
    while True:
        try:
            item = work_queue.get(timeout=1)  # Blocks if queue is empty
            print(f"[Consumer] Processed {item}")
            work_queue.task_done()
        except queue.Empty:
            break

# Start threads
t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()
t1.join()
t2.join()

``` java 
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;

public class ConcurrentQueueExample {
    public static void main(String[] args) throws InterruptedException {
        // Thread-safe bounded blocking queue powered by ReentrantLocks
        BlockingQueue<String> queue = new ArrayBlockingQueue<>(5);

        Thread producer = new Thread(() -> {
            try {
                for (int i = 0; i < 5; i++) {
                    String item = "task-" + i;
                    queue.put(item); // Blocks if queue is full
                    System.out.println("[Producer] Produced " + item);
                    Thread.sleep(100);
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });

        Thread consumer = new Thread(() -> {
            try {
                for (int i = 0; i < 5; i++) {
                    String item = queue.take(); // Blocks if queue is empty
                    System.out.println("[Consumer] Processed " + item);
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });

        producer.start();
        consumer.start();
        producer.join();
        consumer.join();
    }
}