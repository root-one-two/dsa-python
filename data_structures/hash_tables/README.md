# Hash Tables

> **Before you read this:** Comfortable with [arrays](../arrays/README.md) — a hash table is an array of buckets, accessed by a computed index instead of position 0, 1, 2…

---

## In Plain English

A **hash table** (hash map) lets you **look up by name**, not by position.

You store **key → value** pairs: `"email" → "user@example.com"`, `42 → "score"`. Give the key, get the value fast — like a **dictionary** or **phone book by name**.

Behind the scenes, a **hash function** converts the key into an array index where the value lives.

---

## Real-World Examples

- **Python `dict` / Java `HashMap`** — the maps you use every day.
- **Cache** — "Have we seen this URL before?" → stored result.
- **Counting word frequencies** — each word is a key, count is the value.
- **Two Sum** — store seen numbers to find pairs quickly ([arrays](../arrays/README.md)).

---

## Key Ideas

| Term | Simple definition | Example |
|:---|:---|:---|
| **Key** | What you search by | Student ID, username |
| **Value** | What you store | Grade, profile data |
| **Hash function** | Key → bucket index | `hash("cat")` → 7 |
| **Collision** | Two keys land on same index | "cat" and "dog" both → slot 3 |
| **Chaining** | Store a small list at each bucket | Multiple items in one slot |
| **Open addressing** | Probe next free slot on collision | Try slot 4, then 5… |
| **Load factor** | How full the table is | Resize when too crowded |

---

## How It Works

**Put and get:**

```text
put("name", "Uday")  → hash("name") = 2 → store at bucket 2
get("name")          → hash("name") = 2 → read bucket 2 → "Uday"
```

**Collision with chaining:**

```text
Bucket 0 → [ (alice, 90) ]
Bucket 1 → [ (bob, 85) ] → [ (bart, 70) ]   ← two keys hashed to 1
Bucket 2 → empty
```

<details>
<summary><strong>Go deeper — worst case & ordering</strong></summary>

- **Average O(1):** With a good hash and reasonable load factor, lookups are very fast.
- **Worst case O(n):** If every key collides, you scan a long chain.
- **No sorted order:** Keys are not stored alphabetically — unlike a BST.
</details>

---

## What You Can Do With It

| Action | Plain English |
|:---|:---|
| **Put (insert)** | Store key → value |
| **Get** | Look up value by key |
| **Remove** | Delete a key and its value |
| **Contains** | "Have I seen this key?" (hash set = keys only) |

---

## Complexity (quick reference)

*n = number of key-value pairs*

| Operation | Average | Worst case |
|:---|:---|:---|
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Space | O(n) | O(n) |

---

## Common Interview Patterns

| When the problem says… | Think… |
|:---|:---|
| "Count frequency" | Hash map key → count |
| "Group by signature" | Hash map normalized key → list |
| "Duplicate?" | Hash set membership |
| "Two sum" | Map value seen → index |
| "Anagram groups" | Hash by sorted letters |

---

## Practice Problems

| Problem | What it's really asking | Pattern |
|:---|:---|:---|
| Hash Map (ADT) | Core put/get/remove | Chaining |
| Group Anagrams | Cluster words with same letters | Hash by sorted string |
| Top K Frequent | Which numbers appear most? | Count map + bucket/heap |
| Contains Duplicate | Any value appears twice? | Hash set |
| Longest Consecutive (concept) | Longest chain of consecutive integers | Set + expand from starts |

---

## Code

- **Python:** [`solutions.py`](./solutions.py)
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Arrays](../arrays/README.md) — Two Sum with a map
- [Tries](../tries/README.md) — prefix queries a hash set cannot answer cheaply
- [Sorting](../../algorithms/sorting/README.md) — when you need order, not just lookup
- [Concurrency](../../concurrency_parallelism/README.md) — thread-safe maps need extra care
