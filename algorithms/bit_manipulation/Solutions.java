/** Bit manipulation — set bits, XOR uniqueness, powers of two. */
public class Solutions {

    /** Number of 1 bits. O(number of set bits). */
    public static int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            n &= n - 1;
            count++;
        }
        return count;
    }

    /** Every value appears twice except one. XOR cancels pairs. O(n). */
    public static int singleNumber(int[] nums) {
        int unique = 0;
        for (int num : nums) unique ^= num;
        return unique;
    }

    /** True iff n is a positive power of two. O(1). */
    public static boolean isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }

    /** Missing value in 0..n where n = nums.length. XOR indices with values. */
    public static int missingNumber(int[] nums) {
        int missing = nums.length;
        for (int i = 0; i < nums.length; i++) {
            missing ^= i ^ nums[i];
        }
        return missing;
    }

    /** Reverse the lowest 32 bits. Treat n as unsigned. O(32). */
    public static int reverseBits(int n) {
        int result = 0;
        for (int i = 0; i < 32; i++) {
            result = (result << 1) | (n & 1);
            n >>>= 1;
        }
        return result;
    }
}
