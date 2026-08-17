import java.util.*;

/** Union-Find — disjoint set with path compression and union by rank. */
public class Solutions {

    /** Disjoint set. Find/union are effectively O(1) amortized. */
    public static class UnionFind {
        private final int[] parent;
        private final int[] rank;
        private int components;

        public UnionFind(int n) {
            parent = new int[n];
            rank = new int[n];
            components = n;
            for (int i = 0; i < n; i++) parent[i] = i;
        }

        public int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }

        /** Merge groups. Returns false if a and b were already connected. */
        public boolean union(int a, int b) {
            int ra = find(a), rb = find(b);
            if (ra == rb) return false;
            if (rank[ra] < rank[rb]) {
                int tmp = ra;
                ra = rb;
                rb = tmp;
            }
            parent[rb] = ra;
            if (rank[ra] == rank[rb]) rank[ra]++;
            components--;
            return true;
        }

        public boolean connected(int a, int b) {
            return find(a) == find(b);
        }

        public int getComponents() {
            return components;
        }
    }

    /** Number of Provinces — friend circles in an n×n matrix. O(n²). */
    public static int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        UnionFind uf = new UnionFind(n);
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (isConnected[i][j] == 1) uf.union(i, j);
            }
        }
        return uf.getComponents();
    }

    /** Graph Valid Tree — n-1 edges, no cycle, one component. O(n). */
    public static boolean validTree(int n, int[][] edges) {
        if (edges.length != n - 1) return false;
        UnionFind uf = new UnionFind(n);
        for (int[] edge : edges) {
            if (!uf.union(edge[0], edge[1])) return false;
        }
        return uf.getComponents() == 1;
    }

    /** Satisfiability of Equality Equations over letters a–z. O(n). */
    public static boolean equationsPossible(String[] equations) {
        UnionFind uf = new UnionFind(26);
        for (String eq : equations) {
            if (eq.charAt(1) == '=') {
                uf.union(eq.charAt(0) - 'a', eq.charAt(3) - 'a');
            }
        }
        for (String eq : equations) {
            if (eq.charAt(1) == '!') {
                if (uf.connected(eq.charAt(0) - 'a', eq.charAt(3) - 'a')) return false;
            }
        }
        return true;
    }
}
