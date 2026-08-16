# Graphs

## What It Is

A **graph** is a set of **vertices (nodes)** connected by **edges**. Graphs can be **directed** or **undirected**, **weighted** or **unweighted**. Common representations:

- **Adjacency list** — compact for sparse graphs; O(V + E) space
- **Adjacency matrix** — O(V²) space; fast edge lookup

---

## ASCII: Directed Graph (Adjacency List)

```text
    0 ──► 1
    │     │
    ▼     ▼
    2 ──► 3

Adj list:  0 → [1, 2]
           1 → [3]
           2 → [3]
           3 → []
```

---

## Complexity

| Operation | Adjacency List | Notes |
|:---|:---|:---|
| Add vertex | O(1) | |
| Add edge | O(1) | |
| BFS / DFS | O(V + E) | Visit all nodes and edges |
| Space | O(V + E) | Matrix uses O(V²) |

---

## Pros & Cons

**Pros**

- Models networks, dependencies, and pathways accurately
- Rich algorithm toolbox: shortest path, topological sort, cycle detection

**Cons**

- Can be expensive on dense graphs
- Cycles, disconnected components, and edge state add complexity

---

## When to Use

- Social networks, road maps, recommendation graphs
- Dependency resolution (build systems, course prerequisites)
- Reachability, shortest path, and clustering problems

**Pattern cues:** "connected components", "shortest path", "course schedule", "islands" → graph BFS/DFS or topological sort.

---

## Top 5 Essential Problems

| Problem | Pattern | Complexity | Focus |
|:---|:---|:---|:---|
| Graph BFS / DFS | Adjacency traversal | O(V + E) | Foundation for all graph algorithms |
| Number of Islands | Grid DFS/BFS | O(M × N) | Flood-fill connected components |
| Course Schedule | Topological sort | O(V + E) | Detect cycles in dependency graph |
| Clone Graph | BFS + hash map | O(V + E) | Copy nodes while tracking visited |
| Word Ladder (concept) | BFS shortest path | O(V + E) | Transform words one letter at a time |

---

## Implementations

- **Python:** [`solutions.py`](./solutions.py) — `Graph` class, islands, course schedule
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Stacks & Queues](../stacks_queues/README.md) — BFS queue, DFS stack
- [Heaps](../heaps/README.md) — Dijkstra's algorithm uses a priority queue
- [Greedy](../../algorithms/greedy/README.md) — MST and shortest-path variants
