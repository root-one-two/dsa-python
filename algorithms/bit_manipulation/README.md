# Bit Manipulation

> **Before you read this:** Comfortable with [arrays](../../data_structures/arrays/README.md) and integers. Bits are the 0/1 digits inside a number. You do not need hardware knowledge — only a few operations.

---

## In Plain English

Computers store integers as a row of **bits** (binary digits), like:

```text
13  =  1 1 0 1     (8 + 4 + 0 + 1)
```

**Bit manipulation** means answering questions by flipping, masking, or combining those 0s and 1s — often in **O(1)** or **O(number of 1-bits)** instead of converting to a string of `'0'`/`'1'`.

You will see four operators constantly:

| Operator | Name | Everyday picture |
|:---|:---|:---|
| `&` | AND | Both switches on → on |
| `\|` | OR | Either switch on → on |
| `^` | XOR | Different → on (same → off) |
| `~` | NOT | Flip every bit |
| `<<` `>>` | Shift | Slide the row left/right (×2 or ÷2 for unsigned) |

---

## Real-World Examples

- **Flags / permissions** — one integer holds many yes/no options (read, write, execute).
- **Find the unique ID** — every duplicate cancels out with XOR; the leftover is the singleton.
- **Count how many lights are on** — count 1-bits (Hamming weight).
- **Power of two?** — a power of two has **exactly one** 1-bit (`8` is `1000`).

---

## Key Ideas

| Term | Simple definition | Example |
|:---|:---|:---|
| **Bit** | A single 0 or 1 | The 2's place in `1101` |
| **Mask** | A number used to keep or clear bits | `n & 1` keeps only the last bit |
| **XOR cancel** | `x ^ x = 0`, `x ^ 0 = x` | Duplicates vanish |
| **n & (n - 1)** | Clears the lowest 1-bit | `1100` → `1000` |
| **Least significant bit** | The rightmost bit | `n & 1` is 0 if even |

---

## How It Works

**XOR unique number** — `2, 3, 2, 4, 4`:

```text
  2 ^ 3 ^ 2 ^ 4 ^ 4
= (2 ^ 2) ^ (4 ^ 4) ^ 3
= 0 ^ 0 ^ 3
= 3
```

**Clear lowest set bit** (count 1s by repeating this):

```text
n      = 1 0 1 1 0    (22)
n - 1  = 1 0 1 0 1
n & (n-1) = 1 0 1 0 0    ← one 1 removed
```

**Power of two:** `n > 0` and `n & (n - 1) == 0` (only one 1-bit remains).

<details>
<summary><strong>Go deeper — two's complement & shifts</strong></summary>

- Negative numbers in two's complement: `-n` is `~n + 1`. Interview problems usually specify **32-bit unsigned** (e.g. reverse bits) so you treat the value as a fixed-width row.
- `n << k` multiplies by 2^k (watch overflow). `n >> k` in Python is arithmetic on integers of unlimited size — mask with `0xFFFFFFFF` when you need 32-bit wraparound.
- Counting bits with `n & (n - 1)` is O(number of 1s), better than looping all 32 bits when the number is sparse.
</details>

---

## What You Can Do With It

| Question | Trick |
|:---|:---|
| "How many 1-bits?" | Repeat `n &= n - 1` |
| "Which number appears once?" | XOR the whole array |
| "Is n a power of two?" | `n > 0` and `n & (n - 1) == 0` |
| "Missing number in 0..n?" | XOR indices with values |
| "Reverse 32 bits?" | 32 times: shift result left, take `n & 1`, shift n right |

---

## Complexity (quick reference)

| Operation | Time | Notes |
|:---|:---|:---|
| Hamming weight | O(number of 1s) | Or O(32) if you loop bits |
| XOR over n numbers | O(n) | O(1) extra space |
| Power of two / reverse bits | O(1) or O(32) | Fixed width |

---

## Common Interview Patterns

| When the problem says… | Think… |
|:---|:---|
| "Single number" / "appears once" | XOR |
| "Count set bits" / Hamming | `n & (n - 1)` loop |
| "Power of two" | One bit set |
| "Missing / extra in 0..n" | XOR or gauss sum |
| "Without + / -" (concept) | XOR for sum bits, AND+shift for carry |

---

## Practice Problems

| Problem | What it's really asking | Pattern |
|:---|:---|:---|
| Number of 1 Bits | Count set bits | `n & (n - 1)` |
| Single Number | One unique, rest twice | XOR |
| Power of Two | Exactly one 1-bit? | `n & (n - 1)` |
| Missing Number | Which value in 0..n is absent? | XOR index with value |
| Reverse Bits | Flip a 32-bit pattern | Shift and mask |

---

## Code

- **Python:** [`solutions.py`](./solutions.py)
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Arrays](../../data_structures/arrays/README.md) — bit tricks often scan an integer array once
- [Dynamic Programming](../dynamic_programming/README.md) — some DP uses bitmasks for subsets
- [Hash Tables](../../data_structures/hash_tables/README.md) — counting with a map vs XOR when every duplicate appears twice
