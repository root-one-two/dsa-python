# Tries (Prefix Trees)

> **Before you read this:** Comfortable with [trees](../trees/README.md) and [hash tables](../hash_tables/README.md). A trie is a tree where **each edge is a character**, so a path from the root spells a word.

---

## In Plain English

A **trie** (pronounced "try") stores many strings by **sharing prefixes**.

The words `car`, `cat`, and `cart` share `ca`. You do not store three full copies — you store `c → a`, then branch to `r` and `t`.

- **Insert** — walk/create one node per letter, mark the last node "this is a complete word."
- **Search** — walk the letters; succeed only if you end on a marked word (so `ca` is not found just because `cat` exists).
- **Starts with** — same walk, but you only care that the path exists.

A hash set can tell you "is this **exact** word in the dictionary?" in average O(1). A trie answers "**any word start with `app`?**" without scanning every key.

---

## Real-World Examples

- **Autocomplete** — type `app` → `apple`, `apply`, `application`.
- **Spell check / dictionary** — walk letters until the path dies → not a word.
- **IP / URL routing** (concept) — longest matching prefix.
- **Replace words** — in a sentence, swap each word for the **shortest dictionary root** (`cat` replaces `cattle`).

---

## Key Ideas

| Term | Simple definition | Example |
|:---|:---|:---|
| **Node** | One letter position; map of next letters | After `c`, children might be `a` |
| **Edge / child key** | The next character | `'a' →` next node |
| **is_word flag** | This path is a full dictionary word | `ca` vs `cat` |
| **Prefix** | First k letters of a word | `app` is a prefix of `apple` |
| **Shared prefix** | Common start of several words | `car` and `cart` share `car` |

---

## How It Works

Insert `cat`, `car`, `cart`:

```text
        root
         │
         c
         │
         a
        / \
       t*  r*
            \
             t*     * = is_word

search("ca")   → path exists, but node `a` is not marked → false
startsWith("ca") → path exists → true
search("cat")  → ends on t* → true
```

<details>
<summary><strong>Go deeper — cost vs a hash set</strong></summary>

- Time for insert/search is **O(L)** where L is the word length — independent of how many *other* words you stored (unless you count the alphabet branching).
- Space can be high if prefixes don't overlap (one node per character). Compressed tries (radix trees) merge chains of single children.
- Unicode / large alphabets: use a hash map of children (as in this primer) instead of a 26-slot array.
</details>

---

## What You Can Do With It

| Action | Plain English |
|:---|:---|
| **Insert** | Add a word to the dictionary |
| **Search** | Is this exact word present? |
| **Starts with** | Does any word begin with this prefix? |
| **Shortest root** | Walk until the first `is_word` (Replace Words) |

---

## Complexity (quick reference)

*L = length of the word / prefix, n = number of words stored*

| Operation | Time | Notes |
|:---|:---|:---|
| Insert | O(L) | One node per new character |
| Search | O(L) | |
| Starts with | O(L) | |
| Space | O(total characters) | Shared prefixes save space |

---

## Common Interview Patterns

| When the problem says… | Think… |
|:---|:---|
| "Words with prefix" / autocomplete | Trie + DFS from the prefix node |
| "Shortest root / replace words" | Trie, stop at first `is_word` |
| "Word search in a board" (concept) | Trie of the word list + DFS on grid |
| "Exact dictionary lookup only" | Hash set is simpler — skip the trie |

---

## Practice Problems

| Problem | What it's really asking | Pattern |
|:---|:---|:---|
| Implement Trie | Insert, search, startsWith | Prefix tree ADT |
| Replace Words | Swap each sentence word for shortest root | Walk until first word node |

---

## Code

- **Python:** [`solutions.py`](./solutions.py)
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Trees](../trees/README.md) — same parent/child idea; trie children are labeled by characters
- [Hash Tables](../hash_tables/README.md) — better for exact key lookup with no prefix queries
- [Strings, Two Pointers & Sliding Window](../../algorithms/strings/README.md) — raw string scans without a dictionary tree
