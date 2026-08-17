# Graphs

> **Before you read this:** Helpful to know [queues](../stacks_queues/README.md) (for BFS) and [stacks](../stacks_queues/README.md) (for DFS). [Trees](../trees/README.md) are a special case of graphs.

---

## In Plain English

A **graph** models **things connected to other things**.

- **Vertices (nodes)** = the things (cities, people, web pages).
- **Edges** = the connections (roads, friendships, links).

Unlike a tree, graphs can have **cycles** (you can return to where you started) and **multiple paths** between the same places.

---

## Real-World Examples

- **Road map** — cities connected by highways.
- **Social network** — people connected by friendships or follows.
- **Course prerequisites** — course A must be taken before course B.
- **Flight routes** — airports connected by flights (with prices = weights).

---

## Key Ideas

| Term | Simple definition | Real example |
|:---|:---|:---|
| **Vertex (node)** | A point in the graph | A city, user, or course |
| **Edge** | A connection between two vertices | A road, friendship, prerequisite |
| **Undirected** | Connection works both ways | Facebook friend: A↔B |
| **Directed** | Connection is one-way only | Twitter: A follows B ≠ B follows A |
| **Weighted** | Edge has a cost or distance | Road length in km, flight price |
| **Unweighted** | All edges equal — only care if connected | Maze: can I reach the exit? |
| **Path** | Sequence of edges from A to B | Route from home to school |
| **Cycle** | Path that returns to start | Round-trip that loops back |
| **Connected** | Every node reachable from every other | One island of land vs. separate islands |

### Directed vs undirected — side by side

```text
UNDIRECTED (friendship)     DIRECTED (follow / prerequisite)
    A ─── B                     A ──► B
    (both connected)            (A → B only)

WEIGHTED (distance)         UNWEIGHTED (exists or not)
    A ──5── B                   A ─── B
    (cost matters)              (just "linked" or not)
```

---

## How It Works

**Directed graph** — arrows show allowed direction:

```text
    0 ──► 1
    │     │
    ▼     ▼
    2 ──► 3

Meaning: 0 can go to 1 and 2; 1 can go to 3; 2 can go to 3; 3 has no outgoing edges.
```

**Adjacency list** — each node keeps a list of neighbors (who it connects to):

```text
0 → [1, 2]
1 → [3]
2 → [3]
3 → []
```

Think: each city keeps a list of cities you can drive to directly.

<details>
<summary><strong>Go deeper — adjacency matrix & sparse graphs</strong></summary>

- **Adjacency matrix:** A table where row i, column j is 1 (or weight) if i connects to j. Fast "is A connected to B?" but uses O(V²) space.
- **Sparse graph:** Few edges relative to all possible pairs — adjacency list is usually better.
- **V and E:** V = number of vertices (nodes), E = number of edges (connections).
</details>

---

## What You Can Do With It

| Question | Typical approach |
|:---|:---|
| "Can I reach B from A?" | BFS or DFS |
| "Shortest path (fewest steps)?" | BFS on unweighted graph |
| "Cheapest route?" | Weighted shortest path (Dijkstra — uses a [heap](../heaps/README.md)) |
| "Can I finish all courses?" | Detect cycle in directed graph |
| "How many separate groups?" | Count connected components |

---

## Complexity (quick reference)

*V = vertices (nodes), E = edges (connections)*

| Operation | Adjacency list | Notes |
|:---|:---|:---|
| Add vertex | O(1) | |
| Add edge | O(1) | |
| BFS / DFS | O(V + E) | Visit each node and edge once |
| Space | O(V + E) | Matrix uses O(V²) |

---

## Common Interview Patterns

| When the problem says… | Think… |
|:---|:---|
| "Connected components" / "islands" | Flood-fill DFS/BFS on grid |
| "Shortest path" (unweighted) | BFS |
| "Course schedule" / prerequisites | Directed graph + cycle check |
| "Clone / copy graph" | BFS + map old node → new node |
| "Word ladder" | BFS on implicit graph of words |

---

## Practice Problems

| Problem | What it's really asking | Pattern |
|:---|:---|:---|
| Graph BFS / DFS | Walk the whole network | Foundation traversal |
| Number of Islands | How many separate groups of land? | Grid flood-fill |
| Course Schedule | Can prerequisites be satisfied without deadlock? | Cycle detection |
| Clone Graph | Copy entire structure with same links | BFS + hash map |
| Word Ladder (concept) | Fewest letter changes to reach target word | BFS shortest path |

---

## Code

- **Python:** [`solutions.py`](./solutions.py)
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Stacks & Queues](../stacks_queues/README.md) — BFS queue, DFS stack
- [Heaps](../heaps/README.md) — priority in shortest-path algorithms
- [Trees](../trees/README.md) — graph with no cycles and one root
