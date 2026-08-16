# Trees & Binary Search Trees (BST)

## What It Is

A **tree** is a hierarchical structure of nodes with a single **root**. A **binary tree** has at most two children per node. A **BST** orders nodes: left subtree values are smaller, right subtree values are larger — enabling efficient search when balanced.

---

## ASCII: Binary Search Tree

```text
           8
          / \
         3   10
        / \    \
       1   6    14
          / \   /
         4   7 13
```

In-order traversal (left → node → right) yields sorted order: `1, 3, 4, 6, 7, 8, 10, 13, 14`.

---

## Complexity

| Operation | Balanced BST | Unbalanced BST |
|:---|:---|:---|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| In-order traversal | O(n) | O(n) |

Self-balancing trees (AVL, Red-Black) restore O(log n) guarantees with added implementation complexity.

---

## Pros & Cons

**Pros**

- O(log n) search, insert, delete when balanced
- Natural hierarchy (filesystems, DOM, org charts)
- In-order traversal produces sorted sequence

**Cons**

- Unbalanced BST degrades to linked-list performance
- Rebalancing adds implementation overhead

---

## When to Use

- Hierarchical or nested data representation
- Dynamic ordered set with fast lookup and insertion

**Pattern cues:** "depth", "validate BST", "level order", "LCA" → tree traversal or BST properties.

---

## Top 5 Essential Problems

| Problem | Pattern | Complexity | Focus |
|:---|:---|:---|:---|
| Maximum Depth of Binary Tree | DFS recursion | O(n) time | Count levels from root |
| Validate Binary Search Tree | Range-bounded DFS | O(n) time | Enforce min/max per subtree |
| Binary Tree Level Order Traversal | BFS with queue | O(n) time | Process one level at a time |
| BST Insert / Search / Delete | BST operations | O(log n)* | Core ordered-tree ADT |
| In-order Traversal | DFS | O(n) time | Sorted output for BST |

\*O(log n) when balanced.

---

## Implementations

- **Python:** [`solutions.py`](./solutions.py) — `TreeNode`, `BST`, traversals
- **Java:** [`Solutions.java`](./Solutions.java)

---

## Related Topics

- [Heaps](../heaps/README.md) — tree-based but different ordering property
- [Graphs](../graphs/README.md) — trees are acyclic connected graphs
- [Recursion & Backtracking](../../algorithms/recursion_backtracking/README.md) — natural fit for tree DFS
