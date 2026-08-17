# Union-Find (Disjoint Set)

> **Before you read this:** Comfortable with [graphs](../graphs/README.md). Union-Find answers "are these two nodes in the same group?" while you **merge groups** over time.

---

## In Plain English

Start with **n people, each in their own group**.

- **Find** — which group is this person in?
- **Union** — merge two groups into one (they become friends, or a road connects two cities).

After a series of unions, you can ask: "Are A and B already connected?" without walking a full graph each time.

The structure is also called a **disjoint-set** — groups never overlap.

---

## Real-World Examples

- **Friend circles** — if A knows B and B knows C, A, B, and C are one circle (Number of Provinces).
- **Building a network** — add cables; reject a cable that would loop (already connected).
- **Maze / Kruskal's MST** (concept) — add cheapest edges that don't form a cycle.
- **Equality equations** — `a==b` and `b==c` put a, b, c together; `a!=c` then is a contradiction.

---

## Key Ideas

| Term | Simple definition | Example |
|:---|:---|:---|
| **Parent** | Each node points toward its group representative | 3 → 1 → 1 (1 is the root) |
| **Find** | Follow parents to the root | "Who is the leader of 3?" |
| **Union** | Attach one root under another | Merge two friend circles |
| **Path compression** | After find, point nodes straight at the root | Flatten the chain for next time |
| **Union by rank** | Attach the smaller tree under the larger | Keeps trees shallow |
| **Component** | One group / one connected island | Count of remaining roots |

---

## How It Works

Four nodes, then `union(0,1)` and `union(2,3)`, then `union(1,2)`:

```text
Start:     0  1  2  3     (four groups)

union 0-1:  0     2  3
            ↑
            1

union 2-3:  0     2
            ↑     ↑
            1     3

union 1-2:  0
           / \
          1   2
              ↑
              3         one group; find(3) == find(0)
```

**Path compression:** `find(3)` walks 3 → 2 → 0, then sets `parent[3] = 0` so the next find is one hop.

<details>
<summary><strong>Go deeper — almost O(1)</strong></summary>

- With path compression **and** union by rank, a sequence of operations is effectively **almost O(1)** each (inverse Ackermann — slower than any practical log, treated as constant in interviews).
- Without those tricks, a skinny chain makes find O(n).
- Compared with DFS/BFS connected components: Union-Find shines when edges **arrive over time** or you must **reject cycles** while adding edges.
</details>

---

## What You Can Do With It

| Question | Approach |
|:---|:---|
| "How many separate groups?" | `n` unions, then count remaining components |
| "Would this edge create a cycle?" | `union` returns false if already same root |
| "Is this graph a tree?" | `n - 1` edges, every union succeeds, one component |
| "Are these equalities consistent?" | Union all `==`, then check `!=` pairs |

---

## Complexity (quick reference)

*n = nodes, m = union/find operations*

| Operation | Time (with both optimizations) |
|:---|:---|
| Find | ~O(1) amortized |
| Union | ~O(1) amortized |
| Space | O(n) parent (and rank) arrays |

---

## Common Interview Patterns

| When the problem says… | Think… |
|:---|:---|
| "Number of provinces / friend circles" | Union each connected pair, count components |
| "Redundant connection" / extra edge | First union that fails is the cycle edge |
| "Graph valid tree?" | n-1 edges + no cycle + one component |
| "Equations / equality" | Union equals, verify unequals |

---

## Practice Problems

| Problem | What it's really asking | Pattern |
|:---|:---|:---|
| Union-Find ADT | Find, union, connected | Path compression + rank |
| Number of Provinces | How many friend circles in a matrix? | Union all 1s |
| Graph Valid Tree | n nodes, given edges — is it a tree? | Cycle check + one component |
| Satisfiability of Equality Equations | Can `==` and `!=` all be true? | Union `==`, reject bad `!=` |

---

## Code

- **Python:** [`solutions.py`](./solutions.py)
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Graphs](../graphs/README.md) — DFS/BFS also count components; Union-Find is better for online merges
- [Trees](../trees/README.md) — a tree is a connected graph with no cycles
- [Heaps](../heaps/README.md) — Kruskal's MST pairs a heap (edge order) with Union-Find
