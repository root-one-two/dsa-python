# 🔢 Sorting Algorithms

Sorting is the algorithmic process of arranging elements of a collection into a specific order (typically ascending or descending). It serves as a foundational building block for complex operations such as binary search, duplicate detection, data compression, and divide-and-conquer optimizations.

---

## 📌 Features

- **Comparison vs. Non-Comparison Based**: Comparison algorithms (Quick Sort, Merge Sort, Heap Sort) have a lower bound of $O(n \log n)$, while non-comparison algorithms (Counting Sort, Radix Sort) achieve $O(n + k)$ by exploiting data properties.
- **Stability**: Stable sorting algorithms preserve the relative order of duplicate elements (crucial for multi-key sorting like database records).
- **In-Place vs. Out-of-Place**: In-place algorithms sort using $O(1)$ auxiliary space, whereas out-of-place algorithms require extra allocations (e.g., $O(n)$ for Merge Sort).

---

## ⚖️ Pros & Cons

| Algorithm Category | Pros | Cons |
| :--- | :--- | :--- |
| **Divide & Conquer (Merge / Quick Sort)** | • Fast average runtime ($O(n \log n)$)<br>• Highly scalable for large datasets | • Quick Sort degrades to $O(n^2)$ worst-case without pivot randomization<br>• Merge Sort requires $O(n)$ auxiliary memory |
| **Elementary (Insertion / Bubble / Selection)** | • $O(1)$ space<br>• Simple implementation<br>• Insertion sort is $O(n)$ on nearly sorted data | • $O(n^2)$ average/worst-case runtime<br>• Inefficient for large datasets |
| **Linear / Non-Comparison (Counting / Radix Sort)** | • $O(n)$ linear runtime on bounded integers | • High space overhead if the range $k \gg n$<br>• Only applicable to discrete integer/string keys |

---

## 🎯 When to Use

- **Use Merge Sort when:** Stability is strictly required or when sorting external data (like large files or linked lists).
- **Use Quick Sort / Dual-Pivot QuickSort when:** Average-case cache performance and in-place memory optimization are paramount.
- **Use Insertion Sort / Timsort when:** The dataset is small ($n \le 64$) or already partially sorted.
- **Use Counting / Radix Sort when:** The key space is bounded and $k \le O(n)$.

---

## 🛠️ Essential Hands-On Problems

### 1. Merge Intervals
- **Pattern:** Interval Sorting & Overlap Consolidation
- **Complexity:** Time: $O(n \log n)$, Space: $O(n)$
- **Key Takeaway:** Sorting intervals by their start times allows a single-pass merge of adjacent overlaps.

### 2. Kth Largest Element in an Array (Quickselect)
- **Pattern:** Quickselect (Partitioning)
- **Complexity:** Time: $O(n)$ average / $O(n^2)$ worst, Space: $O(1)$
- **Key Takeaway:** Partial sorting via Hoare/Lomuto partitioning finds the $k$-th order statistic in linear average time without fully sorting the array.

### 3. Sort Colors (Dutch National Flag Problem)
- **Pattern:** Three-Way In-Place Partitioning (Two/Three Pointers)
- **Complexity:** Time: $O(n)$, Space: $O(1)$
- **Key Takeaway:** Partitioning an array of three distinct values (0, 1, 2) in a single pass using low, mid, and high pointers.

### 4. Meeting Rooms II
- **Pattern:** Two-Pointer Sweep / Priority Queue Sorting
- **Complexity:** Time: $O(n \log n)$, Space: $O(n)$
- **Key Takeaway:** Splitting and sorting start and end times separately to determine the peak simultaneous overlap count.

### 5. Custom Sort String (Sort by Frequency or Custom Comparator)
- **Pattern:** Bucket Sort / Custom Comparator
- **Complexity:** Time: $O(n + k)$, Space: $O(k)$
- **Key Takeaway:** Using frequency maps and custom sorting orders to build deterministic ordered sequences.
