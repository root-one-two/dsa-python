import java.util.*;

/** Heaps & Priority Queues — Min-Heap Implementation. */
public class Solutions {

    /** Binary min-heap backed by a flat array. O(log n) insert/extract. */
    public static class MinHeap {
        private final List<Integer> heap = new ArrayList<>();

        public void push(int val) {
            heap.add(val);
            siftUp(heap.size() - 1);
        }

        public int pop() {
            if (heap.isEmpty()) throw new NoSuchElementException("pop from empty heap");
            swap(0, heap.size() - 1);
            int val = heap.remove(heap.size() - 1);
            if (!heap.isEmpty()) siftDown(0);
            return val;
        }

        public int peek() { return heap.get(0); }
        public int size() { return heap.size(); }

        private void siftUp(int idx) {
            while (idx > 0) {
                int parent = (idx - 1) / 2;
                if (heap.get(idx) >= heap.get(parent)) break;
                swap(idx, parent);
                idx = parent;
            }
        }

        private void siftDown(int idx) {
            int n = heap.size();
            while (true) {
                int smallest = idx;
                int left = 2 * idx + 1, right = 2 * idx + 2;
                if (left < n && heap.get(left) < heap.get(smallest)) smallest = left;
                if (right < n && heap.get(right) < heap.get(smallest)) smallest = right;
                if (smallest == idx) break;
                swap(idx, smallest);
                idx = smallest;
            }
        }

        private void swap(int i, int j) {
            int tmp = heap.get(i);
            heap.set(i, heap.get(j));
            heap.set(j, tmp);
        }
    }

    /** Find K-th largest element using a min-heap of size k. O(n log k). */
    public static int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int num : nums) {
            heap.offer(num);
            if (heap.size() > k) heap.poll();
        }
        return heap.peek();
    }

    /** Merge K sorted lists using a priority queue. O(N log k) time. */
    public static List<Integer> mergeKSortedLists(List<List<Integer>> lists) {
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        for (int i = 0; i < lists.size(); i++) {
            if (!lists.get(i).isEmpty()) {
                heap.offer(new int[]{lists.get(i).get(0), i, 0});
            }
        }
        List<Integer> result = new ArrayList<>();
        while (!heap.isEmpty()) {
            int[] curr = heap.poll();
            result.add(curr[0]);
            int listIdx = curr[1], elemIdx = curr[2];
            if (elemIdx + 1 < lists.get(listIdx).size()) {
                heap.offer(new int[]{lists.get(listIdx).get(elemIdx + 1), listIdx, elemIdx + 1});
            }
        }
        return result;
    }
}
