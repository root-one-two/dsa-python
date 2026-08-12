# Heaps & Priority Queues

## Functionality
A **Heap** is a specialized tree-based structure satisfying the heap property: in a **Min-Heap**, parent nodes are smaller than or equal to their children; in a **Max-Heap**, parents are larger than or equal to their children. Usually implemented as binary heaps over flat arrays.

## Pros
* **$O(1)$ Min/Max Retrieval**: Instant access to the extreme element without sorting the entire collection.
* **Efficient Updates**: $O(\log n)$ insertions and removals (`extract-min`/`extract-max`).
* **Array Memory Layout**: Binary heaps can be efficiently mapped to contiguous arrays without pointer overhead.

## Cons
* **$O(n)$ Search Complexity**: Searching for an arbitrary non-extreme element requires linear inspection.
* **Unordered Iteration**: Traversing the heap does not yield elements in fully sorted order.

## When to Use
* Implementing Priority Queues (e.g., job scheduling, task prioritization).
* Graph algorithms requiring fast minimum-weight selection (Dijkstra's, Prim's).
* Finding the K-th largest or smallest element in dynamic streaming data.