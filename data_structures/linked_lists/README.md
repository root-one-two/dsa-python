# Linked Lists

## Functionality
A **Linked List** is a linear data structure consisting of nodes connected by pointers. Each node contains a data payload and a reference to the next node (Singly Linked List), and optionally a reference to the previous node (Doubly Linked List). Memory allocation is dynamic and non-contiguous. i.e elements (called nodes) are not stored in contiguous memory locations. Instead, each node contains a data payload and one or more pointers (references) to adjacent nodes in the sequence.

## Pros
* **O(1) Dynamic Insertions & Deletions**: Quick insertions/deletions when holding a pointer to the target node.
* **Dynamic Memory**: Grows and shrinks on demand without requiring upfront allocation or expensive array reallocation.

## Cons
* **O(n) Sequential Access**: Lacks direct index access; search operations require traversing nodes sequentially.
* **Memory Pointer Overhead**: Requires extra memory per node to store pointers/references.
* **Poor Cache Locality**: Nodes are scattered in memory, reducing CPU cache utilization.

## When to Use
* You frequently insert or delete elements at the beginning or middle of a sequence.
* The total dataset size is unpredictable or fluctuates constantly.
* Index-based random access is not required.

## Top 5 Essential Problems for Hands-On Practice
These 5 problems cover the core algorithmic techniques required for linked list manipulation (Pointer Reversal, Fast/Slow Pointers, Dummy Nodes, and Two-Pointer Intersections):
* Reverse a Linked List
    * Pattern: In-Place Pointer Manipulation
    * Focus: Reversing next pointers iteratively using prev, curr, and next_node variables in O(1) space.
* Linked List Cycle Detection (Floyd’s Cycle-Finding Algorithm)
    * Pattern: Fast & Slow Pointers (Tortoise and Hare)
    * Focus: Detecting cycles in a linked list using two pointers moving at different speeds (1x vs. 2x).
* Merge Two Sorted Lists
    * Pattern: Dummy Head Node / Two Pointers
    * Focus: Combining two sorted linked lists into a single sorted list efficiently using a dummy head sentinel node.
* Remove N-th Node From End of List
    * Pattern: Two-Pointer Offset Sweep
    * Focus: Using two pointers maintained at an offset of N nodes to delete a target node in a single pass.
* Intersection of Two Linked Lists
    * Pattern: Dual Pointer Alignment / Length Difference Equalization
    * Focus: Finding the convergence node of two overlapping linked lists in O(n) time without extra space.