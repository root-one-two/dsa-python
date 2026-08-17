# Trees & Binary Search Trees (BST)

> **Before you read this:** Comfortable with [linked lists](../linked_lists/README.md) — a tree is like a node that can point to **two** children instead of one next link.

---

## In Plain English

A **tree** is a **hierarchy** — like a family tree or company org chart. One **root** at the top; each node may have **children** below it. There are no cycles (no node is its own ancestor).

A **Binary Search Tree (BST)** adds a rule: for every node, **left subtree values are smaller**, **right subtree values are larger**. That makes searching fast when the tree stays balanced.

---

## Real-World Examples

- **File folders** — folder inside folder inside folder.
- **HTML DOM** — `<html>` → `<body>` → `<div>` → `<p>`.
- **BST** — sorted catalog where you compare and go left or right (like guessing a number game).

---

## Key Ideas

| Term | Simple definition | Example |
|:---|:---|:---|
| **Root** | Top node of the tree | CEO in org chart |
| **Child / parent** | Node below / node above | Manager and employee |
| **Leaf** | Node with no children | Bottom of hierarchy |
| **Binary tree** | Max 2 children per node | Left and right |
| **BST property** | Left < node < right | Enables ordered search |
| **In-order traversal** | Left → node → right | Gives sorted order in BST |
| **Depth** | How many levels from root | Height of subtree |

---

## How It Works

```text
           8          ← root
          / \
         3   10       ← children of 8
        / \    \
       1   6    14    ← leaves at bottom
          / \   /
         4   7 13
```

**BST search** for 6: start at 8 → 6 < 8 go left → 6 > 3 go right → found.

**In-order visit order:** 1, 3, 4, 6, 7, 8, 10, 13, 14 (sorted).

---

## What You Can Do With It

| Action | Plain English |
|:---|:---|
| **Traverse** | Visit every node (in-order, pre-order, level-order) |
| **Search in BST** | Compare and go left or right |
| **Insert / delete** | Place new value in correct position |
| **Max depth** | How deep is the longest branch? |
| **Validate BST** | Does every node follow left < node < right? |

---

## Complexity (quick reference)

*n = number of nodes*

| Operation | Balanced BST | Unbalanced BST |
|:---|:---|:---|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| Traverse all | O(n) | O(n) |

<details>
<summary><strong>Go deeper — balancing</strong></summary>

If you insert 1, 2, 3, 4, 5 in order into a BST, it becomes a straight line (like a linked list) — search becomes O(n). Self-balancing trees (AVL, Red-Black) fix this but add implementation complexity.
</details>

---

## Common Interview Patterns

| When the problem says… | Think… |
|:---|:---|
| "Maximum depth" | DFS recursion counting levels |
| "Validate BST" | DFS with min/max bounds |
| "Level order" | BFS with a [queue](../stacks_queues/README.md) |
| "Sorted order from tree" | In-order traversal |
| "LCA" (concept) | Walk from root until paths diverge |

---

## Practice Problems

| Problem | What it's really asking | Pattern |
|:---|:---|:---|
| Maximum Depth | How many levels deep? | DFS |
| Validate BST | Is the ordering rule satisfied everywhere? | Bounded DFS |
| Level Order Traversal | Visit row by row | BFS + queue |
| BST Insert/Search/Delete | Core ordered-tree operations | BST rules |
| In-order Traversal | Visit in sorted order | DFS left-root-right |

---

## Code

- **Python:** [`solutions.py`](./solutions.py) — `TreeNode`, `BST`, traversals
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Heaps](../heaps/README.md) — tree-shaped but different rules (min/max at root)
- [Tries](../tries/README.md) — a tree whose edges are characters
- [Graphs](../graphs/README.md) — trees are graphs with no cycles
- [Recursion & Backtracking](../../algorithms/recursion_backtracking/README.md) — tree DFS is recursive
