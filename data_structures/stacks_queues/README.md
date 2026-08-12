# Stacks & Queues

## Functionality
* **Stack**: A **LIFO** (Last-In, First-Out) linear structure where elements are added (`push`) and removed (`pop`) from the same end (the top).
* **Queue**: A **FIFO** (First-In, First-Out) linear structure where elements are added (`enqueue`) at the rear and removed (`dequeue`) from the front.

## Pros
* **Strict $O(1)$ Operations**: Constant-time execution for additions and removals at defined endpoints.
* **Predictable Access Control**: Enforces precise execution ordering for concurrent or state-based workflows.

## Cons
* **No Random Access**: Cannot access arbitrary internal elements without destroying or emptying the structure.
* **$O(n)$ Search Complexity**: Finding a specific value requires popping/dequeuing elements sequentially.

## When to Use
* **Stack**: Call stack management, undo/redo state history, balanced parenthesis parsing, and DFS (Depth-First Search).
* **Queue**: Task queues, rate limiting, buffering stream data, and BFS (Breadth-First Search).