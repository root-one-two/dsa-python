# Arrays & Dynamic Arrays

## Functionality
An **Array** is a linear data structure that stores elements of the same type in contiguous memory locations. A **Dynamic Array** (like Python's `list`) automatically resizes itself when capacity limits are reached, allowing dynamic insertion and deletion while maintaining indexed access.

## Pros
* **$O(1)$ Random Access**: Instant element retrieval using zero-based indexing.
* **Cache Locality**: Elements occupy contiguous memory blocks, maximizing CPU cache efficiency.
* **Low Memory Overhead**: Minimal metadata stored alongside actual elements.

## Cons
* **Fixed/Expensive Resizing**: Dynamic arrays require O(n) time to copy elements into a new block when full.
* **Slow Insertions/Deletions**: Shifts remaining elements in O(n) time when inserting or deleting outside the array's end.

## When to Use
* You require frequent lookup or access by index O(1).
* You know the dataset size in advance, or changes primarily happen at the end of the array.
* You need optimal memory performance for sequential iteration.
