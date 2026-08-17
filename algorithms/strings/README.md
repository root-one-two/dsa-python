# Strings, Two Pointers & Sliding Window

> **Before you read this:** Comfortable with [arrays](../../data_structures/arrays/README.md). A string is a row of characters. Numeric two-pointer examples (container with water, rain water) live on the arrays page — this page focuses on **text** and **windows**.

---

## In Plain English

A **string** is text stored as a sequence of characters you can index like an array: `"cat"[0]` is `'c'`.

**Two pointers** means two indices walking the string (often from both ends, or one staying while the other moves). You avoid nested loops that re-scan the same letters.

A **sliding window** is a **contiguous slice** `[left, right]` that grows and shrinks as you scan. You keep a running count (unique letters, product, frequency) instead of restarting from scratch for every substring.

---

## Real-World Examples

- **Palindrome check** — "Was it a car or a cat I saw?" — skip spaces and punctuation, compare inward.
- **Search box** — longest stretch of typing without repeating a letter (unique-character window).
- **Autocomplete cleanup** — reverse word order in a sentence: `"the sky is blue"` → `"blue is sky the"`.
- **Chat filter** — longest run of the same mood if you are allowed `k` replacements (character replacement).

---

## Key Ideas

| Term | Simple definition | Example |
|:---|:---|:---|
| **Two pointers** | Two indices moving through the same string | Left and right meeting in the middle |
| **Opposite ends** | Start at 0 and n-1, move inward | Palindrome |
| **Same direction** | Both move left → right, `left ≤ right` | 3Sum after sorting |
| **Sliding window** | Inclusive range `[left, right]` that slides | Longest unique substring |
| **Window invariant** | Rule the window must keep true | "All characters unique" |
| **Shrink when invalid** | Move `left` forward until the rule holds again | Repeat seen → jump `left` past it |

---

## How It Works

**Palindrome (opposite ends):**

```text
"A man, a plan, a canal: Panama"
 skip junk → compare A==A, m==m, … meet in the middle
```

**Sliding window (longest substring without repeating letters):**

```text
s = "abcabcbb"
 window: [a] [ab] [abc]  then 'a' repeats → drop left until unique
          a b c a …        left jumps past the first 'a'
 longest unique length = 3  ("abc")
```

**3Sum (sort, then two pointers):**

```text
sorted: [-4, -1, -1, 0, 1, 2]
 fix -1, search pair that sums to +1  →  (-1, 0, 1) and (-1, -1, 2)
 skip duplicate fixed values so you don't emit the same triplet twice
```

<details>
<summary><strong>Go deeper — why O(n) instead of O(n²)</strong></summary>

- Each index is a candidate `right` **once**. `left` only moves forward. Together they move at most 2n steps.
- Store last-seen index (or a frequency map) so shrinking the window is O(1) per step, not a rescan.
- After sorting, 3Sum is O(n²): one loop for the fixed number, two pointers for the pair — not O(n³) three nested loops.
</details>

---

## What You Can Do With It

| Question | Approach |
|:---|:---|
| "Is this a palindrome (ignore punctuation)?" | Two pointers from both ends |
| "Three numbers that sum to 0?" | Sort + fix one + two pointers |
| "Longest substring with all unique letters?" | Window + last-seen index |
| "Longest substring if I may change k letters?" | Window + max frequency in window |
| "Reverse the words, keep letters inside a word?" | Split on spaces, reverse the word list |

---

## Complexity (quick reference)

*n = length of the string (or array)*

| Pattern | Time | Extra space |
|:---|:---|:---|
| Two pointers (palindrome) | O(n) | O(1) |
| Sliding window + map | O(n) | O(alphabet) — often 26 or 128 |
| 3Sum | O(n²) after O(n log n) sort | O(1) besides output |

---

## Common Interview Patterns

| When the problem says… | Think… |
|:---|:---|
| "Palindrome" / "from both ends" | Opposite-end pointers |
| "Contiguous substring / subarray with condition" | Sliding window |
| "At most k distinct / k replacements" | Window + frequency map |
| "All unique characters in a window" | Window + last index of each char |
| "Triplets that sum to target" | Sort + two pointers |

---

## Practice Problems

| Problem | What it's really asking | Pattern |
|:---|:---|:---|
| Valid Palindrome | Same forwards and backwards, ignore junk | Two pointers |
| 3Sum | Unique triplets that add to 0 | Sort + two pointers |
| Longest Substring Without Repeating | Longest unique-letter window | Sliding window |
| Longest Repeating Character Replacement | Longest same-letter run with k edits | Window + max freq |
| Reverse Words in a String | Flip word order, collapse spaces | Two pointers on words |

---

## Code

- **Python:** [`solutions.py`](./solutions.py)
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Arrays](../../data_structures/arrays/README.md) — two pointers on numbers (container, rain water)
- [Hash Tables](../../data_structures/hash_tables/README.md) — last-seen index and frequency maps
- [Searching](../searching/README.md) — binary search is a different two-bound technique
