import java.util.*;

/** Trees & Binary Search Trees — Core Implementations. */
public class Solutions {

    public static class TreeNode {
        int val;
        TreeNode left, right;

        TreeNode() {}

        TreeNode(int val) { this.val = val; }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    /** Binary Search Tree with O(log n) average search/insert/delete. */
    public static class BST {
        TreeNode root;

        public void insert(int val) { root = insert(root, val); }

        private TreeNode insert(TreeNode node, int val) {
            if (node == null) return new TreeNode(val);
            if (val < node.val) node.left = insert(node.left, val);
            else if (val > node.val) node.right = insert(node.right, val);
            return node;
        }

        public boolean search(int val) { return search(root, val); }

        private boolean search(TreeNode node, int val) {
            if (node == null) return false;
            if (val == node.val) return true;
            return search(val < node.val ? node.left : node.right, val);
        }

        public void delete(int val) { root = delete(root, val); }

        private TreeNode delete(TreeNode node, int val) {
            if (node == null) return null;
            if (val < node.val) node.left = delete(node.left, val);
            else if (val > node.val) node.right = delete(node.right, val);
            else {
                if (node.left == null) return node.right;
                if (node.right == null) return node.left;
                TreeNode successor = node.right;
                while (successor.left != null) successor = successor.left;
                node.val = successor.val;
                node.right = delete(node.right, successor.val);
            }
            return node;
        }
    }

    /** In-order traversal yields sorted order for BST. O(n) time. */
    public static List<Integer> inorder(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        inorderDfs(root, result);
        return result;
    }

    private static void inorderDfs(TreeNode node, List<Integer> result) {
        if (node == null) return;
        inorderDfs(node.left, result);
        result.add(node.val);
        inorderDfs(node.right, result);
    }

    /** BFS level-order traversal. O(n) time. */
    public static List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;
        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                level.add(node.val);
                if (node.left != null) queue.add(node.left);
                if (node.right != null) queue.add(node.right);
            }
            result.add(level);
        }
        return result;
    }

    /** Maximum depth of a binary tree. O(n) time. */
    public static int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }

    /** Validate BST ordering constraint. O(n) time. */
    public static boolean isValidBST(TreeNode root) {
        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private static boolean isValidBST(TreeNode node, long low, long high) {
        if (node == null) return true;
        if (node.val <= low || node.val >= high) return false;
        return isValidBST(node.left, low, node.val)
                && isValidBST(node.right, node.val, high);
    }
}
