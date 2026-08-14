import java.util.*;

/** Recursion & Backtracking — Essential Problem Solutions. */
public class Solutions {

    /** Power Set — include/exclude decision tree. O(n * 2^n). */
    public static List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrackSubsets(nums, 0, new ArrayList<>(), result);
        return result;
    }

    private static void backtrackSubsets(int[] nums, int start, List<Integer> path,
                                         List<List<Integer>> result) {
        result.add(new ArrayList<>(path));
        for (int i = start; i < nums.length; i++) {
            path.add(nums[i]);
            backtrackSubsets(nums, i + 1, path, result);
            path.remove(path.size() - 1);
        }
    }

    /** All permutations via in-place swap backtracking. O(n * n!). */
    public static List<List<Integer>> permutations(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrackPermutations(nums, 0, result);
        return result;
    }

    private static void backtrackPermutations(int[] nums, int start,
                                              List<List<Integer>> result) {
        if (start == nums.length) {
            List<Integer> perm = new ArrayList<>();
            for (int n : nums) perm.add(n);
            result.add(perm);
            return;
        }
        for (int i = start; i < nums.length; i++) {
            swap(nums, start, i);
            backtrackPermutations(nums, start + 1, result);
            swap(nums, start, i);
        }
    }

    /** Combination Sum — backtrack with remaining target reduction. */
    public static List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> result = new ArrayList<>();
        backtrackCombination(candidates, 0, target, new ArrayList<>(), result);
        return result;
    }

    private static void backtrackCombination(int[] candidates, int start, int remaining,
                                             List<Integer> path, List<List<Integer>> result) {
        if (remaining == 0) {
            result.add(new ArrayList<>(path));
            return;
        }
        for (int i = start; i < candidates.length; i++) {
            if (candidates[i] > remaining) break;
            path.add(candidates[i]);
            backtrackCombination(candidates, i, remaining - candidates[i], path, result);
            path.remove(path.size() - 1);
        }
    }

    /** N-Queens — constraint propagation with diagonal tracking. */
    public static List<List<String>> solveNQueens(int n) {
        List<List<String>> result = new ArrayList<>();
        char[][] board = new char[n][n];
        for (char[] row : board) Arrays.fill(row, '.');
        backtrackNQueens(0, n, board, new HashSet<>(), new HashSet<>(), new HashSet<>(), result);
        return result;
    }

    private static void backtrackNQueens(int row, int n, char[][] board,
                                         Set<Integer> cols, Set<Integer> posDiag,
                                         Set<Integer> negDiag, List<List<String>> result) {
        if (row == n) {
            List<String> snapshot = new ArrayList<>();
            for (char[] r : board) snapshot.add(new String(r));
            result.add(snapshot);
            return;
        }
        for (int col = 0; col < n; col++) {
            if (cols.contains(col) || posDiag.contains(row + col) || negDiag.contains(row - col))
                continue;
            cols.add(col);
            posDiag.add(row + col);
            negDiag.add(row - col);
            board[row][col] = 'Q';
            backtrackNQueens(row + 1, n, board, cols, posDiag, negDiag, result);
            board[row][col] = '.';
            cols.remove(col);
            posDiag.remove(row + col);
            negDiag.remove(row - col);
        }
    }

    /** Word Search — 2D grid DFS with in-place state rollback. */
    public static boolean wordSearch(char[][] board, String word) {
        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[0].length; c++) {
                if (dfsWordSearch(board, word, r, c, 0)) return true;
            }
        }
        return false;
    }

    private static boolean dfsWordSearch(char[][] board, String word, int r, int c, int idx) {
        if (idx == word.length()) return true;
        if (r < 0 || r >= board.length || c < 0 || c >= board[0].length
                || board[r][c] != word.charAt(idx)) return false;
        char temp = board[r][c];
        board[r][c] = '#';
        boolean found = dfsWordSearch(board, word, r + 1, c, idx + 1)
                || dfsWordSearch(board, word, r - 1, c, idx + 1)
                || dfsWordSearch(board, word, r, c + 1, idx + 1)
                || dfsWordSearch(board, word, r, c - 1, idx + 1);
        board[r][c] = temp;
        return found;
    }

    private static void swap(int[] nums, int i, int j) {
        int tmp = nums[i]; nums[i] = nums[j]; nums[j] = tmp;
    }
}
