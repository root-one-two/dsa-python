"""Concurrency & Parallelism — Producer-Consumer Queue."""

import queue
import threading
import time
from typing import Callable


def run_producer_consumer(
    num_items: int = 5,
    queue_size: int = 5,
    on_produce: Callable[[str], None] | None = None,
    on_consume: Callable[[str], None] | None = None,
) -> None:
    """Thread-safe producer-consumer using a bounded blocking queue."""
    work_queue: queue.Queue[str] = queue.Queue(maxsize=queue_size)

    def producer() -> None:
        for i in range(num_items):
            item = f"task-{i}"
            work_queue.put(item)
            if on_produce:
                on_produce(item)
            else:
                print(f"[Producer] Produced {item}")
            time.sleep(0.1)

    def consumer() -> None:
        for _ in range(num_items):
            try:
                item = work_queue.get(timeout=2)
                if on_consume:
                    on_consume(item)
                else:
                    print(f"[Consumer] Processed {item}")
                work_queue.task_done()
            except queue.Empty:
                break

    t_producer = threading.Thread(target=producer)
    t_consumer = threading.Thread(target=consumer)
    t_producer.start()
    t_consumer.start()
    t_producer.join()
    t_consumer.join()


if __name__ == "__main__":
    run_producer_consumer()
