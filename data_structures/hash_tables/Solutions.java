import java.util.*;

/** Hash Tables — Chaining Hash Map & Essential Patterns. */
public class Solutions {

    /** Hash map with chaining collision resolution. Average O(1) operations. */
    public static class HashMap<K, V> {
        private final int capacity;
        private final List<List<Map.Entry<K, V>>> buckets;
        private int size;

        @SuppressWarnings("unchecked")
        public HashMap(int capacity) {
            this.capacity = capacity;
            this.buckets = new ArrayList<>();
            for (int i = 0; i < capacity; i++) buckets.add(new ArrayList<>());
        }

        public HashMap() { this(16); }

        private int hash(K key) {
            return Math.floorMod(key.hashCode(), capacity);
        }

        public void put(K key, V value) {
            int idx = hash(key);
            for (int i = 0; i < buckets.get(idx).size(); i++) {
                if (buckets.get(idx).get(i).getKey().equals(key)) {
                    buckets.get(idx).set(i, Map.entry(key, value));
                    return;
                }
            }
            buckets.get(idx).add(Map.entry(key, value));
            size++;
        }

        public V get(K key) {
            for (Map.Entry<K, V> entry : buckets.get(hash(key))) {
                if (entry.getKey().equals(key)) return entry.getValue();
            }
            return null;
        }

        public boolean remove(K key) {
            List<Map.Entry<K, V>> bucket = buckets.get(hash(key));
            for (int i = 0; i < bucket.size(); i++) {
                if (bucket.get(i).getKey().equals(key)) {
                    bucket.remove(i);
                    size--;
                    return true;
                }
            }
            return false;
        }

        public int size() { return size; }
    }

    /** Group strings by sorted character signature. O(n * k log k). */
    public static List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> groups = new HashMap<>();
        for (String s : strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);
            groups.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(groups.values());
    }

    /** Top K frequent elements using hash map + bucket sort. O(n) average. */
    public static int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int num : nums) count.merge(num, 1, Integer::sum);
        List<Integer>[] buckets = new List[nums.length + 1];
        for (int i = 0; i <= nums.length; i++) buckets[i] = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            buckets[entry.getValue()].add(entry.getKey());
        }
        int[] result = new int[k];
        int idx = 0;
        for (int i = buckets.length - 1; i >= 0 && idx < k; i--) {
            for (int num : buckets[i]) {
                result[idx++] = num;
                if (idx == k) return result;
            }
        }
        return result;
    }

    /** Duplicate detection using a hash set. O(n) time. */
    public static boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (!seen.add(num)) return true;
        }
        return false;
    }
}
