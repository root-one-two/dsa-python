# Hash Tables

## What It Is

A **hash table** (hash map) stores **key-value pairs**. A **hash function** maps keys to array indices. **Collisions** — when two keys hash to the same index — are resolved via:

- **Chaining** — linked lists at each bucket
- **Open addressing** — probe for next free slot

---

## ASCII: Chaining Collision Resolution

```text
Buckets:
  index 0 → [ (k1,v1) ] → [ (k9,v9) ]   ← collision chain
  index 1 → [ (k2,v2) ]
  index 2 → ∅
  index 3 → [ (k4,v4) ]
```

---

## Complexity

| Operation | Average | Worst Case | Notes |
|:---|:---|:---|:---|
| Insert | O(1) | O(n) | Worst case: all keys collide |
| Search | O(1) | O(n) | Depends on load factor |
| Delete | O(1) | O(n) | Rehashing may be needed |
| Space | O(n) | O(n) | Extra capacity reduces collisions |

---

## Pros & Cons

**Pros**

- Average O(1) lookup, insert, delete by key
- Flexible keys (strings, tuples, custom objects)

**Cons**

- Worst-case O(n) with poor hash function or high load factor
- No inherent ordering of keys
- Memory overhead for buckets and load-factor headroom

---

## When to Use

- Instant lookup, insertion, or deletion by key
- Frequency counting, caching, duplicate detection, indexing

**Pattern cues:** "count frequency", "group by", "duplicate", "two sum with map" → hash table.

---

## Top 5 Essential Problems

| Problem | Pattern | Complexity | Focus |
|:---|:---|:---|:---|
| Hash Map (core ADT) | Chaining | O(1) average | `put`, `get`, `remove` |
| Group Anagrams | Sorted key grouping | O(n × k log k) | Hash by anagram signature |
| Top K Frequent Elements | Count + bucket/heap | O(n) average | Frequency map then select |
| Contains Duplicate | Hash set | O(n) time | O(1) membership check |
| Longest Consecutive Sequence (concept) | Set + expansion | O(n) time | Only start from sequence beginnings |

---

## Implementations

- **Python:** [`solutions.py`](./solutions.py) — `HashMap`, `group_anagrams`, `top_k_frequent`, `contains_duplicate`
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Arrays](../arrays/README.md) — Two Sum often uses a hash map
- [Sorting](../../algorithms/sorting/README.md) — alternative when ordering matters
- [Concurrency](../../concurrency_parallelism/README.md) — concurrent hash maps need synchronization
