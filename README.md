# Data Structures & Algorithms Primer (Python & Java)

A **beginner-friendly primer** for learning core data structures and algorithms. Each topic explains ideas in plain English first, then builds up to interview patterns and code.

---

## How to Read This Repo

1. **Start with "In Plain English"** in each topic README — no jargon required.
2. **Look at the diagram** and match labels to the Key Ideas table.
3. **Skim "What You Can Do With It"** before the complexity table.
4. **Read the code** in `solutions.py` / `Solutions.java` while following one practice problem.
5. **Use "Go Deeper"** sections (collapsed) when you're ready for formal terms and Big-O details.
6. **Run tests** to verify your understanding: `pytest tests/ -v`

If a word is new, it should be defined in that topic's **Key Ideas** table before it's used in complexity or patterns.

---

## Suggested Learning Path

| Phase | Topics | Why this order |
|:---|:---|:---|
| **1 — Foundations** | [Arrays](data_structures/arrays/README.md) → [Linked Lists](data_structures/linked_lists/README.md) → [Stacks & Queues](data_structures/stacks_queues/README.md) → [Strings & Windows](algorithms/strings/README.md) | Linear structures, then scans on text |
| **2 — Non-linear** | [Trees](data_structures/trees/README.md) → [Tries](data_structures/tries/README.md) → [Heaps](data_structures/heaps/README.md) → [Hash Tables](data_structures/hash_tables/README.md) → [Graphs](data_structures/graphs/README.md) → [Union-Find](data_structures/union_find/README.md) | Hierarchy, prefixes, priority, lookup, networks, merging groups |
| **3 — Paradigms** | [Sorting](algorithms/sorting/README.md) → [Searching](algorithms/searching/README.md) → [Recursion & Backtracking](algorithms/recursion_backtracking/README.md) → [Bit Manipulation](algorithms/bit_manipulation/README.md) | Ordering, exploration, and integer tricks |
| **4 — Optimization** | [Dynamic Programming](algorithms/dynamic_programming/README.md) → [Greedy](algorithms/greedy/README.md) | When to cache vs. when to guess |
| **5 — Systems** | [Concurrency](concurrency_parallelism/README.md) | Multiple threads sharing data |

---

## Topic Index

### Data Structures

| Topic | One-line summary | README | Code |
|:---|:---|:---|:---|
| Arrays | Numbered lockers in a row | [README](data_structures/arrays/README.md) | [py](data_structures/arrays/solutions.py) · [java](data_structures/arrays/Solutions.java) |
| Linked Lists | Chain of nodes pointing forward | [README](data_structures/linked_lists/README.md) | [py](data_structures/linked_lists/solutions.py) · [java](data_structures/linked_lists/Solutions.java) |
| Stacks & Queues | LIFO stack and FIFO queue | [README](data_structures/stacks_queues/README.md) | [py](data_structures/stacks_queues/solutions.py) · [java](data_structures/stacks_queues/Solutions.java) |
| Trees & BST | Hierarchy like a family tree | [README](data_structures/trees/README.md) | [py](data_structures/trees/solutions.py) · [java](data_structures/trees/Solutions.java) |
| Heaps | Always know the smallest or largest item | [README](data_structures/heaps/README.md) | [py](data_structures/heaps/solutions.py) · [java](data_structures/heaps/Solutions.java) |
| Hash Tables | Look up by name, not position | [README](data_structures/hash_tables/README.md) | [py](data_structures/hash_tables/solutions.py) · [java](data_structures/hash_tables/Solutions.java) |
| Graphs | Cities and roads between them | [README](data_structures/graphs/README.md) | [py](data_structures/graphs/solutions.py) · [java](data_structures/graphs/Solutions.java) |
| Tries | Shared prefixes of many words | [README](data_structures/tries/README.md) | [py](data_structures/tries/solutions.py) · [java](data_structures/tries/Solutions.java) |
| Union-Find | Merge groups; ask if two items are connected | [README](data_structures/union_find/README.md) | [py](data_structures/union_find/solutions.py) · [java](data_structures/union_find/Solutions.java) |

### Algorithms

| Topic | One-line summary | README | Code |
|:---|:---|:---|:---|
| Sorting | Put items in order | [README](algorithms/sorting/README.md) | [py](algorithms/sorting/solutions.py) · [java](algorithms/sorting/Solutions.java) |
| Searching | Find a value or best answer | [README](algorithms/searching/README.md) | [py](algorithms/searching/solutions.py) · [java](algorithms/searching/Solutions.java) |
| Recursion & Backtracking | Solve by breaking down; explore choices | [README](algorithms/recursion_backtracking/README.md) | [py](algorithms/recursion_backtracking/solutions.py) · [java](algorithms/recursion_backtracking/Solutions.java) |
| Dynamic Programming | Remember answers to sub-problems | [README](algorithms/dynamic_programming/README.md) | [py](algorithms/dynamic_programming/solutions.py) · [java](algorithms/dynamic_programming/Solutions.java) |
| Greedy | Pick the best local choice each step | [README](algorithms/greedy/README.md) | [py](algorithms/greedy/solutions.py) · [java](algorithms/greedy/Solutions.java) |
| Strings & Windows | Palindromes, unique substrings, 3Sum | [README](algorithms/strings/README.md) | [py](algorithms/strings/solutions.py) · [java](algorithms/strings/Solutions.java) |
| Bit Manipulation | AND, XOR, and counting 1-bits | [README](algorithms/bit_manipulation/README.md) | [py](algorithms/bit_manipulation/solutions.py) · [java](algorithms/bit_manipulation/Solutions.java) |

### Systems

| Topic | One-line summary | README | Code |
|:---|:---|:---|:---|
| Concurrency | Many threads sharing the same data safely | [README](concurrency_parallelism/README.md) | [py](concurrency_parallelism/solutions.py) · [java](concurrency_parallelism/Solutions.java) |

---

## Getting Started

### Python

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest tests/ -v
```

### Java

Each topic has a `Solutions.java` file. Compile from the topic folder:

```bash
cd data_structures/arrays
javac Solutions.java
```

---

## Repository Structure

```text
dsa-python/
├── data_structures/     # arrays, lists, trees, tries, graphs, union-find, etc.
├── algorithms/        # sorting, searching, strings/windows, bits, DP, greedy, etc.
├── concurrency_parallelism/
├── tests/
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Testing

```bash
pytest tests/ -v
```

Tests cover representative problems from each topic. They grow as the primer expands — run them after reading a topic and studying the solutions.

---

## Contributing

Improvements that make concepts clearer for beginners are especially welcome: better analogies, simpler opening sections, and examples before jargon.
