# 📘 Essential Data Structures – Visual Guide with Python & C# Examples

---

## 📌 Arrays & Strings

### 🔹 Description
- Arrays: Fixed-size, indexed collections.
- Strings: Immutable sequences of characters.

### 🔹 Visual
```
Index:     0     1     2     3
Array:   [10]  [20]  [30]  [40]
```

### 🔹 Python
```python
arr = [10, 20, 30, 40]
print(arr[2])  # 30

s = "hello"
print(s[1:4])  # ell
```

### 🔹 C#
```csharp
int[] arr = {10, 20, 30, 40};
Console.WriteLine(arr[2]);  // 30

string s = "hello";
Console.WriteLine(s.Substring(1, 3));  // ell
```

---

## 📌 Hash Maps & Sets

### 🔹 Description
- Hash Map: Stores key-value pairs for O(1) average access.
- Set: Stores unique items.

### 🔹 Visual
```
Keys → Hash → Index → Bucket

Example:
{
  "apple"  → 3,
  "banana" → 7
}
```

### 🔹 Python
```python
hashmap = {"apple": 3, "banana": 7}
print(hashmap["apple"])  # 3

myset = {"a", "b"}
print("a" in myset)  # True
```

### 🔹 C#
```csharp
var hashmap = new Dictionary<string, int> {
    {"apple", 3}, {"banana", 7}
};
Console.WriteLine(hashmap["apple"]);  // 3

var myset = new HashSet<string> { "a", "b" };
Console.WriteLine(myset.Contains("a"));  // True
```

---

## 📌 Linked Lists

### 🔹 Description
- A chain of nodes pointing to the next (and optionally previous) node.

### 🔹 Visual
```
Singly:  [10] → [20] → [30] → None
Doubly:  None ← [10] ⇄ [20] ⇄ [30] → None
```

### 🔹 Python
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
```

### 🔹 C#
```csharp
class Node {
    public int val;
    public Node next;
    public Node(int val) {
        this.val = val;
        this.next = null;
    }
}
```

---

## 📌 Trees

### 🔹 Description
- Hierarchical structures with parent-child relationships.

---

### 🌲 Binary Tree

#### 🔹 Visual
```
       10
      /  \
     5    15
    / \     \
   3   7     20
```

#### 🔹 Python
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

#### 🔹 C#
```csharp
class TreeNode {
    public int val;
    public TreeNode left, right;
    public TreeNode(int val) {
        this.val = val;
    }
}
```

---

### 🌲 Binary Search Tree (BST)

#### 🔹 Property
Left < Node < Right (in-order traversal gives sorted output)

---

### 🌲 AVL Tree
- Height-balanced BST
- Balance factor ∈ {-1, 0, 1}

---

### 🌲 Red-Black Tree
- Self-balancing BST with color constraints
- Used in `TreeMap` (Java), `SortedDictionary` (C#)

---

### 🌲 Tries

#### 🔹 Visual
```
Words: [ "cat", "car" ]
         (root)
           |
           c
           |
           a
         /   \
        t     r
```

#### 🔹 Python
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
```

#### 🔹 C#
```csharp
class TrieNode {
    public Dictionary<char, TrieNode> children = new();
    public bool isEnd = false;
}
```

---

## 📌 Heaps & Priority Queues

### 🔹 Description
- Min-Heap: Parent ≤ Children
- Backed by an array

### 🔹 Visual
```
        1
       / \
      3   5
     / \
    7   9

Array: [1, 3, 5, 7, 9]
```

### 🔹 Python
```python
import heapq
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
print(heapq.heappop(heap))  # 1
```

### 🔹 C#
```csharp
var pq = new PriorityQueue<int, int>();
pq.Enqueue(3, 3);
pq.Enqueue(1, 1);
Console.WriteLine(pq.Dequeue());  // 1
```

---

## 📌 Graphs

### 🔹 Description
- Nodes (vertices) connected by edges
- Directed/Undirected, Weighted/Unweighted

---

### 🔹 Adjacency List

#### 🔹 Visual
```
0 → 1, 2
1 → 2
2 → 0, 3
3 → 3
```

#### 🔹 Python
```python
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}
```

#### 🔹 C#
```csharp
var graph = new Dictionary<int, List<int>> {
    {0, new List<int>{1, 2}},
    {1, new List<int>{2}},
    {2, new List<int>{0, 3}},
    {3, new List<int>{3}},
};
```

---

### 🔹 Adjacency Matrix

#### 🔹 Visual
```
     0  1  2  3
  ---------------
0 | 0  1  1  0
1 | 0  0  1  0
2 | 1  0  0  1
3 | 0  0  0  1
```

#### 🔹 Python
```python
matrix = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1]
]
```

#### 🔹 C#
```csharp
int[,] matrix = {
    {0, 1, 1, 0},
    {0, 0, 1, 0},
    {1, 0, 0, 1},
    {0, 0, 0, 1}
};
```

---

**✅ Tip:** Focus on operations, time complexity, and real-world usage scenarios for each data structure.
