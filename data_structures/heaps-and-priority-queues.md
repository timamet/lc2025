# 📊 Heaps & Priority Queues

## 📋 Overview

**Heaps** are complete binary trees that maintain the heap property: in a max heap, parent nodes are greater than or equal to their children; in a min heap, parent nodes are less than or equal to their children. **Priority Queues** are abstract data types typically implemented using heaps.

---

## 🎯 Key Properties

- **Complete Binary Tree:** All levels filled except possibly the last, filled left to right
- **Heap Property:** Parent-child relationship maintains order (min/max)
- **Array Representation:** Efficient storage using array indices
- **Efficient Operations:** O(log n) insert/delete, O(1) peek
- **Self-Balancing:** Automatically maintains heap property

---

## 📊 Time & Space Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Insert | O(log n) | O(1) |
| Extract Min/Max | O(log n) | O(1) |
| Peek Min/Max | O(1) | O(1) |
| Build Heap | O(n) | O(1) |
| Heapify | O(log n) | O(1) |

---

## 🔍 Visual Representation

```
Min Heap:
        1
       / \
      3   6
     / \ / \
    5  9 8  12

Array: [1, 3, 6, 5, 9, 8, 12]
Index:  0  1  2  3  4  5   6

Parent of i: (i-1)/2
Left child of i: 2*i + 1
Right child of i: 2*i + 2

Max Heap:
       12
      /  \
     9    8
    / \  / \
   5  3 6   1

Array: [12, 9, 8, 5, 3, 6, 1]
```

---

## 🚀 Top 5 Essential Algorithms

### 1. Heap Sort

**Use Cases:** Sorting algorithms, in-place sorting, guaranteed O(n log n) performance

#### C# Implementation
```csharp
using System;

public class HeapSort 
{
    public static void Sort(int[] arr) 
    {
        int n = arr.Length;
        
        // Build max heap
        for (int i = n / 2 - 1; i >= 0; i--) 
        {
            Heapify(arr, n, i);
        }
        
        // Extract elements one by one
        for (int i = n - 1; i > 0; i--) 
        {
            // Move current root to end
            Swap(arr, 0, i);
            
            // Call heapify on reduced heap
            Heapify(arr, i, 0);
        }
    }
    
    private static void Heapify(int[] arr, int n, int i) 
    {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        
        // If left child is larger than root
        if (left < n && arr[left] > arr[largest]) 
        {
            largest = left;
        }
        
        // If right child is larger than largest so far
        if (right < n && arr[right] > arr[largest]) 
        {
            largest = right;
        }
        
        // If largest is not root
        if (largest != i) 
        {
            Swap(arr, i, largest);
            
            // Recursively heapify the affected sub-tree
            Heapify(arr, n, largest);
        }
    }
    
    private static void Swap(int[] arr, int i, int j) 
    {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    // Alternative iterative heapify
    public static void HeapifyIterative(int[] arr, int n, int i) 
    {
        while (true) 
        {
            int largest = i;
            int left = 2 * i + 1;
            int right = 2 * i + 2;
            
            if (left < n && arr[left] > arr[largest]) 
            {
                largest = left;
            }
            
            if (right < n && arr[right] > arr[largest]) 
            {
                largest = right;
            }
            
            if (largest == i) break;
            
            Swap(arr, i, largest);
            i = largest;
        }
    }
}

// Generic Min Heap Implementation
public class MinHeap<T> where T : IComparable<T> 
{
    private T[] heap;
    private int size;
    private int capacity;
    
    public MinHeap(int capacity = 10) 
    {
        this.capacity = capacity;
        this.heap = new T[capacity];
        this.size = 0;
    }
    
    public MinHeap(T[] array) 
    {
        this.capacity = array.Length;
        this.size = array.Length;
        this.heap = new T[capacity];
        Array.Copy(array, heap, size);
        
        // Build heap (heapify)
        for (int i = size / 2 - 1; i >= 0; i--) 
        {
            HeapifyDown(i);
        }
    }
    
    public int Count => size;
    public bool IsEmpty => size == 0;
    
    private int GetParentIndex(int index) => (index - 1) / 2;
    private int GetLeftChildIndex(int index) => 2 * index + 1;
    private int GetRightChildIndex(int index) => 2 * index + 2;
    
    private bool HasParent(int index) => GetParentIndex(index) >= 0;
    private bool HasLeftChild(int index) => GetLeftChildIndex(index) < size;
    private bool HasRightChild(int index) => GetRightChildIndex(index) < size;
    
    private T Parent(int index) => heap[GetParentIndex(index)];
    private T LeftChild(int index) => heap[GetLeftChildIndex(index)];
    private T RightChild(int index) => heap[GetRightChildIndex(index)];
    
    private void Swap(int index1, int index2) 
    {
        T temp = heap[index1];
        heap[index1] = heap[index2];
        heap[index2] = temp;
    }
    
    private void EnsureCapacity() 
    {
        if (size == capacity) 
        {
            capacity *= 2;
            T[] newHeap = new T[capacity];
            Array.Copy(heap, newHeap, size);
            heap = newHeap;
        }
    }
    
    public T Peek() 
    {
        if (IsEmpty) throw new InvalidOperationException("Heap is empty");
        return heap[0];
    }
    
    public T ExtractMin() 
    {
        if (IsEmpty) throw new InvalidOperationException("Heap is empty");
        
        T item = heap[0];
        heap[0] = heap[size - 1];
        size--;
        HeapifyDown(0);
        
        return item;
    }
    
    public void Insert(T item) 
    {
        EnsureCapacity();
        heap[size] = item;
        size++;
        HeapifyUp(size - 1);
    }
    
    private void HeapifyUp(int index) 
    {
        while (HasParent(index) && Parent(index).CompareTo(heap[index]) > 0) 
        {
            Swap(GetParentIndex(index), index);
            index = GetParentIndex(index);
        }
    }
    
    private void HeapifyDown(int index) 
    {
        while (HasLeftChild(index)) 
        {
            int smallerChildIndex = GetLeftChildIndex(index);
            
            if (HasRightChild(index) && 
                RightChild(index).CompareTo(LeftChild(index)) < 0) 
            {
                smallerChildIndex = GetRightChildIndex(index);
            }
            
            if (heap[index].CompareTo(heap[smallerChildIndex]) < 0) 
            {
                break;
            }
            
            Swap(index, smallerChildIndex);
            index = smallerChildIndex;
        }
    }
    
    public T[] ToArray() 
    {
        T[] result = new T[size];
        Array.Copy(heap, result, size);
        return result;
    }
}

// Max Heap Implementation
public class MaxHeap<T> where T : IComparable<T> 
{
    private T[] heap;
    private int size;
    private int capacity;
    
    public MaxHeap(int capacity = 10) 
    {
        this.capacity = capacity;
        this.heap = new T[capacity];
        this.size = 0;
    }
    
    public int Count => size;
    public bool IsEmpty => size == 0;
    
    private int GetParentIndex(int index) => (index - 1) / 2;
    private int GetLeftChildIndex(int index) => 2 * index + 1;
    private int GetRightChildIndex(int index) => 2 * index + 2;
    
    private bool HasParent(int index) => GetParentIndex(index) >= 0;
    private bool HasLeftChild(int index) => GetLeftChildIndex(index) < size;
    private bool HasRightChild(int index) => GetRightChildIndex(index) < size;
    
    private T Parent(int index) => heap[GetParentIndex(index)];
    private T LeftChild(int index) => heap[GetLeftChildIndex(index)];
    private T RightChild(int index) => heap[GetRightChildIndex(index)];
    
    private void Swap(int index1, int index2) 
    {
        T temp = heap[index1];
        heap[index1] = heap[index2];
        heap[index2] = temp;
    }
    
    private void EnsureCapacity() 
    {
        if (size == capacity) 
        {
            capacity *= 2;
            T[] newHeap = new T[capacity];
            Array.Copy(heap, newHeap, size);
            heap = newHeap;
        }
    }
    
    public T Peek() 
    {
        if (IsEmpty) throw new InvalidOperationException("Heap is empty");
        return heap[0];
    }
    
    public T ExtractMax() 
    {
        if (IsEmpty) throw new InvalidOperationException("Heap is empty");
        
        T item = heap[0];
        heap[0] = heap[size - 1];
        size--;
        HeapifyDown(0);
        
        return item;
    }
    
    public void Insert(T item) 
    {
        EnsureCapacity();
        heap[size] = item;
        size++;
        HeapifyUp(size - 1);
    }
    
    private void HeapifyUp(int index) 
    {
        while (HasParent(index) && Parent(index).CompareTo(heap[index]) < 0) 
        {
            Swap(GetParentIndex(index), index);
            index = GetParentIndex(index);
        }
    }
    
    private void HeapifyDown(int index) 
    {
        while (HasLeftChild(index)) 
        {
            int largerChildIndex = GetLeftChildIndex(index);
            
            if (HasRightChild(index) && 
                RightChild(index).CompareTo(LeftChild(index)) > 0) 
            {
                largerChildIndex = GetRightChildIndex(index);
            }
            
            if (heap[index].CompareTo(heap[largerChildIndex]) > 0) 
            {
                break;
            }
            
            Swap(index, largerChildIndex);
            index = largerChildIndex;
        }
    }
}
```

---

### 2. K Largest/Smallest Elements

**Use Cases:** Top-K problems, finding extremes, data stream processing

#### C# Implementation
```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class KLargestSmallest 
{
    // Find K largest elements using min heap
    public static int[] FindKLargest(int[] nums, int k) 
    {
        if (k <= 0 || k > nums.Length) return new int[0];
        
        var minHeap = new PriorityQueue<int, int>();
        
        foreach (int num in nums) 
        {
            if (minHeap.Count < k) 
            {
                minHeap.Enqueue(num, num);
            }
            else if (num > minHeap.Peek()) 
            {
                minHeap.Dequeue();
                minHeap.Enqueue(num, num);
            }
        }
        
        int[] result = new int[k];
        for (int i = k - 1; i >= 0; i--) 
        {
            result[i] = minHeap.Dequeue();
        }
        
        return result;
    }
    
    // Find K smallest elements using max heap
    public static int[] FindKSmallest(int[] nums, int k) 
    {
        if (k <= 0 || k > nums.Length) return new int[0];
        
        var maxHeap = new PriorityQueue<int, int>(Comparer<int>.Create((a, b) => b.CompareTo(a)));
        
        foreach (int num in nums) 
        {
            if (maxHeap.Count < k) 
            {
                maxHeap.Enqueue(num, num);
            }
            else if (num < maxHeap.Peek()) 
            {
                maxHeap.Dequeue();
                maxHeap.Enqueue(num, num);
            }
        }
        
        int[] result = new int[k];
        for (int i = k - 1; i >= 0; i--) 
        {
            result[i] = maxHeap.Dequeue();
        }
        
        return result;
    }
    
    // Kth largest element in array
    public static int FindKthLargest(int[] nums, int k) 
    {
        var minHeap = new PriorityQueue<int, int>();
        
        foreach (int num in nums) 
        {
            if (minHeap.Count < k) 
            {
                minHeap.Enqueue(num, num);
            }
            else if (num > minHeap.Peek()) 
            {
                minHeap.Dequeue();
                minHeap.Enqueue(num, num);
            }
        }
        
        return minHeap.Peek();
    }
    
    // Kth largest using QuickSelect (more efficient)
    public static int FindKthLargestQuickSelect(int[] nums, int k) 
    {
        return QuickSelect(nums, 0, nums.Length - 1, nums.Length - k);
    }
    
    private static int QuickSelect(int[] nums, int left, int right, int k) 
    {
        if (left == right) return nums[left];
        
        int pivotIndex = Partition(nums, left, right);
        
        if (k == pivotIndex) 
        {
            return nums[k];
        }
        else if (k < pivotIndex) 
        {
            return QuickSelect(nums, left, pivotIndex - 1, k);
        }
        else 
        {
            return QuickSelect(nums, pivotIndex + 1, right, k);
        }
    }
    
    private static int Partition(int[] nums, int left, int right) 
    {
        int pivot = nums[right];
        int i = left;
        
        for (int j = left; j < right; j++) 
        {
            if (nums[j] <= pivot) 
            {
                Swap(nums, i, j);
                i++;
            }
        }
        
        Swap(nums, i, right);
        return i;
    }
    
    private static void Swap(int[] nums, int i, int j) 
    {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    
    // K closest points to origin
    public static int[][] KClosest(int[][] points, int k) 
    {
        var maxHeap = new PriorityQueue<int[], int>(
            Comparer<int>.Create((a, b) => b.CompareTo(a))
        );
        
        foreach (var point in points) 
        {
            int distanceSquared = point[0] * point[0] + point[1] * point[1];
            
            if (maxHeap.Count < k) 
            {
                maxHeap.Enqueue(point, distanceSquared);
            }
            else if (distanceSquared < maxHeap.Priority) 
            {
                maxHeap.Dequeue();
                maxHeap.Enqueue(point, distanceSquared);
            }
        }
        
        int[][] result = new int[k][];
        for (int i = 0; i < k; i++) 
        {
            result[i] = maxHeap.Dequeue();
        }
        
        return result;
    }
    
    // Top K frequent elements
    public static int[] TopKFrequent(int[] nums, int k) 
    {
        var frequency = new Dictionary<int, int>();
        
        foreach (int num in nums) 
        {
            frequency[num] = frequency.GetValueOrDefault(num, 0) + 1;
        }
        
        var minHeap = new PriorityQueue<int, int>();
        
        foreach (var kvp in frequency) 
        {
            if (minHeap.Count < k) 
            {
                minHeap.Enqueue(kvp.Key, kvp.Value);
            }
            else if (kvp.Value > minHeap.Priority) 
            {
                minHeap.Dequeue();
                minHeap.Enqueue(kvp.Key, kvp.Value);
            }
        }
        
        int[] result = new int[k];
        for (int i = k - 1; i >= 0; i--) 
        {
            result[i] = minHeap.Dequeue();
        }
        
        return result;
    }
}

// Custom Priority Queue Extension
public static class PriorityQueueExtensions 
{
    public static int Priority<TElement, TPriority>(this PriorityQueue<TElement, TPriority> pq) 
        where TPriority : IComparable<TPriority>
    {
        // Note: This is a conceptual extension. 
        // The actual implementation would need to store priority separately
        // or use a custom comparer that exposes the priority.
        throw new NotImplementedException("Priority property not directly available in .NET PriorityQueue");
    }
}
```

---

### 3. Merge K Sorted Lists/Arrays

**Use Cases:** External sorting, merging data streams, distributed computing

#### C# Implementation
```csharp
using System;
using System.Collections.Generic;

public class ListNode 
{
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null) 
    {
        this.val = val;
        this.next = next;
    }
}

public class MergeKSorted 
{
    // Merge K sorted linked lists using min heap
    public static ListNode MergeKLists(ListNode[] lists) 
    {
        if (lists == null || lists.Length == 0) return null;
        
        var minHeap = new PriorityQueue<ListNode, int>();
        
        // Add first node of each list to heap
        for (int i = 0; i < lists.Length; i++) 
        {
            if (lists[i] != null) 
            {
                minHeap.Enqueue(lists[i], lists[i].val);
            }
        }
        
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        
        while (minHeap.Count > 0) 
        {
            ListNode node = minHeap.Dequeue();
            current.next = node;
            current = current.next;
            
            if (node.next != null) 
            {
                minHeap.Enqueue(node.next, node.next.val);
            }
        }
        
        return dummy.next;
    }
    
    // Merge K sorted lists using divide and conquer
    public static ListNode MergeKListsDivideConquer(ListNode[] lists) 
    {
        if (lists == null || lists.Length == 0) return null;
        if (lists.Length == 1) return lists[0];
        
        return MergeKListsHelper(lists, 0, lists.Length - 1);
    }
    
    private static ListNode MergeKListsHelper(ListNode[] lists, int start, int end) 
    {
        if (start == end) return lists[start];
        if (start + 1 == end) return MergeTwoLists(lists[start], lists[end]);
        
        int mid = start + (end - start) / 2;
        ListNode left = MergeKListsHelper(lists, start, mid);
        ListNode right = MergeKListsHelper(lists, mid + 1, end);
        
        return MergeTwoLists(left, right);
    }
    
    private static ListNode MergeTwoLists(ListNode l1, ListNode l2) 
    {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        
        while (l1 != null && l2 != null) 
        {
            if (l1.val <= l2.val) 
            {
                current.next = l1;
                l1 = l1.next;
            }
            else 
            {
                current.next = l2;
                l2 = l2.next;
            }
            current = current.next;
        }
        
        current.next = l1 ?? l2;
        return dummy.next;
    }
    
    // Merge K sorted arrays
    public static int[] MergeKArrays(int[][] arrays) 
    {
        if (arrays == null || arrays.Length == 0) return new int[0];
        
        var minHeap = new PriorityQueue<(int value, int arrayIndex, int elementIndex), int>();
        int totalSize = 0;
        
        // Add first element of each array to heap
        for (int i = 0; i < arrays.Length; i++) 
        {
            if (arrays[i].Length > 0) 
            {
                minHeap.Enqueue((arrays[i][0], i, 0), arrays[i][0]);
                totalSize += arrays[i].Length;
            }
        }
        
        int[] result = new int[totalSize];
        int resultIndex = 0;
        
        while (minHeap.Count > 0) 
        {
            var (value, arrayIndex, elementIndex) = minHeap.Dequeue();
            result[resultIndex++] = value;
            
            // Add next element from the same array
            if (elementIndex + 1 < arrays[arrayIndex].Length) 
            {
                int nextValue = arrays[arrayIndex][elementIndex + 1];
                minHeap.Enqueue((nextValue, arrayIndex, elementIndex + 1), nextValue);
            }
        }
        
        return result;
    }
    
    // Merge K sorted arrays using divide and conquer
    public static int[] MergeKArraysDivideConquer(int[][] arrays) 
    {
        if (arrays == null || arrays.Length == 0) return new int[0];
        if (arrays.Length == 1) return arrays[0];
        
        return MergeKArraysHelper(arrays, 0, arrays.Length - 1);
    }
    
    private static int[] MergeKArraysHelper(int[][] arrays, int start, int end) 
    {
        if (start == end) return arrays[start];
        if (start + 1 == end) return MergeTwoArrays(arrays[start], arrays[end]);
        
        int mid = start + (end - start) / 2;
        int[] left = MergeKArraysHelper(arrays, start, mid);
        int[] right = MergeKArraysHelper(arrays, mid + 1, end);
        
        return MergeTwoArrays(left, right);
    }
    
    private static int[] MergeTwoArrays(int[] arr1, int[] arr2) 
    {
        int[] merged = new int[arr1.Length + arr2.Length];
        int i = 0, j = 0, k = 0;
        
        while (i < arr1.Length && j < arr2.Length) 
        {
            if (arr1[i] <= arr2[j]) 
            {
                merged[k++] = arr1[i++];
            }
            else 
            {
                merged[k++] = arr2[j++];
            }
        }
        
        while (i < arr1.Length) merged[k++] = arr1[i++];
        while (j < arr2.Length) merged[k++] = arr2[j++];
        
        return merged;
    }
    
    // Smallest range covering elements from K lists
    public static int[] SmallestRange(IList<IList<int>> nums) 
    {
        var minHeap = new PriorityQueue<(int value, int listIndex, int elementIndex), int>();
        int maxValue = int.MinValue;
        
        // Add first element of each list
        for (int i = 0; i < nums.Count; i++) 
        {
            if (nums[i].Count > 0) 
            {
                minHeap.Enqueue((nums[i][0], i, 0), nums[i][0]);
                maxValue = Math.Max(maxValue, nums[i][0]);
            }
        }
        
        int rangeStart = 0, rangeEnd = int.MaxValue;
        
        while (minHeap.Count == nums.Count) 
        {
            var (minValue, listIndex, elementIndex) = minHeap.Dequeue();
            
            // Update range if current is smaller
            if (maxValue - minValue < rangeEnd - rangeStart) 
            {
                rangeStart = minValue;
                rangeEnd = maxValue;
            }
            
            // Add next element from the same list
            if (elementIndex + 1 < nums[listIndex].Count) 
            {
                int nextValue = nums[listIndex][elementIndex + 1];
                minHeap.Enqueue((nextValue, listIndex, elementIndex + 1), nextValue);
                maxValue = Math.Max(maxValue, nextValue);
            }
        }
        
        return new int[] { rangeStart, rangeEnd };
    }
}
```

---

### 4. Running Median (Median Finder)

**Use Cases:** Data stream processing, statistics, sliding window problems

#### C# Implementation
```csharp
using System;
using System.Collections.Generic;

public class MedianFinder 
{
    private PriorityQueue<int, int> maxHeap; // Lower half (max heap)
    private PriorityQueue<int, int> minHeap; // Upper half (min heap)
    
    public MedianFinder() 
    {
        maxHeap = new PriorityQueue<int, int>(Comparer<int>.Create((a, b) => b.CompareTo(a)));
        minHeap = new PriorityQueue<int, int>();
    }
    
    public void AddNum(int num) 
    {
        // Add to max heap (lower half)
        maxHeap.Enqueue(num, num);
        
        // Balance: move largest from lower half to upper half
        minHeap.Enqueue(maxHeap.Peek(), maxHeap.Peek());
        maxHeap.Dequeue();
        
        // Maintain size property: maxHeap size >= minHeap size
        if (maxHeap.Count < minHeap.Count) 
        {
            maxHeap.Enqueue(minHeap.Peek(), minHeap.Peek());
            minHeap.Dequeue();
        }
    }
    
    public double FindMedian() 
    {
        if (maxHeap.Count > minHeap.Count) 
        {
            return maxHeap.Peek();
        }
        
        return (maxHeap.Peek() + minHeap.Peek()) / 2.0;
    }
}

public class SlidingWindowMedian 
{
    private SortedDictionary<int, int> lowerHalf;
    private SortedDictionary<int, int> upperHalf;
    private int lowerSize, upperSize;
    
    public SlidingWindowMedian() 
    {
        lowerHalf = new SortedDictionary<int, int>();
        upperHalf = new SortedDictionary<int, int>();
        lowerSize = upperSize = 0;
    }
    
    public double[] MedianSlidingWindow(int[] nums, int k) 
    {
        double[] result = new double[nums.Length - k + 1];
        
        for (int i = 0; i < nums.Length; i++) 
        {
            AddNumber(nums[i]);
            
            if (i >= k) 
            {
                RemoveNumber(nums[i - k]);
            }
            
            if (i >= k - 1) 
            {
                result[i - k + 1] = GetMedian();
            }
        }
        
        return result;
    }
    
    private void AddNumber(int num) 
    {
        if (lowerSize <= upperSize) 
        {
            AddToDict(upperHalf, num);
            upperSize++;
            
            if (upperHalf.Count > 0) 
            {
                int minUpper = upperHalf.Keys.First();
                RemoveFromDict(upperHalf, minUpper);
                upperSize--;
                AddToDict(lowerHalf, minUpper);
                lowerSize++;
            }
        }
        else 
        {
            AddToDict(lowerHalf, num);
            lowerSize++;
            
            if (lowerHalf.Count > 0) 
            {
                int maxLower = lowerHalf.Keys.Last();
                RemoveFromDict(lowerHalf, maxLower);
                lowerSize--;
                AddToDict(upperHalf, maxLower);
                upperSize++;
            }
        }
    }
    
    private void RemoveNumber(int num) 
    {
        if (lowerHalf.ContainsKey(num)) 
        {
            RemoveFromDict(lowerHalf, num);
            lowerSize--;
        }
        else 
        {
            RemoveFromDict(upperHalf, num);
            upperSize--;
        }
        
        Balance();
    }
    
    private void Balance() 
    {
        if (lowerSize > upperSize + 1) 
        {
            int maxLower = lowerHalf.Keys.Last();
            RemoveFromDict(lowerHalf, maxLower);
            lowerSize--;
            AddToDict(upperHalf, maxLower);
            upperSize++;
        }
        else if (upperSize > lowerSize + 1) 
        {
            int minUpper = upperHalf.Keys.First();
            RemoveFromDict(upperHalf, minUpper);
            upperSize--;
            AddToDict(lowerHalf, minUpper);
            lowerSize++;
        }
    }
    
    private double GetMedian() 
    {
        if (lowerSize == upperSize) 
        {
            return ((long)lowerHalf.Keys.Last() + upperHalf.Keys.First()) / 2.0;
        }
        else if (lowerSize > upperSize) 
        {
            return lowerHalf.Keys.Last();
        }
        else 
        {
            return upperHalf.Keys.First();
        }
    }
    
    private void AddToDict(SortedDictionary<int, int> dict, int num) 
    {
        dict[num] = dict.GetValueOrDefault(num, 0) + 1;
    }
    
    private void RemoveFromDict(SortedDictionary<int, int> dict, int num) 
    {
        dict[num]--;
        if (dict[num] == 0) 
        {
            dict.Remove(num);
        }
    }
}

// Alternative implementation using custom balanced BST
public class MedianFinderBST 
{
    private class TreeNode 
    {
        public int val;
        public int count;
        public int leftSize;
        public TreeNode left, right;
        
        public TreeNode(int val) 
        {
            this.val = val;
            this.count = 1;
            this.leftSize = 0;
        }
    }
    
    private TreeNode root;
    private int totalCount;
    
    public MedianFinderBST() 
    {
        root = null;
        totalCount = 0;
    }
    
    public void AddNum(int num) 
    {
        root = Insert(root, num);
        totalCount++;
    }
    
    private TreeNode Insert(TreeNode node, int val) 
    {
        if (node == null) return new TreeNode(val);
        
        if (val == node.val) 
        {
            node.count++;
        }
        else if (val < node.val) 
        {
            node.leftSize++;
            node.left = Insert(node.left, val);
        }
        else 
        {
            node.right = Insert(node.right, val);
        }
        
        return node;
    }
    
    public double FindMedian() 
    {
        if (totalCount % 2 == 1) 
        {
            return FindKth(root, totalCount / 2 + 1);
        }
        else 
        {
            int k1 = totalCount / 2;
            int k2 = totalCount / 2 + 1;
            return (FindKth(root, k1) + FindKth(root, k2)) / 2.0;
        }
    }
    
    private int FindKth(TreeNode node, int k) 
    {
        if (node == null) return -1;
        
        if (k <= node.leftSize) 
        {
            return FindKth(node.left, k);
        }
        else if (k <= node.leftSize + node.count) 
        {
            return node.val;
        }
        else 
        {
            return FindKth(node.right, k - node.leftSize - node.count);
        }
    }
}
```

---

### 5. Dijkstra's Algorithm

**Use Cases:** Shortest path algorithms, network routing, GPS navigation

#### C# Implementation
```csharp
using System;
using System.Collections.Generic;

public class DijkstraAlgorithm 
{
    public class Edge 
    {
        public int To { get; set; }
        public int Weight { get; set; }
        
        public Edge(int to, int weight) 
        {
            To = to;
            Weight = weight;
        }
    }
    
    public static int[] Dijkstra(List<List<Edge>> graph, int start) 
    {
        int n = graph.Count;
        int[] distances = new int[n];
        Array.Fill(distances, int.MaxValue);
        distances[start] = 0;
        
        var minHeap = new PriorityQueue<int, int>();
        minHeap.Enqueue(start, 0);
        
        while (minHeap.Count > 0) 
        {
            int u = minHeap.Dequeue();
            
            foreach (var edge in graph[u]) 
            {
                int v = edge.To;
                int weight = edge.Weight;
                
                if (distances[u] != int.MaxValue && 
                    distances[u] + weight < distances[v]) 
                {
                    distances[v] = distances[u] + weight;
                    minHeap.Enqueue(v, distances[v]);
                }
            }
        }
        
        return distances;
    }
    
    public static (int[] distances, int[] previous) DijkstraWithPath(List<List<Edge>> graph, int start) 
    {
        int n = graph.Count;
        int[] distances = new int[n];
        int[] previous = new int[n];
        bool[] visited = new bool[n];
        
        Array.Fill(distances, int.MaxValue);
        Array.Fill(previous, -1);
        distances[start] = 0;
        
        var minHeap = new PriorityQueue<int, int>();
        minHeap.Enqueue(start, 0);
        
        while (minHeap.Count > 0) 
        {
            int u = minHeap.Dequeue();
            
            if (visited[u]) continue;
            visited[u] = true;
            
            foreach (var edge in graph[u]) 
            {
                int v = edge.To;
                int weight = edge.Weight;
                
                if (!visited[v] && distances[u] != int.MaxValue && 
                    distances[u] + weight < distances[v]) 
                {
                    distances[v] = distances[u] + weight;
                    previous[v] = u;
                    minHeap.Enqueue(v, distances[v]);
                }
            }
        }
        
        return (distances, previous);
    }
    
    public static List<int> GetShortestPath(int[] previous, int start, int end) 
    {
        var path = new List<int>();
        int current = end;
        
        while (current != -1) 
        {
            path.Add(current);
            current = previous[current];
        }
        
        if (path[path.Count - 1] != start) 
        {
            return new List<int>(); // No path exists
        }
        
        path.Reverse();
        return path;
    }
    
    // Network delay time problem
    public static int NetworkDelayTime(int[][] times, int n, int k) 
    {
        var graph = new List<List<Edge>>();
        for (int i = 0; i <= n; i++) 
        {
            graph.Add(new List<Edge>());
        }
        
        foreach (var time in times) 
        {
            graph[time[0]].Add(new Edge(time[1], time[2]));
        }
        
        int[] distances = Dijkstra(graph, k);
        
        int maxDelay = 0;
        for (int i = 1; i <= n; i++) 
        {
            if (distances[i] == int.MaxValue) return -1;
            maxDelay = Math.Max(maxDelay, distances[i]);
        }
        
        return maxDelay;
    }
    
    // Cheapest flights within K stops
    public static int FindCheapestPrice(int n, int[][] flights, int src, int dst, int k) 
    {
        var graph = new List<List<Edge>>();
        for (int i = 0; i < n; i++) 
        {
            graph.Add(new List<Edge>());
        }
        
        foreach (var flight in flights) 
        {
            graph[flight[0]].Add(new Edge(flight[1], flight[2]));
        }
        
        // (cost, node, stops)
        var minHeap = new PriorityQueue<(int cost, int node, int stops), int>();
        minHeap.Enqueue((0, src, 0), 0);
        
        var visited = new Dictionary<(int node, int stops), int>();
        
        while (minHeap.Count > 0) 
        {
            var (cost, node, stops) = minHeap.Dequeue();
            
            if (node == dst) return cost;
            if (stops > k) continue;
            
            var key = (node, stops);
            if (visited.ContainsKey(key) && visited[key] <= cost) continue;
            visited[key] = cost;
            
            foreach (var edge in graph[node]) 
            {
                int nextCost = cost + edge.Weight;
                minHeap.Enqueue((nextCost, edge.To, stops + 1), nextCost);
            }
        }
        
        return -1;
    }
    
    // Path with minimum effort
    public static int MinimumEffortPath(int[][] heights) 
    {
        int m = heights.Length, n = heights[0].Length;
        int[][] directions = { new int[] {0, 1}, new int[] {1, 0}, 
                              new int[] {0, -1}, new int[] {-1, 0} };
        
        var minHeap = new PriorityQueue<(int effort, int row, int col), int>();
        var efforts = new int[m, n];
        
        for (int i = 0; i < m; i++) 
        {
            for (int j = 0; j < n; j++) 
            {
                efforts[i, j] = int.MaxValue;
            }
        }
        
        efforts[0, 0] = 0;
        minHeap.Enqueue((0, 0, 0), 0);
        
        while (minHeap.Count > 0) 
        {
            var (effort, row, col) = minHeap.Dequeue();
            
            if (row == m - 1 && col == n - 1) return effort;
            if (effort > efforts[row, col]) continue;
            
            foreach (var dir in directions) 
            {
                int newRow = row + dir[0];
                int newCol = col + dir[1];
                
                if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n) 
                {
                    int newEffort = Math.Max(effort, 
                        Math.Abs(heights[newRow][newCol] - heights[row][col]));
                    
                    if (newEffort < efforts[newRow, newCol]) 
                    {
                        efforts[newRow, newCol] = newEffort;
                        minHeap.Enqueue((newEffort, newRow, newCol), newEffort);
                    }
                }
            }
        }
        
        return 0;
    }
}
```

---

## 🎯 Common Patterns & Tips

### Pattern Recognition
- **Heap Sort:** Use for guaranteed O(n log n) sorting with O(1) space
- **K Problems:** Use min/max heap to maintain K elements efficiently
- **Merge Operations:** Use heap for merging multiple sorted sequences
- **Median Finding:** Use two heaps (max heap for lower half, min heap for upper half)
- **Shortest Path:** Use min heap in Dijkstra's algorithm for optimal performance

### Optimization Tips
1. **Choose right heap type:** Min heap for smallest elements, max heap for largest
2. **Use array representation:** More cache-friendly than pointer-based trees
3. **Build heap in O(n):** Use bottom-up heapify instead of repeated insertions
4. **Consider QuickSelect:** For one-time Kth element finding, may be faster than heap
5. **Balance heap sizes:** In median finding, keep size difference ≤ 1

### Common Pitfalls
- **Index calculations** - ensure correct parent/child index formulas
- **Heap property violations** - always heapify after modifications
- **Empty heap operations** - check for empty heap before peek/extract
- **Integer overflow** in priority calculations
- **Comparison function errors** in custom priority queues

---

## 📚 Related LeetCode Problems

### Easy
- [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
- [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)
- [Relative Ranks](https://leetcode.com/problems/relative-ranks/)

### Medium
- [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
- [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)
- [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

### Hard
- [Sliding Window Median](https://leetcode.com/problems/sliding-window-median/)
- [IPO](https://leetcode.com/problems/ipo/)
- [Smallest Range Covering Elements from K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/)

---

[← Back to Main Guide](./README.md)
