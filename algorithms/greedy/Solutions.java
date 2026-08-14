import java.util.*;

/** Greedy Algorithms — Essential Problem Solutions. */
public class Solutions {

    /** Jump Game I — furthest reachable index tracking. O(n) time. */
    public static boolean canJump(int[] nums) {
        int maxReach = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > maxReach) return false;
            maxReach = Math.max(maxReach, i + nums[i]);
        }
        return true;
    }

    /** Jump Game II — minimum jumps to reach end. O(n) time. */
    public static int jump(int[] nums) {
        int jumps = 0, currentEnd = 0, farthest = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            farthest = Math.max(farthest, i + nums[i]);
            if (i == currentEnd) {
                jumps++;
                currentEnd = farthest;
            }
        }
        return jumps;
    }

    /** Gas Station — running deficit & reset sweep. O(n) time. */
    public static int canCompleteCircuit(int[] gas, int[] cost) {
        int totalGas = 0, totalCost = 0, tank = 0, start = 0;
        for (int i = 0; i < gas.length; i++) {
            totalGas += gas[i];
            totalCost += cost[i];
            tank += gas[i] - cost[i];
            if (tank < 0) {
                start = i + 1;
                tank = 0;
            }
        }
        return totalGas >= totalCost ? start : -1;
    }

    /** Task Scheduler — frequency bottleneck math. O(n) time. */
    public static int leastInterval(char[] tasks, int n) {
        int[] count = new int[26];
        for (char task : tasks) count[task - 'A']++;
        Arrays.sort(count);
        int maxFreq = count[25];
        int maxCount = 0;
        for (int c : count) if (c == maxFreq) maxCount++;
        int partCount = maxFreq - 1;
        int partLength = n + 1;
        int emptySlots = partCount * partLength;
        int available = tasks.length - maxFreq * maxCount;
        int idle = Math.max(0, emptySlots - available);
        return tasks.length + idle;
    }

    /** Candy — two-way pass (left-to-right & right-to-left). O(n) time. */
    public static int candy(int[] ratings) {
        int n = ratings.length;
        int[] candies = new int[n];
        Arrays.fill(candies, 1);
        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1]) candies[i] = candies[i - 1] + 1;
        }
        for (int i = n - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1])
                candies[i] = Math.max(candies[i], candies[i + 1] + 1);
        }
        return Arrays.stream(candies).sum();
    }

    /** Non-overlapping Intervals — earliest deadline first. O(n log n). */
    public static int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[1]));
        int count = 0;
        int prevEnd = Integer.MIN_VALUE;
        for (int[] interval : intervals) {
            if (interval[0] >= prevEnd) {
                prevEnd = interval[1];
            } else {
                count++;
            }
        }
        return count;
    }
}
