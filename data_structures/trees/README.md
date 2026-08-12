# Trees & Binary Search Trees (BST)

## Functionality
A **Tree** is a hierarchical structure of connected nodes starting from a single root. A **Binary Search Tree (BST)** imposes an ordering constraint where every node's left child contains a strictly smaller value, and its right child contains a larger value.

## Pros
* **Efficient $O(\log n)$ Searching**: Faster search, insertion, and deletion operations than linear lists (when balanced).
* **Hierarchical Organization**: Naturally represents nested or multi-level data structures (like directory systems or DOM nodes).
* **Sorted Traversal**: In-order traversal yields elements in sorted order in $O(n)$ time.

## Cons
* **Tree Unbalancing**: Unbalanced search trees degrade to $O(n)$ operations, acting like linked lists.
* **Complex Rebalancing**: Self-balancing trees (AVL, Red-Black) introduce implementation complexity.

## When to Use
* You need hierarchical representation (e.g., file systems, XML/HTML parsers).
* You require fast, dynamic search and insertion while keeping data ordered.