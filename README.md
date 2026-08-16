# Data Structures & Algorithms Primer (Python & Java)

A structured **primer** for learning core data structures and algorithmic paradigms. Each topic folder explains *what* the concept is, *when* to use it, *how* it behaves under load, and *which patterns* show up in interviews — with reference implementations in Python and Java.

---

## Table of Contents

- [How to Use This Repo](#how-to-use-this-repo)
- [Suggested Learning Path](#suggested-learning-path)
- [Topic Index](#topic-index)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Testing](#testing)
- [Time & Space Complexity Reference](#time--space-complexity-reference)
- [Contributing](#contributing)

---

## How to Use This Repo

1. **Read** the topic `README.md` — concept, tradeoffs, patterns, and practice problems.
2. **Study** the implementations in `solutions.py` and `Solutions.java`.
3. **Run** the Python examples or compile the Java classes locally.
4. **Practice** the Top 5 problems listed in each topic before moving on.
5. **Verify** your understanding with `pytest` (see [Testing](#testing)).

Each subdirectory follows the same layout:

```text
topic/
├── README.md        # Primer notes for this topic
├── solutions.py     # Python reference implementations
└── Solutions.java   # Java reference implementations
```

---

## Suggested Learning Path

| Phase | Topics | Why this order |
|:---|:---|:---|
| **1 — Foundations** | Arrays → Linked Lists → Stacks & Queues | Linear structures and pointer/window patterns |
| **2 — Non-linear** | Trees → Heaps → Hash Tables → Graphs | Hierarchical and networked data |
| **3 — Paradigms** | Sorting → Searching → Recursion & Backtracking | Core algorithm families |
| **4 — Optimization** | Dynamic Programming → Greedy | Choosing the right optimization lens |
| **5 — Systems** | Concurrency & Parallelism | When single-threaded assumptions break |

**Cross-links:** Searching assumes sorted data (Sorting). Heaps extend Trees. Graph BFS/DFS use Queues and Stacks.

---

## Topic Index

### Data Structures

| Topic | Summary | README | Solutions |
|:---|:---|:---|:---|
| Arrays | Contiguous memory, two pointers, sliding window | [README](data_structures/arrays/README.md) | [py](data_structures/arrays/solutions.py) · [java](data_structures/arrays/Solutions.java) |
| Linked Lists | Pointer manipulation, fast/slow pointers | [README](data_structures/linked_lists/README.md) | [py](data_structures/linked_lists/solutions.py) · [java](data_structures/linked_lists/Solutions.java) |
| Stacks & Queues | LIFO/FIFO, DFS/BFS building blocks | [README](data_structures/stacks_queues/README.md) | [py](data_structures/stacks_queues/solutions.py) · [java](data_structures/stacks_queues/Solutions.java) |
| Trees & BST | Hierarchy, ordered search, traversals | [README](data_structures/trees/README.md) | [py](data_structures/trees/solutions.py) · [java](data_structures/trees/Solutions.java) |
| Heaps | Min/max retrieval, priority queues | [README](data_structures/heaps/README.md) | [py](data_structures/heaps/solutions.py) · [java](data_structures/heaps/Solutions.java) |
| Hash Tables | Key-value maps, O(1) average lookup | [README](data_structures/hash_tables/README.md) | [py](data_structures/hash_tables/solutions.py) · [java](data_structures/hash_tables/Solutions.java) |
| Graphs | Nodes and edges, traversal, dependencies | [README](data_structures/graphs/README.md) | [py](data_structures/graphs/solutions.py) · [java](data_structures/graphs/Solutions.java) |

### Algorithms

| Topic | Summary | README | Solutions |
|:---|:---|:---|:---|
| Sorting | Ordering, partitioning, interval problems | [README](algorithms/sorting/README.md) | [py](algorithms/sorting/solutions.py) · [java](algorithms/sorting/Solutions.java) |
| Searching | Binary search, answer-space bisection | [README](algorithms/searching/README.md) | [py](algorithms/searching/solutions.py) · [java](algorithms/searching/Solutions.java) |
| Recursion & Backtracking | State-space exploration, prune & undo | [README](algorithms/recursion_backtracking/README.md) | [py](algorithms/recursion_backtracking/solutions.py) · [java](algorithms/recursion_backtracking/Solutions.java) |
| Dynamic Programming | Overlapping subproblems, optimal substructure | [README](algorithms/dynamic_programming/README.md) | [py](algorithms/dynamic_programming/solutions.py) · [java](algorithms/dynamic_programming/Solutions.java) |
| Greedy | Local optimal choices, interval scheduling | [README](algorithms/greedy/README.md) | [py](algorithms/greedy/solutions.py) · [java](algorithms/greedy/Solutions.java) |

### Systems

| Topic | Summary | README | Solutions |
|:---|:---|:---|:---|
| Concurrency & Parallelism | Thread safety, producer-consumer, race conditions | [README](concurrency_parallelism/README.md) | [py](concurrency_parallelism/solutions.py) · [java](concurrency_parallelism/Solutions.java) |

Deep dive: [From Sequential to Multithreaded](concurrency_parallelism/FROM_SEQUENTIAL_TO_MULTITHREADED.md)

---

## Repository Structure

```text
dsa-python/
├── data_structures/
│   ├── arrays/
│   ├── linked_lists/
│   ├── stacks_queues/
│   ├── trees/
│   ├── heaps/
│   ├── hash_tables/
│   └── graphs/
├── algorithms/
│   ├── sorting/
│   ├── searching/
│   ├── recursion_backtracking/
│   ├── dynamic_programming/
│   └── greedy/
├── concurrency_parallelism/
├── tests/
│   ├── test_data_structures.py
│   └── test_algorithms.py
├── requirements.txt
└── README.md
```

---

## Getting Started

### Python

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest tests/ -v
```

Run a topic module directly (example):

```bash
python concurrency_parallelism/solutions.py
```

### Java

Each topic includes a `Solutions.java` file. Compile and run from the topic directory:

```bash
cd data_structures/arrays
javac Solutions.java
# Use a small driver or IDE to call static methods on Solutions
```

---

## Testing

Tests use `pytest` and cover representative problems from the primer. They are **growing** alongside the repo — not every README problem has a test yet.

```bash
pytest tests/ -v
```

Current coverage includes arrays, linked lists, sorting, searching, dynamic programming, and greedy samples. Add tests as you practice each topic.

---

## Time & Space Complexity Reference

### Common Data Structure Operations

| Structure | Access | Search | Insert | Delete | Notes |
|:---|:---|:---|:---|:---|:---|
| Array | O(1) | O(n) | O(n) | O(n) | O(1) append at end (amortized for dynamic arrays) |
| Linked List | O(n) | O(n) | O(1)* | O(1)* | *With pointer to node |
| Stack / Queue | O(n) | O(n) | O(1) | O(1) | Endpoint operations only |
| BST (balanced) | O(log n) | O(log n) | O(log n) | O(log n) | Degrades to O(n) if unbalanced |
| Hash Table | — | O(1)* | O(1)* | O(1)* | *Average; O(n) worst case |
| Binary Heap | — | O(n) | O(log n) | O(log n) | O(1) peek min/max |
| Graph (adj list) | — | O(V+E) | O(1) | O(E) | BFS/DFS traversal |

### Common Algorithm Families

| Family | Typical Time | Typical Space | Example |
|:---|:---|:---|:---|
| Sorting (comparison) | O(n log n) | O(1)–O(n) | Merge Sort, Quick Sort |
| Binary Search | O(log n) | O(1) | Find in sorted array |
| Binary Search on Answer | O(n log R) | O(1) | Koko Eating Bananas |
| Backtracking | O(2^n)–O(n!) | O(n) | Subsets, N-Queens |
| Dynamic Programming | O(n)–O(n²) | O(n)–O(n²) | Coin Change, LCS |
| Greedy | O(n)–O(n log n) | O(1)–O(n) | Interval scheduling |

---

## Contributing

Contributions that improve primer clarity are welcome: clearer explanations, consistent README structure, additional tests, and corrected implementations. Open a PR with a short description of what learners will gain from the change.
