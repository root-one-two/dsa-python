# Greedy Algorithms

A **greedy algorithm** builds a solution step by step, always picking the locally best option. It never backtracks. When the **greedy choice property** and **optimal substructure** hold, this yields a globally optimal solution in O(n) or O(n log n) time.

---

## ASCII: Interval Scheduling (Earliest Finish First)

```text
Timeline:  |----A----|
           |--B--|
                |-----C-----|
           pick B (ends earliest) → leaves room for C
```

Sort by end time; greedily take non-overlapping intervals.

---

## Features

- **Greedy choice property** — local optimum leads to global optimum
- **Optimal substructure** — optimal solution contains optimal sub-solutions
- **Single pass / irreversible** — fast but problem-specific

---

## Pros & Cons

| Aspect | Pros | Cons |
|:---|:---|:---|
| Performance | O(n)–O(n log n); low memory | Only works with proof of correctness |
| Design | Simple, intuitive logic | Fails on general knapsack / arbitrary coin change |

---

## When to Use

- Provable greedy problems: interval scheduling, Huffman coding, MST, Dijkstra
- Fast approximation for some NP-hard problems

**Avoid when:** Future choices depend on complex accumulated state.

**Pattern cues:** "maximum jumps", "gas station", "task scheduler", "candy", "non-overlapping intervals" → greedy.

---

## Top 5 Essential Problems

| Problem | Pattern | Complexity | Focus |
|:---|:---|:---|:---|
| Jump Game I & II | Furthest reach | O(n) time | Track `max_reach` and jump boundaries |
| Gas Station | Running tank reset | O(n) time | Reset start when tank < 0 |
| Task Scheduler | Frequency bottleneck | O(n) time | Idle slots from max frequency |
| Candy | Two-pass greedy | O(n) time | Left pass then right pass |
| Non-overlapping Intervals | Earliest finish first | O(n log n) | Sort by end; minimize removals |

---

## Implementations

- **Python:** [`solutions.py`](./solutions.py)
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Sorting](../sorting/README.md) — many greedy algorithms sort first
- [Dynamic Programming](../dynamic_programming/README.md) — when greedy fails (0/1 knapsack)
- [Arrays](../../data_structures/arrays/README.md) — Jump Game and Gas Station are array sweeps
