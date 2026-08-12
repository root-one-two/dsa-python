# Linked Lists

## Functionality
A **Linked List** is a linear data structure consisting of nodes connected by pointers. Each node contains a data payload and a reference to the next node (Singly Linked List), and optionally a reference to the previous node (Doubly Linked List). Memory allocation is dynamic and non-contiguous.

## Pros
* **$O(1)$ Dynamic Insertions & Deletions**: Quick insertions/deletions when holding a pointer to the target node.
* **Dynamic Memory**: Grows and shrinks on demand without requiring upfront allocation or expensive array reallocation.

## Cons
* **$O(n)$ Sequential Access**: Lacks direct index access; search operations require traversing nodes sequentially.
* **Memory Pointer Overhead**: Requires extra memory per node to store pointers/references.
* **Poor Cache Locality**: Nodes are scattered in memory, reducing CPU cache utilization.

## When to Use
* You frequently insert or delete elements at the beginning or middle of a sequence.
* The total dataset size is unpredictable or fluctuates constantly.
* Index-based random access is not required.