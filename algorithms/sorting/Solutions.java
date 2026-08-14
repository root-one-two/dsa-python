import java.util.*;

/** Sorting Algorithms — Essential Problem Solutions. */
public class Solutions {

    /** Stable divide-and-conquer sort. O(n log n) time, O(n) space. */
    public static int[] mergeSort(int[] arr) {
        if (arr.length <= 1) return arr;
        int mid = arr.length / 2;
        int[] left = mergeSort(Arrays.copyOfRange(arr, 0, mid));
        int[] right = mergeSort(Arrays.copyOfRange(arr, mid, arr.length));
        return merge(left, right);
    }

    private static int[] merge(int[] left, int[] right) {
        int[] result = new int[left.length + right.length];
        int i = 0, j = 0, k = 0;
        while (i < left.length && j < right.length) {
            result[k++] = (left[i] <= right[j]) ? left[i++] : right[j++];
        }
        while (i < left.length) result[k++] = left[i++];
        while (j < right.length) result[k++] = right[j++];
        return result;
    }

    /** Merge Intervals — sort by start, single-pass merge. O(n log n). */
    public static int[][] mergeIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        List<int[]> merged = new ArrayList<>();
        for (int[] interval : intervals) {
            if (!merged.isEmpty() && interval[0] <= merged.get(merged.size() - 1)[1]) {
                merged.get(merged.size() - 1)[1] =
                        Math.max(merged.get(merged.size() - 1)[1], interval[1]);
            } else {
                merged.add(interval);
            }
        }
        return merged.toArray(new int[0][]);
    }

    /** Kth Largest Element via Quickselect. O(n) average. */
    public static int findKthLargest(int[] nums, int k) {
        int target = nums.length - k;
        int lo = 0, hi = nums.length - 1;
        Random rand = new Random();
        while (lo <= hi) {
            int p = partition(nums, lo, hi, rand);
            if (p == target) return nums[p];
            if (p < target) lo = p + 1;
            else hi = p - 1;
        }
        return nums[lo];
    }

    private static int partition(int[] nums, int lo, int hi, Random rand) {
        int pivotIdx = lo + rand.nextInt(hi - lo + 1);
        swap(nums, pivotIdx, hi);
        int pivot = nums[hi], store = lo;
        for (int i = lo; i < hi; i++) {
            if (nums[i] <= pivot) swap(nums, store++, i);
        }
        swap(nums, store, hi);
        return store;
    }

    private static void swap(int[] nums, int i, int j) {
        int tmp = nums[i]; nums[i] = nums[j]; nums[j] = tmp;
    }

    /** Dutch National Flag — three-way in-place partition. O(n) time. */
    public static void sortColors(int[] nums) {
        int low = 0, mid = 0, high = nums.length - 1;
        while (mid <= high) {
            if (nums[mid] == 0) {
                swap(nums, low++, mid++);
            } else if (nums[mid] == 1) {
                mid++;
            } else {
                swap(nums, mid, high--);
            }
        }
    }

    /** Meeting Rooms II — sort starts/ends, two-pointer sweep. O(n log n). */
    public static int minMeetingRooms(int[][] intervals) {
        if (intervals.length == 0) return 0;
        int[] starts = new int[intervals.length];
        int[] ends = new int[intervals.length];
        for (int i = 0; i < intervals.length; i++) {
            starts[i] = intervals[i][0];
            ends[i] = intervals[i][1];
        }
        Arrays.sort(starts);
        Arrays.sort(ends);
        int rooms = 0, maxRooms = 0, s = 0, e = 0;
        while (s < starts.length) {
            if (starts[s] < ends[e]) {
                rooms++;
                maxRooms = Math.max(maxRooms, rooms);
                s++;
            } else {
                rooms--;
                e++;
            }
        }
        return maxRooms;
    }

    /** Custom Sort String — frequency map + bucket ordering. O(n + k). */
    public static String customSortString(String order, String s) {
        int[] count = new int[26];
        for (char ch : s.toCharArray()) count[ch - 'a']++;
        StringBuilder result = new StringBuilder();
        for (char ch : order.toCharArray()) {
            result.append(String.valueOf(ch).repeat(count[ch - 'a']));
            count[ch - 'a'] = 0;
        }
        for (int i = 0; i < 26; i++) {
            result.append(String.valueOf((char) ('a' + i)).repeat(count[i]));
        }
        return result.toString();
    }
}
