# 🔗 Linked Lists

## 📋 Overview

**Linked Lists** are linear data structures where elements (nodes) are stored in sequence, but not in contiguous memory locations. Each node contains data and a reference (or link) to the next node in the sequence.

---

## 🎯 Key Properties

- **Dynamic Size:** Can grow or shrink during runtime
- **Sequential Access:** Must traverse from head to reach a specific node
- **Efficient Insertion/Deletion:** O(1) at known positions
- **Memory Efficiency:** No wasted memory (unlike arrays with fixed size)
- **Cache Performance:** Poor due to non-contiguous memory layout

---

## 📊 Time & Space Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Access/Search | O(n) | O(1) |
| Insertion (at head) | O(1) | O(1) |
| Insertion (at tail) | O(n) / O(1) with tail pointer | O(1) |
| Insertion (at position) | O(n) | O(1) |
| Deletion (at head) | O(1) | O(1) |
| Deletion (at position) | O(n) | O(1) |

---

## 🔍 Visual Representation

```
Singly Linked List:
[10] → [20] → [30] → [40] → None
 ↑                           ↑
head                        tail

Doubly Linked List:
None ← [10] ⇄ [20] ⇄ [30] ⇄ [40] → None
        ↑                    ↑
       head                 tail

Circular Linked List:
       ┌─────────────────┐
       ↓                 │
[10] → [20] → [30] → [40] ┘
 ↑
head
```

---

## 🚀 Top 5 Essential Algorithms

### 1. Reverse Linked List

**Use Cases:** List manipulation, recursive problem solving, stack simulation

**Algorithm Steps:**
1. **Initialize Pointers:** Set prev=null, current=head for iterative approach
2. **Store Next:** Save next node before breaking the link
3. **Reverse Link:** Point current.next to prev (reverse the connection)
4. **Move Forward:** Update prev=current, current=nextTemp
5. **Return New Head:** prev becomes the new head when current is null

**Process Visualization:**
```
Iterative Reversal of [1] → [2] → [3] → [4] → null:

Initial:  prev=null, current=[1] → [2] → [3] → [4] → null

Step 1:   next=[2] → [3] → [4] → null
          prev=null ← [1]   current=[2] → [3] → [4] → null

Step 2:   next=[3] → [4] → null  
          prev=null ← [1] ← [2]   current=[3] → [4] → null

Step 3:   next=[4] → null
          prev=null ← [1] ← [2] ← [3]   current=[4] → null

Step 4:   next=null
          prev=null ← [1] ← [2] ← [3] ← [4]   current=null

Result: [4] → [3] → [2] → [1] → null (prev is new head)

Recursive Approach:
reverse([1,2,3,4]) = reverse([2,3,4]) + attach(1)
                   = [4,3,2] + attach(1)
                   = [4,3,2,1]

Base case: single node or null returns itself
```



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

public class ReverseLinkedList 
{
    /// <summary>
    /// Reverse linked list iteratively using three pointers
    /// Time: O(n), Space: O(1)
    /// </summary>
    /// <param name="head">Head of the linked list</param>
    /// <returns>New head of reversed list</returns>
    public static ListNode ReverseListIterative(ListNode head) 
    {
        ListNode prev = null;      // Previous node (starts as null)
        ListNode current = head;   // Current node being processed
        
        while (current != null) 
        {
            // Step 1: Store next node before we lose the reference
            ListNode nextTemp = current.next;
            
            // Step 2: Reverse the link (point current to previous)
            current.next = prev;
            
            // Step 3: Move pointers forward for next iteration
            prev = current;        // Previous becomes current
            current = nextTemp;    // Current becomes next
        }
        
        return prev;  // prev is now the new head
    }
    
    /// <summary>
    /// Reverse linked list recursively
    /// Time: O(n), Space: O(n) due to recursion stack
    /// </summary>
    /// <param name="head">Head of the linked list</param>
    /// <returns>New head of reversed list</returns>
    public static ListNode ReverseListRecursive(ListNode head) 
    {
        // Base case: empty list or single node
        if (head == null || head.next == null) 
        {
            return head;
        }
        
        // Recursively reverse the rest of the list
        ListNode newHead = ReverseListRecursive(head.next);
        
        // Reverse the current connection
        head.next.next = head;  // Make next node point back to current
        head.next = null;       // Break forward link to avoid cycle
        
        return newHead;         // Return the new head (unchanged through recursion)
    }
    
    /// <summary>
    /// Reverse nodes of linked list in groups of k
    /// Time: O(n), Space: O(1)
    /// </summary>
    /// <param name="head">Head of the linked list</param>
    /// <param name="k">Group size for reversal</param>
    /// <returns>New head after group reversal</returns>
    public static ListNode ReverseKGroup(ListNode head, int k) 
    {
        if (head == null || k == 1) return head;
        
        // Check if we have at least k nodes
        ListNode current = head;
        int count = 0;
        while (current != null && count < k) 
        {
            current = current.next;
            count++;
        }
        
        // If we have k nodes, reverse them
        if (count == k) 
        {
            // Recursively reverse the rest first
            current = ReverseKGroup(current, k);
            
            // Reverse current k-group
            while (count > 0) 
            {
                ListNode nextTemp = head.next;
                head.next = current;
                current = head;
                head = nextTemp;
                count--;
            }
            head = current;  // current is now the new head of this group
        }
        
        return head;
    }
    
    /// <summary>
    /// Reverse linked list between positions left and right (1-indexed)
    /// Time: O(n), Space: O(1)
    /// </summary>
    /// <param name="head">Head of the linked list</param>
    /// <param name="left">Start position (1-indexed)</param>
    /// <param name="right">End position (1-indexed)</param>
    /// <returns>Head of modified list</returns>
    public static ListNode ReverseBetween(ListNode head, int left, int right) 
    {
        if (head == null || left == right) return head;
        
        // Create dummy node to handle edge case where left = 1
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prevLeft = dummy;
        
        // Move to node before left position
        for (int i = 1; i < left; i++) 
        {
            prevLeft = prevLeft.next;
        }
        
        // Start reversing from left position
        ListNode current = prevLeft.next;
        for (int i = 0; i < right - left; i++) 
        {
            ListNode nextNode = current.next;
            current.next = nextNode.next;
            nextNode.next = prevLeft.next;
            prevLeft.next = nextNode;
        }
        
        return dummy.next;
    }
}
            return head;
        }
        
        ListNode newHead = ReverseListRecursive(head.next);
        head.next.next = head;
        head.next = null;
        
        return newHead;
    }
    
    public static ListNode ReverseBetween(ListNode head, int left, int right) 
    {
        if (head == null || left == right) return head;
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        
        for (int i = 0; i < left - 1; i++) 
        {
            prev = prev.next;
        }
        
        ListNode current = prev.next;
        for (int i = 0; i < right - left; i++) 
        {
            ListNode nextTemp = current.next;
            current.next = nextTemp.next;
            nextTemp.next = prev.next;
            prev.next = nextTemp;
        }
        
        return dummy.next;
    }
    
    public static ListNode ReverseKGroup(ListNode head, int k) 
    {
        int GetLength(ListNode node) 
        {
            int length = 0;
            while (node != null) 
            {
                length++;
                node = node.next;
            }
            return length;
        }
        
        (ListNode newStart, ListNode newEnd, ListNode nextStart) ReverseGroup(ListNode start, int k) 
        {
            ListNode prev = null;
            ListNode current = start;
            for (int i = 0; i < k; i++) 
            {
                ListNode nextTemp = current.next;
                current.next = prev;
                prev = current;
                current = nextTemp;
            }
            return (prev, start, current);
        }
        
        int length = GetLength(head);
        if (length < k) return head;
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prevGroupEnd = dummy;
        
        while (length >= k) 
        {
            ListNode groupStart = prevGroupEnd.next;
            var (newGroupStart, newGroupEnd, nextGroupStart) = ReverseGroup(groupStart, k);
            
            prevGroupEnd.next = newGroupStart;
            newGroupEnd.next = nextGroupStart;
            prevGroupEnd = newGroupEnd;
            
            length -= k;
        }
        
        return dummy.next;
    }
}
```

---

### 2. Detect Cycle (Floyd's Algorithm)

**Use Cases:** Cycle detection, finding loop start, duplicate detection



#### C# Implementation
```csharp
using System;

public class CycleDetection 
{
    public static bool HasCycle(ListNode head) 
    {
        if (head == null || head.next == null) return false;
        
        ListNode slow = head;
        ListNode fast = head;
        
        while (fast != null && fast.next != null) 
        {
            slow = slow.next;
            fast = fast.next.next;
            
            if (slow == fast) 
            {
                return true;
            }
        }
        
        return false;
    }
    
    public static ListNode DetectCycleStart(ListNode head) 
    {
        if (head == null || head.next == null) return null;
        
        ListNode slow = head;
        ListNode fast = head;
        
        // Phase 1: Detect cycle
        while (fast != null && fast.next != null) 
        {
            slow = slow.next;
            fast = fast.next.next;
            
            if (slow == fast) break;
        }
        
        if (fast == null || fast.next == null) return null;
        
        // Phase 2: Find cycle start
        ListNode start = head;
        while (start != slow) 
        {
            start = start.next;
            slow = slow.next;
        }
        
        return start;
    }
    
    public static int FindCycleLength(ListNode head) 
    {
        if (head == null || head.next == null) return 0;
        
        ListNode slow = head;
        ListNode fast = head;
        
        // Detect cycle
        while (fast != null && fast.next != null) 
        {
            slow = slow.next;
            fast = fast.next.next;
            
            if (slow == fast) break;
        }
        
        if (fast == null || fast.next == null) return 0;
        
        // Count cycle length
        int length = 1;
        ListNode current = slow.next;
        while (current != slow) 
        {
            length++;
            current = current.next;
        }
        
        return length;
    }
    
    public static int FindDuplicateNumber(int[] nums) 
    {
        int slow = nums[0];
        int fast = nums[0];
        
        // Phase 1: Find intersection
        do 
        {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);
        
        // Phase 2: Find entrance to cycle
        slow = nums[0];
        while (slow != fast) 
        {
            slow = nums[slow];
            fast = nums[fast];
        }
        
        return slow;
    }
    
    public static ListNode RemoveCycle(ListNode head) 
    {
        if (head == null || head.next == null) return head;
        
        ListNode slow = head;
        ListNode fast = head;
        
        // Detect cycle
        while (fast != null && fast.next != null) 
        {
            slow = slow.next;
            fast = fast.next.next;
            
            if (slow == fast) break;
        }
        
        if (fast == null || fast.next == null) return head;
        
        // Find cycle start
        ListNode start = head;
        while (start != slow) 
        {
            start = start.next;
            slow = slow.next;
        }
        
        // Find node just before cycle start
        while (slow.next != start) 
        {
            slow = slow.next;
        }
        
        // Break cycle
        slow.next = null;
        
        return head;
    }
}
```

---

### 3. Merge Sorted Lists

**Use Cases:** Merge sort implementation, combining sorted data, divide and conquer



#### C# Implementation
```csharp
using System;
using System.Collections.Generic;

public class MergeSortedLists 
{
    public static ListNode MergeTwoLists(ListNode l1, ListNode l2) 
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
    
    public static ListNode MergeKLists(ListNode[] lists) 
    {
        if (lists == null || lists.Length == 0) return null;
        
        ListNode MergeRange(int start, int end) 
        {
            if (start == end) return lists[start];
            if (start + 1 == end) return MergeTwoLists(lists[start], lists[end]);
            
            int mid = (start + end) / 2;
            ListNode left = MergeRange(start, mid);
            ListNode right = MergeRange(mid + 1, end);
            
            return MergeTwoLists(left, right);
        }
        
        return MergeRange(0, lists.Length - 1);
    }
    
    public static ListNode MergeKListsHeap(ListNode[] lists) 
    {
        var pq = new PriorityQueue<(int val, int idx, ListNode node), int>();
        
        for (int i = 0; i < lists.Length; i++) 
        {
            if (lists[i] != null) 
            {
                pq.Enqueue((lists[i].val, i, lists[i]), lists[i].val);
            }
        }
        
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        
        while (pq.Count > 0) 
        {
            var (val, idx, node) = pq.Dequeue();
            current.next = node;
            current = current.next;
            
            if (node.next != null) 
            {
                pq.Enqueue((node.next.val, idx, node.next), node.next.val);
            }
        }
        
        return dummy.next;
    }
    
    public static ListNode SortList(ListNode head) 
    {
        if (head == null || head.next == null) return head;
        
        ListNode FindMiddle(ListNode node) 
        {
            ListNode slow = node;
            ListNode fast = node;
            ListNode prev = null;
            
            while (fast != null && fast.next != null) 
            {
                prev = slow;
                slow = slow.next;
                fast = fast.next.next;
            }
            
            prev.next = null;
            return slow;
        }
        
        ListNode middle = FindMiddle(head);
        
        ListNode left = SortList(head);
        ListNode right = SortList(middle);
        
        return MergeTwoLists(left, right);
    }
    
    public static ListNode MergeSortBottomUp(ListNode head) 
    {
        if (head == null || head.next == null) return head;
        
        int CountNodes(ListNode node) 
        {
            int count = 0;
            while (node != null) 
            {
                count++;
                node = node.next;
            }
            return count;
        }
        
        ListNode Split(ListNode head, int size) 
        {
            for (int i = 0; i < size - 1 && head != null; i++) 
            {
                head = head.next;
            }
            
            if (head == null) return null;
            
            ListNode second = head.next;
            head.next = null;
            return second;
        }
        
        int totalNodes = CountNodes(head);
        
        for (int size = 1; size < totalNodes; size *= 2) 
        {
            ListNode dummy = new ListNode(0);
            ListNode current = dummy;
            ListNode remaining = head;
            
            while (remaining != null) 
            {
                ListNode left = remaining;
                ListNode right = Split(left, size);
                remaining = Split(right, size);
                
                ListNode merged = MergeTwoLists(left, right);
                current.next = merged;
                
                while (current.next != null) 
                {
                    current = current.next;
                }
            }
            
            head = dummy.next;
        }
        
        return head;
    }
}
```

---

### 4. Fast & Slow Pointers (Two Pointers)

**Use Cases:** Finding middle, detecting cycles, palindrome checking, nth from end



#### C# Implementation
```csharp
using System;

public class TwoPointers 
{
    public static ListNode FindMiddle(ListNode head) 
    {
        if (head == null) return null;
        
        ListNode slow = head;
        ListNode fast = head;
        
        while (fast != null && fast.next != null) 
        {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        return slow;
    }
    
    public static ListNode FindNthFromEnd(ListNode head, int n) 
    {
        if (head == null || n <= 0) return null;
        
        ListNode first = head;
        ListNode second = head;
        
        for (int i = 0; i < n; i++) 
        {
            if (first == null) return null;
            first = first.next;
        }
        
        while (first != null) 
        {
            first = first.next;
            second = second.next;
        }
        
        return second;
    }
    
    public static ListNode RemoveNthFromEnd(ListNode head, int n) 
    {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        ListNode first = dummy;
        ListNode second = dummy;
        
        for (int i = 0; i <= n; i++) 
        {
            first = first.next;
        }
        
        while (first != null) 
        {
            first = first.next;
            second = second.next;
        }
        
        second.next = second.next.next;
        return dummy.next;
    }
    
    public static bool IsPalindrome(ListNode head) 
    {
        if (head == null || head.next == null) return true;
        
        // Find middle
        ListNode slow = head;
        ListNode fast = head;
        
        while (fast != null && fast.next != null) 
        {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        // Reverse second half
        ListNode ReverseList(ListNode node) 
        {
            ListNode prev = null;
            ListNode current = node;
            
            while (current != null) 
            {
                ListNode nextTemp = current.next;
                current.next = prev;
                prev = current;
                current = nextTemp;
            }
            
            return prev;
        }
        
        ListNode secondHalf = ReverseList(slow);
        
        // Compare both halves
        ListNode firstHalf = head;
        while (secondHalf != null) 
        {
            if (firstHalf.val != secondHalf.val) 
            {
                return false;
            }
            firstHalf = firstHalf.next;
            secondHalf = secondHalf.next;
        }
        
        return true;
    }
    
    public static void ReorderList(ListNode head) 
    {
        if (head == null || head.next == null) return;
        
        // Find middle
        ListNode slow = head;
        ListNode fast = head;
        
        while (fast.next != null && fast.next.next != null) 
        {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        // Split and reverse second half
        ListNode secondHalf = slow.next;
        slow.next = null;
        
        ListNode ReverseList(ListNode node) 
        {
            ListNode prev = null;
            ListNode current = node;
            
            while (current != null) 
            {
                ListNode nextTemp = current.next;
                current.next = prev;
                prev = current;
                current = nextTemp;
            }
            
            return prev;
        }
        
        secondHalf = ReverseList(secondHalf);
        
        // Merge alternately
        ListNode first = head;
        ListNode second = secondHalf;
        
        while (second != null) 
        {
            ListNode nextFirst = first.next;
            ListNode nextSecond = second.next;
            
            first.next = second;
            second.next = nextFirst;
            
            first = nextFirst;
            second = nextSecond;
        }
    }
    
    public static ListNode GetIntersectionNode(ListNode headA, ListNode headB) 
    {
        if (headA == null || headB == null) return null;
        
        ListNode pA = headA;
        ListNode pB = headB;
        
        while (pA != pB) 
        {
            pA = pA?.next ?? headB;
            pB = pB?.next ?? headA;
        }
        
        return pA;
    }
}
```

---

### 5. LRU Cache with Linked List

**Use Cases:** Cache implementation, memory management, operating systems



#### C# Implementation
```csharp
using System;
using System.Collections.Generic;

public class LRUCacheLinkedList 
{
    private class Node 
    {
        public int Key { get; set; }
        public int Value { get; set; }
        public Node Prev { get; set; }
        public Node Next { get; set; }
        
        public Node(int key = 0, int value = 0) 
        {
            Key = key;
            Value = value;
        }
    }
    
    private readonly int capacity;
    private readonly Dictionary<int, Node> cache;
    private readonly Node head;
    private readonly Node tail;
    
    public LRUCacheLinkedList(int capacity) 
    {
        this.capacity = capacity;
        this.cache = new Dictionary<int, Node>();
        
        this.head = new Node();
        this.tail = new Node();
        this.head.Next = this.tail;
        this.tail.Prev = this.head;
    }
    
    private void AddNode(Node node) 
    {
        node.Prev = head;
        node.Next = head.Next;
        head.Next.Prev = node;
        head.Next = node;
    }
    
    private void RemoveNode(Node node) 
    {
        Node prevNode = node.Prev;
        Node nextNode = node.Next;
        prevNode.Next = nextNode;
        nextNode.Prev = prevNode;
    }
    
    private void MoveToHead(Node node) 
    {
        RemoveNode(node);
        AddNode(node);
    }
    
    private Node PopTail() 
    {
        Node lastNode = tail.Prev;
        RemoveNode(lastNode);
        return lastNode;
    }
    
    public int Get(int key) 
    {
        if (cache.TryGetValue(key, out Node node)) 
        {
            MoveToHead(node);
            return node.Value;
        }
        
        return -1;
    }
    
    public void Put(int key, int value) 
    {
        if (cache.TryGetValue(key, out Node node)) 
        {
            node.Value = value;
            MoveToHead(node);
        }
        else 
        {
            Node newNode = new Node(key, value);
            
            if (cache.Count >= capacity) 
            {
                Node tail = PopTail();
                cache.Remove(tail.Key);
            }
            
            cache[key] = newNode;
            AddNode(newNode);
        }
    }
}

public class DoublyLinkedList<T> 
{
    private class Node 
    {
        public T Value { get; set; }
        public Node Prev { get; set; }
        public Node Next { get; set; }
        
        public Node(T value) 
        {
            Value = value;
        }
    }
    
    private readonly Node head;
    private readonly Node tail;
    private int size;
    
    public DoublyLinkedList() 
    {
        head = new Node(default(T));
        tail = new Node(default(T));
        head.Next = tail;
        tail.Prev = head;
        size = 0;
    }
    
    public void AddFirst(T value) 
    {
        Node node = new Node(value);
        node.Next = head.Next;
        node.Prev = head;
        head.Next.Prev = node;
        head.Next = node;
        size++;
    }
    
    public void AddLast(T value) 
    {
        Node node = new Node(value);
        node.Prev = tail.Prev;
        node.Next = tail;
        tail.Prev.Next = node;
        tail.Prev = node;
        size++;
    }
    
    public T RemoveFirst() 
    {
        if (size == 0) throw new InvalidOperationException("List is empty");
        
        Node first = head.Next;
        head.Next = first.Next;
        first.Next.Prev = head;
        size--;
        
        return first.Value;
    }
    
    public T RemoveLast() 
    {
        if (size == 0) throw new InvalidOperationException("List is empty");
        
        Node last = tail.Prev;
        tail.Prev = last.Prev;
        last.Prev.Next = tail;
        size--;
        
        return last.Value;
    }
    
    public T PeekFirst() 
    {
        if (size == 0) throw new InvalidOperationException("List is empty");
        return head.Next.Value;
    }
    
    public T PeekLast() 
    {
        if (size == 0) throw new InvalidOperationException("List is empty");
        return tail.Prev.Value;
    }
    
    public bool IsEmpty => size == 0;
    public int Count => size;
    
    public T[] ToArray() 
    {
        T[] result = new T[size];
        Node current = head.Next;
        int index = 0;
        
        while (current != tail) 
        {
            result[index++] = current.Value;
            current = current.Next;
        }
        
        return result;
    }
}

public class DequeLinkedList<T> 
{
    private readonly DoublyLinkedList<T> dll;
    
    public DequeLinkedList() 
    {
        dll = new DoublyLinkedList<T>();
    }
    
    public void AddFront(T value) => dll.AddFirst(value);
    public void AddRear(T value) => dll.AddLast(value);
    public T RemoveFront() => dll.RemoveFirst();
    public T RemoveRear() => dll.RemoveLast();
    public T Front() => dll.PeekFirst();
    public T Rear() => dll.PeekLast();
    public bool IsEmpty => dll.IsEmpty;
    public int Count => dll.Count;
}
```

---

## 🎯 Common Patterns & Tips

### Pattern Recognition
- **Reverse Operations:** Use iterative or recursive reversal
- **Cycle Detection:** Use Floyd's two-pointer algorithm
- **Merge Operations:** Use dummy nodes and careful pointer manipulation
- **Two Pointers:** Use for finding middle, nth from end, palindrome checking
- **LRU Cache:** Combine hash map with doubly linked list

### Optimization Tips
1. **Use dummy nodes** to simplify edge cases
2. **Draw diagrams** to visualize pointer movements
3. **Handle edge cases:** null lists, single nodes, empty lists
4. **Consider space complexity:** in-place vs additional space
5. **Test with simple cases** before complex scenarios

### Common Pitfalls
- **Null pointer exceptions** - always check for null
- **Memory leaks** in languages with manual memory management
- **Losing references** during pointer manipulation
- **Off-by-one errors** in counting operations
- **Infinite loops** in cycle-related problems

---

## 📚 Related LeetCode Problems

### Easy
- [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

### Medium
- [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
- [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
- [Reorder List](https://leetcode.com/problems/reorder-list/)
- [LRU Cache](https://leetcode.com/problems/lru-cache/)

### Hard
- [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)
- [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)

---

[← Back to Main Guide](./README.md)
