# Arrays & Dynamic Arrays

## Functionality
An **Array** is a linear data structure that stores elements of the same type in contiguous memory locations. A **Dynamic Array** (like Python's `list`) automatically resizes itself when capacity limits are reached, allowing dynamic insertion and deletion while maintaining indexed access. 
**Dynamic Resizing (Python list):** Python automatically allocates extra capacity using an growth factor algorithm (~1.125x to 1.5x) to amortize the cost of append() operations.

## Pros
* **O(1) Random Access**: Instant element retrieval using zero-based indexing.
* **Cache Locality**: Elements occupy contiguous memory blocks, maximizing CPU cache efficiency.
* **Low Memory Overhead**: Minimal metadata stored alongside actual elements.

## Cons
* **Fixed/Expensive Resizing**: Dynamic arrays require O(n) time to copy elements into a new block when full.
* **Slow Insertions/Deletions**: Shifts remaining elements in O(n) time when inserting or deleting outside the array's end.

## When to Use
* You require frequent lookup or access by index O(1).
* You know the dataset size in advance, or changes primarily happen at the end of the array.
* You need optimal memory performance for sequential iteration.

## Top 5 Essential Problems for Hands-On Practice
These 5 curated problems cover the primary pattern archetypes for Array manipulation (Two Pointers, Sliding Window, Prefix Sum, Kadane’s Algorithm, and Hash Index Mapping):
**Two Sum**
    Pattern: Hash Mapping / Pre-computation
    Focus: Finding pair indices that match a target sum in O(n) time using a hash map trade-off.
**Best Time to Buy and Sell Stock**
    Pattern: Dynamic Tracking / Greedy
    Focus: Single-pass iteration tracking minimum element and maximum profit margin.
**Maximum Subarray (Kadane’s Algorithm)**
    Pattern: Kadane's Algorithm
    Focus: Continuous contiguous sub-array optimization in linear time.
**Two Pointers (e.g., Container With Most Water / Trapping Rain Water)**
    Pattern: Two Pointers (Left & Right inward sweep)
    Focus: Reducing O(n2) exhaustive search to O(n) space-time optimization using two pointers moving toward each other.
**Sliding Window Maximum / Subarray Product Less Than K**
    Pattern: Dynamic Sliding Window
    Focus: Managing fixed or variable range pointers over a dynamic window to evaluate running metrics efficiently.