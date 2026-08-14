import java.util.*;

/** Graphs — Adjacency List, BFS, and DFS Implementations. */
public class Solutions {

    /** Undirected graph using adjacency list representation. */
    public static class Graph {
        private final Map<Integer, List<Integer>> adj = new HashMap<>();

        public Graph(int n) {
            for (int i = 0; i < n; i++) adj.put(i, new ArrayList<>());
        }

        public void addEdge(int u, int v) {
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        /** Breadth-First Search using a queue. O(V + E) time. */
        public List<Integer> bfs(int start) {
            Set<Integer> visited = new HashSet<>();
            List<Integer> order = new ArrayList<>();
            Queue<Integer> queue = new ArrayDeque<>();
            queue.add(start);
            visited.add(start);
            while (!queue.isEmpty()) {
                int node = queue.poll();
                order.add(node);
                for (int neighbor : adj.get(node)) {
                    if (!visited.contains(neighbor)) {
                        visited.add(neighbor);
                        queue.add(neighbor);
                    }
                }
            }
            return order;
        }

        /** Depth-First Search using a stack. O(V + E) time. */
        public List<Integer> dfs(int start) {
            Set<Integer> visited = new HashSet<>();
            List<Integer> order = new ArrayList<>();
            Deque<Integer> stack = new ArrayDeque<>();
            stack.push(start);
            while (!stack.isEmpty()) {
                int node = stack.pop();
                if (visited.contains(node)) continue;
                visited.add(node);
                order.add(node);
                List<Integer> neighbors = adj.get(node);
                for (int i = neighbors.size() - 1; i >= 0; i--) {
                    int neighbor = neighbors.get(i);
                    if (!visited.contains(neighbor)) stack.push(neighbor);
                }
            }
            return order;
        }
    }

    /** Count connected components in a 2D grid. O(M * N) time. */
    public static int numIslands(char[][] grid) {
        if (grid.length == 0) return 0;
        int rows = grid.length, cols = grid[0].length, count = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1') {
                    dfsIsland(grid, r, c);
                    count++;
                }
            }
        }
        return count;
    }

    private static void dfsIsland(char[][] grid, int r, int c) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] != '1') return;
        grid[r][c] = '0';
        dfsIsland(grid, r + 1, c);
        dfsIsland(grid, r - 1, c);
        dfsIsland(grid, r, c + 1);
        dfsIsland(grid, r, c - 1);
    }

    /** Course Schedule — cycle detection via topological sort. O(V + E). */
    public static boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        int[] indegree = new int[numCourses];
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
        for (int[] prereq : prerequisites) {
            adj.get(prereq[1]).add(prereq[0]);
            indegree[prereq[0]]++;
        }
        Queue<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) queue.add(i);
        }
        int visited = 0;
        while (!queue.isEmpty()) {
            int node = queue.poll();
            visited++;
            for (int neighbor : adj.get(node)) {
                if (--indegree[neighbor] == 0) queue.add(neighbor);
            }
        }
        return visited == numCourses;
    }
}
