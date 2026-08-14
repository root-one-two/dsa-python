import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;

/** Concurrency & Parallelism — Producer-Consumer Queue. */
public class Solutions {

    /** Thread-safe producer-consumer using a bounded blocking queue. */
    public static void runProducerConsumer(int numItems, int queueSize) throws InterruptedException {
        BlockingQueue<String> queue = new ArrayBlockingQueue<>(queueSize);

        Thread producer = new Thread(() -> {
            try {
                for (int i = 0; i < numItems; i++) {
                    String item = "task-" + i;
                    queue.put(item);
                    System.out.println("[Producer] Produced " + item);
                    Thread.sleep(100);
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        });

        Thread consumer = new Thread(() -> {
            try {
                for (int i = 0; i < numItems; i++) {
                    String item = queue.take();
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

    public static void main(String[] args) throws InterruptedException {
        runProducerConsumer(5, 5);
    }
}
