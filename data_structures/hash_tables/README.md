# Hash Tables

## Functionality
A **Hash Table** (or Hash Map) maps key-value pairs by passing keys through a **Hash Function** to compute array indexes. Collisions are handled via techniques like **Chaining** (linked lists at bucket indices) or **Open Addressing** (probing).

## Pros
* **Average $O(1)$ Lookups**: Extremely fast insertions, deletions, and retrievals by key.
* **Key-Value Flexibility**: Enables indexing using arbitrary data types (strings, custom objects).

## Cons
* **Worst-Case $O(n)$ Degeneration**: Severe hash collisions collapse performance to linear time.
* **Unordered Keys**: Hash tables do not maintain natural element order.
* **Memory Overhead**: Requires excess array allocation to maintain low load factors and avoid frequent collisions.

## When to Use
* You need instant lookup, insertion, or deletion using unique key attributes.
* Caching, indexing, counting frequencies, or duplicate detection scenarios.