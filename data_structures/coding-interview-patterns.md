# 🎯 Coding Interview Patterns Guide

A comprehensive reference for the most useful patterns to master for coding interviews.

---

## 📋 Table of Contents

1. [Two Pointers](#1-two-pointers)
2. [Sliding Window](#2-sliding-window)
3. [Fast & Slow Pointers](#3-fast--slow-pointers)
4. [Merge Intervals](#4-merge-intervals)
5. [Cyclic Sort](#5-cyclic-sort)
6. [In-place Reversal of LinkedList](#6-in-place-reversal-of-linkedlist)
7. [Tree Breadth First Search (BFS)](#7-tree-breadth-first-search-bfs)
8. [Tree Depth First Search (DFS)](#8-tree-depth-first-search-dfs)
9. [Two Heaps](#9-two-heaps)
10. [Subsets](#10-subsets)
11. [Modified Binary Search](#11-modified-binary-search)
12. [Bitwise XOR](#12-bitwise-xor)
13. [Top K Elements](#13-top-k-elements)
14. [K-way Merge](#14-k-way-merge)
15. [Dynamic Programming](#15-dynamic-programming)
16. [Backtracking](#16-backtracking)

---

## 1. Two Pointers

### 🎯 When to Use
- Array is sorted or you need to find pairs/triplets
- Need to find elements that meet certain criteria
- Reversing or comparing from both ends

### 🔍 Pattern Recognition
- "Find pair/triplet that sums to target"
- "Remove duplicates from sorted array"
- "Reverse string/array in place"
- "Check if string is palindrome"

### 📋 Algorithm Steps
1. **Initialize Pointers**: Set left=0, right=length-1
2. **Move Pointers**: Based on condition (sum comparison, etc.)
3. **Check Condition**: Compare current elements
4. **Update Result**: Store valid pairs/solutions
5. **Continue Until**: Pointers meet or cross

### 💻 Code Template
```csharp
public int[] TwoPointers(int[] arr, int target) 
{
    int left = 0, right = arr.Length - 1;
    
    while (left < right) 
    {
        int sum = arr[left] + arr[right];
        
        if (sum == target) 
        {
            return new int[] { left, right };
        }
        else if (sum < target) 
        {
            left++;  // Need larger sum
        }
        else 
        {
            right--; // Need smaller sum
        }
    }
    
    return new int[] { -1, -1 }; // Not found
}
```

### 🎲 Example Problems
- Two Sum II (sorted array)
- 3Sum
- Remove Duplicates from Sorted Array
- Container With Most Water
- Valid Palindrome

---

## 2. Sliding Window

### 🎯 When to Use
- Find subarray/substring with certain property
- Maximum/minimum in fixed or variable window
- All permutations/anagrams in string

### 🔍 Pattern Recognition
- "Find longest/shortest subarray with condition"
- "Maximum sum of k elements"
- "All anagrams in string"
- "Minimum window substring"

### 📋 Algorithm Steps
1. **Initialize Window**: Set start=0, track window state
2. **Expand Window**: Move end pointer, update state
3. **Contract Window**: When condition met, move start
4. **Update Result**: Track optimal window size/content
5. **Continue**: Until end reaches array end

### 💻 Code Template
```csharp
// Fixed Window Size
public int SlidingWindowFixed(int[] arr, int k) 
{
    int windowSum = 0, maxSum = 0;
    
    // Calculate first window
    for (int i = 0; i < k; i++) 
    {
        windowSum += arr[i];
    }
    maxSum = windowSum;
    
    // Slide window
    for (int i = k; i < arr.Length; i++) 
    {
        windowSum += arr[i] - arr[i - k]; // Add new, remove old
        maxSum = Math.Max(maxSum, windowSum);
    }
    
    return maxSum;
}

// Variable Window Size
public int SlidingWindowVariable(int[] arr, int target) 
{
    int start = 0, sum = 0, minLength = int.MaxValue;
    
    for (int end = 0; end < arr.Length; end++) 
    {
        sum += arr[end]; // Expand window
        
        // Contract window while condition is met
        while (sum >= target && start <= end) 
        {
            minLength = Math.Min(minLength, end - start + 1);
            sum -= arr[start++];
        }
    }
    
    return minLength == int.MaxValue ? 0 : minLength;
}
```

### 🎲 Example Problems
- Maximum Sum Subarray of Size K
- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Permutation in String
- Fruits into Baskets

---

## 3. Fast & Slow Pointers

### 🎯 When to Use
- Detect cycles in linked list or array
- Find middle element
- Determine if linked list is palindrome

### 🔍 Pattern Recognition
- "Detect cycle in linked list"
- "Find middle of linked list"
- "Find start of cycle"
- "Check if linked list is palindrome"

### 📋 Algorithm Steps
1. **Initialize Pointers**: slow=head, fast=head
2. **Move Pointers**: slow moves 1 step, fast moves 2 steps
3. **Check Meeting**: If fast meets slow, cycle exists
4. **Find Details**: Use additional logic for cycle start/middle
5. **Handle Edge Cases**: Null lists, single nodes

### 💻 Code Template
```csharp
// Cycle Detection
public bool HasCycle(ListNode head) 
{
    if (head == null || head.next == null) return false;
    
    ListNode slow = head, fast = head;
    
    while (fast != null && fast.next != null) 
    {
        slow = slow.next;        // Move 1 step
        fast = fast.next.next;   // Move 2 steps
        
        if (slow == fast) return true; // Cycle detected
    }
    
    return false;
}

// Find Middle
public ListNode FindMiddle(ListNode head) 
{
    ListNode slow = head, fast = head;
    
    while (fast != null && fast.next != null) 
    {
        slow = slow.next;
        fast = fast.next.next;
    }
    
    return slow; // Middle node
}
```

### 🎲 Example Problems
- Linked List Cycle
- Start of LinkedList Cycle
- Middle of the LinkedList
- Palindrome LinkedList
- Happy Number

---

## 4. Merge Intervals

### 🎯 When to Use
- Overlapping intervals problems
- Merge or insert intervals
- Find conflicts in scheduling

### 🔍 Pattern Recognition
- "Merge overlapping intervals"
- "Insert interval into sorted list"
- "Find minimum meeting rooms"
- "Employee free time"

### 📋 Algorithm Steps
1. **Sort Intervals**: By start time
2. **Initialize Result**: With first interval
3. **Compare Intervals**: Check for overlap
4. **Merge or Add**: Based on overlap condition
5. **Continue**: Through all intervals

### 💻 Code Template
```csharp
public class Interval 
{
    public int start, end;
    public Interval(int start, int end) 
    {
        this.start = start;
        this.end = end;
    }
}

public List<Interval> MergeIntervals(List<Interval> intervals) 
{
    if (intervals.Count < 2) return intervals;
    
    // Sort by start time
    intervals.Sort((a, b) => a.start.CompareTo(b.start));
    
    var merged = new List<Interval>();
    Interval current = intervals[0];
    
    for (int i = 1; i < intervals.Count; i++) 
    {
        Interval next = intervals[i];
        
        if (current.end >= next.start) 
        {
            // Overlapping intervals, merge them
            current.end = Math.Max(current.end, next.end);
        }
        else 
        {
            // No overlap, add current and move to next
            merged.Add(current);
            current = next;
        }
    }
    
    merged.Add(current); // Add last interval
    return merged;
}
```

### 🎲 Example Problems
- Merge Intervals
- Insert Interval
- Minimum Meeting Rooms
- Intervals Intersection
- Employee Free Time

---

## 5. Cyclic Sort

### 🎯 When to Use
- Array contains numbers in given range (1 to n)
- Find missing/duplicate numbers
- Array elements should be in specific positions

### 🔍 Pattern Recognition
- "Find missing number in array 1 to n"
- "Find duplicate number"
- "Array contains numbers 1 to n"
- "Find all missing numbers"

### 📋 Algorithm Steps
1. **Iterate Array**: Go through each position
2. **Check Position**: If number is in correct place
3. **Swap Elements**: Place number in correct position
4. **Repeat**: Until array is sorted
5. **Find Anomalies**: Missing/duplicate numbers

### 💻 Code Template
```csharp
public void CyclicSort(int[] nums) 
{
    int i = 0;
    
    while (i < nums.Length) 
    {
        int correctIndex = nums[i] - 1; // For 1-based array
        
        if (nums[i] != nums[correctIndex]) 
        {
            // Swap to place number in correct position
            int temp = nums[i];
            nums[i] = nums[correctIndex];
            nums[correctIndex] = temp;
        }
        else 
        {
            i++; // Move to next if already in correct place
        }
    }
}

public int FindMissingNumber(int[] nums) 
{
    int i = 0;
    int n = nums.Length;
    
    // Place each number in its correct position
    while (i < n) 
    {
        if (nums[i] < n && nums[i] != nums[nums[i]]) 
        {
            int temp = nums[i];
            nums[i] = nums[nums[i]];
            nums[temp] = temp;
        }
        else 
        {
            i++;
        }
    }
    
    // Find missing number
    for (i = 0; i < n; i++) 
    {
        if (nums[i] != i) return i;
    }
    
    return n; // All numbers present, missing is n
}
```

### 🎲 Example Problems
- Missing Number
- Find All Missing Numbers
- Find the Duplicate Number
- Find All Duplicates
- First Missing Positive

---

## 6. In-place Reversal of LinkedList

### 🎯 When to Use
- Reverse entire or part of linked list
- Reverse in groups
- Rotate linked list

### 🔍 Pattern Recognition
- "Reverse linked list"
- "Reverse nodes in k-group"
- "Reverse sublist"
- "Rotate linked list"

### 📋 Algorithm Steps
1. **Track Previous**: Keep reference to previous node
2. **Save Next**: Store next node before breaking link
3. **Reverse Link**: Point current to previous
4. **Move Pointers**: Advance all pointers
5. **Continue**: Until end of reversal range

### 💻 Code Template
```csharp
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

// Reverse entire list
public ListNode ReverseList(ListNode head) 
{
    ListNode prev = null, current = head;
    
    while (current != null) 
    {
        ListNode nextNode = current.next; // Save next
        current.next = prev;              // Reverse link
        prev = current;                   // Move prev
        current = nextNode;               // Move current
    }
    
    return prev; // New head
}

// Reverse between positions
public ListNode ReverseBetween(ListNode head, int left, int right) 
{
    if (head == null) return null;
    
    ListNode dummy = new ListNode(0);
    dummy.next = head;
    ListNode prev = dummy;
    
    // Move to start position
    for (int i = 0; i < left - 1; i++) 
    {
        prev = prev.next;
    }
    
    ListNode current = prev.next;
    
    // Reverse the sublist
    for (int i = 0; i < right - left; i++) 
    {
        ListNode nextNode = current.next;
        current.next = nextNode.next;
        nextNode.next = prev.next;
        prev.next = nextNode;
    }
    
    return dummy.next;
}
```

### 🎲 Example Problems
- Reverse Linked List
- Reverse Linked List II
- Reverse Nodes in k-Group
- Rotate List
- Swap Nodes in Pairs

---

## 7. Tree Breadth First Search (BFS)

### 🎯 When to Use
- Level-by-level tree traversal
- Find minimum depth/path
- Connect nodes at same level

### 🔍 Pattern Recognition
- "Level order traversal"
- "Find minimum depth"
- "Connect level order nodes"
- "Binary tree zigzag traversal"

### 📋 Algorithm Steps
1. **Initialize Queue**: Add root node
2. **Process Level**: Get all nodes at current level
3. **Add Children**: Enqueue children for next level
4. **Collect Results**: Store level information
5. **Continue**: Until queue is empty

### 💻 Code Template
```csharp
public List<List<int>> LevelOrder(TreeNode root) 
{
    var result = new List<List<int>>();
    if (root == null) return result;
    
    var queue = new Queue<TreeNode>();
    queue.Enqueue(root);
    
    while (queue.Count > 0) 
    {
        int levelSize = queue.Count;
        var currentLevel = new List<int>();
        
        for (int i = 0; i < levelSize; i++) 
        {
            TreeNode node = queue.Dequeue();
            currentLevel.Add(node.val);
            
            if (node.left != null) queue.Enqueue(node.left);
            if (node.right != null) queue.Enqueue(node.right);
        }
        
        result.Add(currentLevel);
    }
    
    return result;
}

public int MinDepth(TreeNode root) 
{
    if (root == null) return 0;
    
    var queue = new Queue<TreeNode>();
    queue.Enqueue(root);
    int depth = 1;
    
    while (queue.Count > 0) 
    {
        int levelSize = queue.Count;
        
        for (int i = 0; i < levelSize; i++) 
        {
            TreeNode node = queue.Dequeue();
            
            // If leaf node found, return depth
            if (node.left == null && node.right == null) 
            {
                return depth;
            }
            
            if (node.left != null) queue.Enqueue(node.left);
            if (node.right != null) queue.Enqueue(node.right);
        }
        
        depth++;
    }
    
    return depth;
}
```

### 🎲 Example Problems
- Binary Tree Level Order Traversal
- Minimum Depth of Binary Tree
- Connect Level Order Siblings
- Binary Tree Zigzag Level Order Traversal
- Level Averages in Binary Tree

---

## 8. Tree Depth First Search (DFS)

### 🎯 When to Use
- Traverse all paths from root to leaf
- Check tree properties (balanced, symmetric)
- Find paths with specific sum

### 🔍 Pattern Recognition
- "Find all root-to-leaf paths"
- "Check if tree is balanced/symmetric"
- "Path sum problems"
- "Maximum depth of tree"

### 📋 Algorithm Steps
1. **Base Case**: Handle null nodes
2. **Process Node**: Check current node value
3. **Recurse Left**: Explore left subtree
4. **Recurse Right**: Explore right subtree
5. **Backtrack**: Undo changes if needed

### 💻 Code Template
```csharp
// Basic DFS template
public bool DFS(TreeNode node, int targetSum, int currentSum) 
{
    if (node == null) return false;
    
    currentSum += node.val;
    
    // Leaf node check
    if (node.left == null && node.right == null) 
    {
        return currentSum == targetSum;
    }
    
    // Recurse on children
    return DFS(node.left, targetSum, currentSum) || 
           DFS(node.right, targetSum, currentSum);
}

// Path finding with backtracking
public List<List<int>> FindPaths(TreeNode root, int targetSum) 
{
    var result = new List<List<int>>();
    var currentPath = new List<int>();
    FindPathsHelper(root, targetSum, currentPath, result);
    return result;
}

private void FindPathsHelper(TreeNode node, int targetSum, 
                           List<int> currentPath, List<List<int>> result) 
{
    if (node == null) return;
    
    currentPath.Add(node.val); // Add to path
    
    if (node.left == null && node.right == null && targetSum == node.val) 
    {
        result.Add(new List<int>(currentPath)); // Found valid path
    }
    else 
    {
        FindPathsHelper(node.left, targetSum - node.val, currentPath, result);
        FindPathsHelper(node.right, targetSum - node.val, currentPath, result);
    }
    
    currentPath.RemoveAt(currentPath.Count - 1); // Backtrack
}
```

### 🎲 Example Problems
- Path Sum
- All Paths for a Sum
- Sum of Path Numbers
- Path With Given Sequence
- Count Paths for a Sum

---

## 9. Two Heaps

### 🎯 When to Use
- Find median in data stream
- Sliding window median
- Split array into two equal parts

### 🔍 Pattern Recognition
- "Find median in data stream"
- "Sliding window median"
- "Maximize capital"
- "Next interval"

### 📋 Algorithm Steps
1. **Maintain Two Heaps**: Max heap (smaller half), min heap (larger half)
2. **Balance Heaps**: Keep size difference ≤ 1
3. **Insert Elements**: Choose correct heap based on median
4. **Rebalance**: Move elements between heaps if needed
5. **Calculate Median**: From heap tops

### 💻 Code Template
```csharp
public class MedianFinder 
{
    private PriorityQueue<int, int> maxHeap; // Smaller half (max heap)
    private PriorityQueue<int, int> minHeap; // Larger half (min heap)
    
    public MedianFinder() 
    {
        maxHeap = new PriorityQueue<int, int>(Comparer<int>.Create((a, b) => b.CompareTo(a)));
        minHeap = new PriorityQueue<int, int>();
    }
    
    public void AddNum(int num) 
    {
        if (maxHeap.Count == 0 || num <= maxHeap.Peek()) 
        {
            maxHeap.Enqueue(num, num);
        }
        else 
        {
            minHeap.Enqueue(num, num);
        }
        
        // Rebalance heaps
        if (maxHeap.Count > minHeap.Count + 1) 
        {
            int val = maxHeap.Dequeue();
            minHeap.Enqueue(val, val);
        }
        else if (minHeap.Count > maxHeap.Count + 1) 
        {
            int val = minHeap.Dequeue();
            maxHeap.Enqueue(val, val);
        }
    }
    
    public double FindMedian() 
    {
        if (maxHeap.Count == minHeap.Count) 
        {
            return (maxHeap.Peek() + minHeap.Peek()) / 2.0;
        }
        
        return maxHeap.Count > minHeap.Count ? maxHeap.Peek() : minHeap.Peek();
    }
}
```

### 🎲 Example Problems
- Find Median from Data Stream
- Sliding Window Median
- IPO (Maximize Capital)
- Next Interval
- Maximize Capital

---

## 10. Subsets

### 🎯 When to Use
- Generate all combinations/permutations
- Backtracking problems
- Decision tree exploration

### 🔍 Pattern Recognition
- "Generate all subsets"
- "Find all permutations"
- "Generate balanced parentheses"
- "Letter combinations"

### 📋 Algorithm Steps
1. **Start with Empty**: Begin with empty subset/combination
2. **Make Choice**: Include or exclude current element
3. **Recurse**: Explore both choices
4. **Backtrack**: Undo choice and try next
5. **Collect Results**: Store valid combinations

### 💻 Code Template
```csharp
// Generate subsets
public List<List<int>> Subsets(int[] nums) 
{
    var result = new List<List<int>>();
    var currentSubset = new List<int>();
    GenerateSubsets(nums, 0, currentSubset, result);
    return result;
}

private void GenerateSubsets(int[] nums, int index, 
                           List<int> currentSubset, List<List<int>> result) 
{
    result.Add(new List<int>(currentSubset)); // Add current subset
    
    for (int i = index; i < nums.Length; i++) 
    {
        currentSubset.Add(nums[i]);              // Include element
        GenerateSubsets(nums, i + 1, currentSubset, result); // Recurse
        currentSubset.RemoveAt(currentSubset.Count - 1);     // Backtrack
    }
}

// Generate permutations
public List<List<int>> Permutations(int[] nums) 
{
    var result = new List<List<int>>();
    var currentPerm = new List<int>();
    var used = new bool[nums.Length];
    GeneratePermutations(nums, currentPerm, used, result);
    return result;
}

private void GeneratePermutations(int[] nums, List<int> currentPerm, 
                                bool[] used, List<List<int>> result) 
{
    if (currentPerm.Count == nums.Length) 
    {
        result.Add(new List<int>(currentPerm));
        return;
    }
    
    for (int i = 0; i < nums.Length; i++) 
    {
        if (!used[i]) 
        {
            used[i] = true;
            currentPerm.Add(nums[i]);
            GeneratePermutations(nums, currentPerm, used, result);
            currentPerm.RemoveAt(currentPerm.Count - 1);
            used[i] = false;
        }
    }
}
```

### 🎲 Example Problems
- Subsets
- Permutations
- Generate Parentheses
- Letter Combinations of Phone Number
- Word Search

---

## 11. Modified Binary Search

### 🎯 When to Use
- Search in rotated sorted array
- Find peak element
- Search in infinite array

### 🔍 Pattern Recognition
- "Search in rotated sorted array"
- "Find peak element"
- "Find minimum in rotated array"
- "Search in bitonic array"

### 📋 Algorithm Steps
1. **Identify Sorted Half**: Determine which half is sorted
2. **Check Target Range**: See if target is in sorted half
3. **Eliminate Half**: Choose which half to discard
4. **Update Bounds**: Adjust start/end pointers
5. **Continue**: Until target found or bounds invalid

### 💻 Code Template
```csharp
public int SearchRotated(int[] nums, int target) 
{
    int start = 0, end = nums.Length - 1;
    
    while (start <= end) 
    {
        int mid = start + (end - start) / 2;
        
        if (nums[mid] == target) return mid;
        
        // Left half is sorted
        if (nums[start] <= nums[mid]) 
        {
            if (target >= nums[start] && target < nums[mid]) 
            {
                end = mid - 1; // Target in left half
            }
            else 
            {
                start = mid + 1; // Target in right half
            }
        }
        // Right half is sorted
        else 
        {
            if (target > nums[mid] && target <= nums[end]) 
            {
                start = mid + 1; // Target in right half
            }
            else 
            {
                end = mid - 1; // Target in left half
            }
        }
    }
    
    return -1; // Not found
}

public int FindPeakElement(int[] nums) 
{
    int start = 0, end = nums.Length - 1;
    
    while (start < end) 
    {
        int mid = start + (end - start) / 2;
        
        if (nums[mid] > nums[mid + 1]) 
        {
            end = mid; // Peak is in left half (including mid)
        }
        else 
        {
            start = mid + 1; // Peak is in right half
        }
    }
    
    return start; // Peak index
}
```

### 🎲 Example Problems
- Search in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array
- Find Peak Element
- Search in Bitonic Array
- Search in Infinite Array

---

## 12. Bitwise XOR

### 🎯 When to Use
- Find missing/duplicate numbers
- Problems involving pairs
- Toggle bits or find unique elements

### 🔍 Pattern Recognition
- "Find single number"
- "Find missing number"
- "Two numbers appearing once"
- "Complement of base 10 number"

### 📋 Algorithm Steps
1. **XOR Property**: a ⊕ a = 0, a ⊕ 0 = a
2. **XOR All Elements**: Use property to cancel pairs
3. **Isolate Differences**: Use rightmost set bit
4. **Group Elements**: Based on bit differences
5. **Apply XOR**: To each group separately

### 💻 Code Template
```csharp
// Find single number (all others appear twice)
public int SingleNumber(int[] nums) 
{
    int result = 0;
    foreach (int num in nums) 
    {
        result ^= num; // XOR cancels out pairs
    }
    return result;
}

// Find two single numbers (all others appear twice)
public int[] SingleNumbers(int[] nums) 
{
    int xorAll = 0;
    foreach (int num in nums) 
    {
        xorAll ^= num;
    }
    
    // Find rightmost set bit
    int rightmostSetBit = xorAll & (-xorAll);
    
    int num1 = 0, num2 = 0;
    foreach (int num in nums) 
    {
        if ((num & rightmostSetBit) != 0) 
        {
            num1 ^= num; // Group 1
        }
        else 
        {
            num2 ^= num; // Group 2
        }
    }
    
    return new int[] { num1, num2 };
}

// Find missing number
public int MissingNumber(int[] nums) 
{
    int n = nums.Length;
    int xor1 = 0, xor2 = 0;
    
    // XOR all numbers from 0 to n
    for (int i = 0; i <= n; i++) 
    {
        xor1 ^= i;
    }
    
    // XOR all numbers in array
    foreach (int num in nums) 
    {
        xor2 ^= num;
    }
    
    return xor1 ^ xor2; // Missing number
}
```

### 🎲 Example Problems
- Single Number
- Single Number III
- Missing Number
- Find the Duplicate Number
- Complement of Base 10 Integer

---

## 13. Top K Elements

### 🎯 When to Use
- Find largest/smallest K elements
- K most frequent elements
- K closest points

### 🔍 Pattern Recognition
- "Find K largest/smallest elements"
- "K most frequent elements"
- "K closest points to origin"
- "Kth largest element"

### 📋 Algorithm Steps
1. **Use Min/Max Heap**: Based on requirement (K largest → min heap)
2. **Maintain Size K**: Keep heap size ≤ K
3. **Process Elements**: Add to heap and adjust size
4. **Extract Results**: Get elements from heap
5. **Handle Edge Cases**: Empty array, K > array size

### 💻 Code Template
```csharp
// Find K largest elements
public int[] FindKLargest(int[] nums, int k) 
{
    var minHeap = new PriorityQueue<int, int>(); // Min heap for K largest
    
    foreach (int num in nums) 
    {
        minHeap.Enqueue(num, num);
        
        if (minHeap.Count > k) 
        {
            minHeap.Dequeue(); // Remove smallest
        }
    }
    
    var result = new int[k];
    for (int i = k - 1; i >= 0; i--) 
    {
        result[i] = minHeap.Dequeue();
    }
    
    return result;
}

// Find K most frequent elements
public int[] TopKFrequent(int[] nums, int k) 
{
    var freqMap = new Dictionary<int, int>();
    foreach (int num in nums) 
    {
        freqMap[num] = freqMap.GetValueOrDefault(num, 0) + 1;
    }
    
    var minHeap = new PriorityQueue<int, int>();
    
    foreach (var kvp in freqMap) 
    {
        minHeap.Enqueue(kvp.Key, kvp.Value);
        
        if (minHeap.Count > k) 
        {
            minHeap.Dequeue();
        }
    }
    
    var result = new int[k];
    for (int i = 0; i < k; i++) 
    {
        result[i] = minHeap.Dequeue();
    }
    
    return result;
}
```

### 🎲 Example Problems
- Kth Largest Element in Array
- K Largest Elements
- Top K Frequent Elements
- K Closest Points to Origin
- Kth Smallest Element in Sorted Matrix

---

## 14. K-way Merge

### 🎯 When to Use
- Merge K sorted arrays/lists
- Find smallest range in K lists
- K pairs with smallest sums

### 🔍 Pattern Recognition
- "Merge K sorted lists"
- "Find smallest range covering K lists"
- "K pairs with smallest sums"
- "Kth smallest in sorted matrix"

### 📋 Algorithm Steps
1. **Use Min Heap**: Store elements with list index
2. **Initialize**: Add first element from each list
3. **Extract Minimum**: Get smallest element
4. **Add Next**: From same list as extracted element
5. **Continue**: Until all elements processed

### 💻 Code Template
```csharp
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

public ListNode MergeKLists(ListNode[] lists) 
{
    if (lists == null || lists.Length == 0) return null;
    
    var minHeap = new PriorityQueue<ListNode, int>();
    
    // Add first node from each list
    foreach (var list in lists) 
    {
        if (list != null) 
        {
            minHeap.Enqueue(list, list.val);
        }
    }
    
    var dummy = new ListNode(0);
    var current = dummy;
    
    while (minHeap.Count > 0) 
    {
        var node = minHeap.Dequeue();
        current.next = node;
        current = current.next;
        
        // Add next node from same list
        if (node.next != null) 
        {
            minHeap.Enqueue(node.next, node.next.val);
        }
    }
    
    return dummy.next;
}

// Find smallest range covering K lists
public int[] SmallestRange(IList<IList<int>> nums) 
{
    var minHeap = new PriorityQueue<(int val, int listIdx, int elemIdx), int>();
    int currentMax = int.MinValue;
    
    // Initialize heap with first element from each list
    for (int i = 0; i < nums.Count; i++) 
    {
        minHeap.Enqueue((nums[i][0], i, 0), nums[i][0]);
        currentMax = Math.Max(currentMax, nums[i][0]);
    }
    
    int[] result = { 0, int.MaxValue };
    
    while (minHeap.Count == nums.Count) 
    {
        var (val, listIdx, elemIdx) = minHeap.Dequeue();
        
        // Update result if current range is smaller
        if (currentMax - val < result[1] - result[0]) 
        {
            result[0] = val;
            result[1] = currentMax;
        }
        
        // Add next element from same list
        if (elemIdx + 1 < nums[listIdx].Count) 
        {
            int nextVal = nums[listIdx][elemIdx + 1];
            minHeap.Enqueue((nextVal, listIdx, elemIdx + 1), nextVal);
            currentMax = Math.Max(currentMax, nextVal);
        }
    }
    
    return result;
}
```

### 🎲 Example Problems
- Merge k Sorted Lists
- Kth Smallest Element in Sorted Matrix
- Smallest Range Covering Elements from K Lists
- Find K Pairs with Smallest Sums
- Merge K Sorted Arrays

---

## 15. Dynamic Programming

### 🎯 When to Use
- Optimization problems (min/max)
- Counting problems
- Decision problems with overlapping subproblems

### 🔍 Pattern Recognition
- "Find maximum/minimum"
- "Count number of ways"
- "Optimal strategy"
- "Yes/No decision with constraints"

### 📋 Algorithm Steps
1. **Identify Subproblems**: Break into smaller problems
2. **Define State**: What parameters define subproblem
3. **Find Recurrence**: Relationship between subproblems
4. **Handle Base Cases**: Trivial subproblems
5. **Optimize Space**: Use only necessary storage

### 💻 Code Template
```csharp
// 1D DP - Fibonacci-like problems
public int Fibonacci(int n) 
{
    if (n <= 1) return n;
    
    var dp = new int[n + 1];
    dp[0] = 0;
    dp[1] = 1;
    
    for (int i = 2; i <= n; i++) 
    {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    
    return dp[n];
}

// 2D DP - Grid problems
public int UniquePaths(int m, int n) 
{
    var dp = new int[m, n];
    
    // Initialize base cases
    for (int i = 0; i < m; i++) dp[i, 0] = 1;
    for (int j = 0; j < n; j++) dp[0, j] = 1;
    
    for (int i = 1; i < m; i++) 
    {
        for (int j = 1; j < n; j++) 
        {
            dp[i, j] = dp[i - 1, j] + dp[i, j - 1];
        }
    }
    
    return dp[m - 1, n - 1];
}

// Knapsack pattern
public int Knapsack(int[] weights, int[] values, int capacity) 
{
    int n = weights.Length;
    var dp = new int[n + 1, capacity + 1];
    
    for (int i = 1; i <= n; i++) 
    {
        for (int w = 1; w <= capacity; w++) 
        {
            if (weights[i - 1] <= w) 
            {
                dp[i, w] = Math.Max(
                    dp[i - 1, w], // Don't take item
                    dp[i - 1, w - weights[i - 1]] + values[i - 1] // Take item
                );
            }
            else 
            {
                dp[i, w] = dp[i - 1, w]; // Can't take item
            }
        }
    }
    
    return dp[n, capacity];
}

// Space-optimized version
public int KnapsackOptimized(int[] weights, int[] values, int capacity) 
{
    var dp = new int[capacity + 1];
    
    for (int i = 0; i < weights.Length; i++) 
    {
        for (int w = capacity; w >= weights[i]; w--) 
        {
            dp[w] = Math.Max(dp[w], dp[w - weights[i]] + values[i]);
        }
    }
    
    return dp[capacity];
}
```

### 🎲 Example Problems
- Climbing Stairs
- House Robber
- Coin Change
- Longest Increasing Subsequence
- 0/1 Knapsack

---

## 16. Backtracking

### 🎯 When to Use
- Generate all possible solutions
- Constraint satisfaction problems
- Decision tree exploration with pruning

### 🔍 Pattern Recognition
- "Find all solutions"
- "Generate all combinations/permutations"
- "Solve puzzle with constraints"
- "Path finding with obstacles"

### 📋 Algorithm Steps
1. **Choose**: Make a decision/choice
2. **Explore**: Recursively explore consequences
3. **Unchoose**: Backtrack if dead end
4. **Prune**: Skip invalid branches early
5. **Collect**: Store valid solutions

### 💻 Code Template
```csharp
// General backtracking template
public List<List<int>> Backtrack(int[] candidates, int target) 
{
    var result = new List<List<int>>();
    var currentCombination = new List<int>();
    BacktrackHelper(candidates, target, 0, currentCombination, result);
    return result;
}

private void BacktrackHelper(int[] candidates, int target, int startIndex,
                           List<int> currentCombination, List<List<int>> result) 
{
    // Base case - found valid solution
    if (target == 0) 
    {
        result.Add(new List<int>(currentCombination));
        return;
    }
    
    // Base case - invalid path
    if (target < 0) return;
    
    for (int i = startIndex; i < candidates.Length; i++) 
    {
        // Pruning - skip duplicates
        if (i > startIndex && candidates[i] == candidates[i - 1]) continue;
        
        // Choose
        currentCombination.Add(candidates[i]);
        
        // Explore
        BacktrackHelper(candidates, target - candidates[i], i + 1, 
                       currentCombination, result);
        
        // Unchoose (backtrack)
        currentCombination.RemoveAt(currentCombination.Count - 1);
    }
}

// N-Queens problem
public List<List<string>> SolveNQueens(int n) 
{
    var result = new List<List<string>>();
    var board = new char[n][];
    
    for (int i = 0; i < n; i++) 
    {
        board[i] = new char[n];
        for (int j = 0; j < n; j++) 
        {
            board[i][j] = '.';
        }
    }
    
    SolveNQueensHelper(board, 0, result);
    return result;
}

private void SolveNQueensHelper(char[][] board, int row, List<List<string>> result) 
{
    if (row == board.Length) 
    {
        result.Add(BoardToStrings(board));
        return;
    }
    
    for (int col = 0; col < board.Length; col++) 
    {
        if (IsValidPlacement(board, row, col)) 
        {
            board[row][col] = 'Q'; // Choose
            SolveNQueensHelper(board, row + 1, result); // Explore
            board[row][col] = '.'; // Unchoose
        }
    }
}

private bool IsValidPlacement(char[][] board, int row, int col) 
{
    int n = board.Length;
    
    // Check column
    for (int i = 0; i < row; i++) 
    {
        if (board[i][col] == 'Q') return false;
    }
    
    // Check diagonal
    for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) 
    {
        if (board[i][j] == 'Q') return false;
    }
    
    // Check anti-diagonal
    for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) 
    {
        if (board[i][j] == 'Q') return false;
    }
    
    return true;
}

private List<string> BoardToStrings(char[][] board) 
{
    var result = new List<string>();
    foreach (var row in board) 
    {
        result.Add(new string(row));
    }
    return result;
}
```

### 🎲 Example Problems
- N-Queens
- Sudoku Solver
- Word Search
- Combination Sum
- Generate Parentheses

---

## 🎯 Pattern Selection Guide

### By Problem Type
- **Array/String**: Two Pointers, Sliding Window, Modified Binary Search
- **Linked List**: Fast & Slow Pointers, In-place Reversal
- **Tree**: DFS, BFS, Two Heaps
- **Graph**: DFS, BFS, Union Find
- **Optimization**: Dynamic Programming, Backtracking
- **Sorting/Searching**: Modified Binary Search, Top K Elements

### By Time Complexity Goal
- **O(1)**: Hash Maps, Two Heaps (peek)
- **O(log n)**: Binary Search variants, Heaps
- **O(n)**: Two Pointers, Sliding Window, Linear scan
- **O(n log n)**: Merge Intervals, Top K Elements
- **O(n²)**: Nested loops, some DP problems

### By Space Complexity Goal
- **O(1)**: Two Pointers, Cyclic Sort, In-place operations
- **O(n)**: Hash Maps, DP arrays, Recursion
- **O(k)**: Top K Elements, Sliding Window

---

## 🏆 Interview Success Tips

1. **Pattern Recognition**: Practice identifying which pattern fits each problem
2. **Template Mastery**: Memorize and understand core templates
3. **Edge Case Handling**: Always consider null inputs, empty arrays, single elements
4. **Complexity Analysis**: Know time and space complexity for each pattern
5. **Multiple Solutions**: Start with brute force, then optimize using patterns
6. **Code Quality**: Write clean, readable code with meaningful variable names
7. **Test Cases**: Verify your solution with examples before submitting

---

**💡 Remember**: Patterns are tools, not rules. Some problems may require combining multiple patterns or creating variations. Practice recognizing which pattern(s) to apply and when to modify them for specific requirements.
