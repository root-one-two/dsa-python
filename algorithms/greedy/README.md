# Greedy Algorithms

> **Before you read this:** Comfortable with [arrays](../../data_structures/arrays/README.md) and [sorting](../sorting/README.md). Greedy often sorts first, then makes one pass.

---

## In Plain English

A **greedy algorithm** always picks the **best-looking option right now**, without reconsidering past choices.

If the problem is designed for greed, that local choice leads to the **global best answer**. Greedy is fast and simple — but it **does not work** for every problem (e.g. general 0/1 knapsack needs [DP](../dynamic_programming/README.md)).

---

## Real-World Examples

- **Interval scheduling** — pick the meeting that **ends earliest**, leave room for more meetings.
- **Jump game** — from each position, you only care how far you can reach.
- **Gas station loop** — if total gas ≥ total cost, a solution exists; find start by resetting when tank goes negative.
- **Handing out candy** — give minimum candy satisfying "more than neighbor if rating is higher."

---

## Key Ideas

| Term | Simple definition | Example |
|:---|:---|:---|
| **Greedy choice** | Pick best local option now | Earliest-ending meeting |
| **Optimal substructure** | Rest of solution is optimal too | After picking meeting, schedule rest optimally |
| **No backtracking** | Never undo a choice | Unlike backtracking |
| **Two-pass greedy** | Forward pass + backward pass | Candy problem |

---

## How It Works

**Non-overlapping intervals** — sort by **end time**, keep meetings that don't overlap:

```text
Sorted by end:  [1,2]  [2,3]  [3,5]
Pick [1,2] (ends at 2)
Skip [2,3] if it overlaps previous (start < 2)
Pick [3,5] if start ≥ 2 → maximum kept, minimum removed
```

**Jump game** — track furthest index reachable:

```text
Index:  0  1  2  3  4
Jump:   2  3  1  1  4
Reach:  0→2→4→...  can you reach last index?
```

<details>
<summary><strong>Go deeper — when greedy fails</strong></summary>

Greedy fails on **0/1 knapsack** (can't split items) and some **coin change** denominations. Always ask: "If I take the locally best choice, can I still reach the global optimum?" — that's the greedy proof.
</details>

---

## What You Can Do With It

| Question | Greedy idea |
|:---|:---|
| "Can reach last index?" | Track max reach |
| "Minimum jumps to end?" | Jump when at window boundary |
| "Valid gas station start?" | Reset when tank < 0 |
| "Minimum idle time for tasks?" | Schedule by frequency |
| "Minimum intervals to remove?" | Keep earliest-ending |

---

## Complexity (quick reference)

| Problem | Time | Space |
|:---|:---|:---|
| Jump game | O(n) | O(1) |
| Gas station | O(n) | O(1) |
| Task scheduler | O(n) | O(1) |
| Candy | O(n) | O(n) |
| Non-overlapping intervals | O(n log n) | O(1) |

---

## Common Interview Patterns

| When the problem says… | Think… |
|:---|:---|
| "Can jump to end" | Furthest reach |
| "Minimum jumps" | Jump window boundaries |
| "Gas station circuit" | Running tank + reset |
| "Task scheduler with cooldown" | Frequency math |
| "Minimum removals for intervals" | Sort by end, greedy keep |

---

## Practice Problems

| Problem | What it's really asking | Pattern |
|:---|:---|:---|
| Jump Game I | Can you reach the last index? | Max reach |
| Jump Game II | Minimum jumps to reach end? | Jump windows |
| Gas Station | Starting station for full circuit? | Tank reset |
| Task Scheduler | Minimum time with cooldown? | Frequency bottleneck |
| Non-overlapping Intervals | Fewest meetings to remove? | Earliest finish first |

Also in repo: **Candy** (two-pass greedy).

---

## Code

- **Python:** [`solutions.py`](./solutions.py)
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Sorting](../sorting/README.md) — sort before many greedy interval problems
- [Dynamic Programming](../dynamic_programming/README.md) — when greedy doesn't guarantee optimal
- [Arrays](../../data_structures/arrays/README.md) — many greedy problems are array sweeps
