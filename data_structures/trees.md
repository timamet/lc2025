# 🌳 Trees

## 📋 Overview

**Trees** are hierarchical data structures consisting of nodes connected by edges, with a single root node and each node having zero or more child nodes. Trees are fundamental structures used in many algorithms and applications.

---

## 🎯 Key Properties

- **Hierarchical Structure:** Parent-child relationships with one root
- **No Cycles:** Trees are acyclic connected graphs
- **Unique Path:** Exactly one path between any two nodes
- **Recursive Structure:** Each subtree is also a tree
- **Various Types:** Binary trees, BSTs, AVL trees, Tries, etc.

---

## 📊 Time & Space Complexity

| Operation | Balanced Tree | Unbalanced Tree | Space |
|-----------|---------------|-----------------|-------|
| Search | O(log n) | O(n) | O(h) |
| Insert | O(log n) | O(n) | O(h) |
| Delete | O(log n) | O(n) | O(h) |
| Traversal | O(n) | O(n) | O(h) |

*h = height of tree*

---

## 🔍 Visual Representation

```
Binary Tree:
       10
      /  \
     5    15
    / \     \
   3   7     20

Binary Search Tree:
       8
      / \
     3   10
    / \    \
   1   6    14
      / \   /
     4   7 13

Trie (Prefix Tree):
Words: ["cat", "car", "card"]
         root
          |
          c
          |
          a
         / \
        t   r
            |
            d
```

---

## 🚀 Top 5 Essential Algorithms

### 1. Tree Traversals (DFS & BFS)

**Use Cases:** Tree processing, serialization, searching, validation

**Algorithm Steps:**
1. **Choose Strategy:** DFS (recursive/stack) or BFS (queue) based on requirements
2. **DFS Variants:** Inorder (left-root-right), Preorder (root-left-right), Postorder (left-right-root)
3. **Process Node:** Visit/process current node according to traversal order
4. **Recurse/Iterate:** Apply same strategy to child nodes
5. **Collect Results:** Gather processed values in desired order

**Process Visualization:**
```
Tree Example:        1
                   /   \
                  2     3
                 / \
                4   5

Inorder (Left-Root-Right): 4 → 2 → 5 → 1 → 3
Process: Visit left subtree completely, then root, then right subtree

Preorder (Root-Left-Right): 1 → 2 → 4 → 5 → 3  
Process: Visit root first, then left subtree, then right subtree

Postorder (Left-Right-Root): 4 → 5 → 2 → 3 → 1
Process: Visit children completely before processing parent

Level Order (BFS): 1 → 2 → 3 → 4 → 5
Process: Visit all nodes at depth 0, then depth 1, then depth 2, etc.

DFS vs BFS Memory Usage:
- DFS: O(h) where h is height (recursion stack)
- BFS: O(w) where w is maximum width at any level
```

#### C# Implementation
```csharp
using System;
using System.Collections.Generic;

public class TreeNode 
{
    public int val;
    public TreeNode left;
    public TreeNode right;
    
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) 
    {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class TreeTraversal 
{
    /// <summary>
    /// Inorder traversal: Left → Root → Right (gives sorted order for BST)
    /// Time: O(n), Space: O(h) where h is tree height
    /// </summary>
    /// <param name="root">Root of the tree</param>
    /// <returns>List of values in inorder sequence</returns>
    public static List<int> InorderTraversal(TreeNode root) 
    {
        var result = new List<int>();
        InorderHelper(root, result);
        return result;
    }
    
    private static void InorderHelper(TreeNode node, List<int> result) 
    {
        if (node == null) return;  // Base case: null node
        
        InorderHelper(node.left, result);   // Process left subtree first
        result.Add(node.val);               // Process current node
        InorderHelper(node.right, result);  // Process right subtree last
    }
    
    /// <summary>
    /// Preorder traversal: Root → Left → Right (useful for tree serialization)
    /// Time: O(n), Space: O(h)
    /// </summary>
    /// <param name="root">Root of the tree</param>
    /// <returns>List of values in preorder sequence</returns>
    public static List<int> PreorderTraversal(TreeNode root) 
    {
        var result = new List<int>();
        if (root == null) return result;
        
        var stack = new Stack<TreeNode>();
        stack.Push(root);
        
        while (stack.Count > 0) 
        {
            TreeNode current = stack.Pop();
            result.Add(current.val);        // Process root first
            
            // Push right first so left is processed first (stack is LIFO)
            if (current.right != null) stack.Push(current.right);
            if (current.left != null) stack.Push(current.left);
        }
        
        return result;
    }
    
    /// <summary>
    /// Postorder traversal: Left → Right → Root (useful for tree deletion)
    /// Time: O(n), Space: O(h)
    /// </summary>
    /// <param name="root">Root of the tree</param>
    /// <returns>List of values in postorder sequence</returns>
    public static List<int> PostorderTraversal(TreeNode root) 
    {
        var result = new List<int>();
        PostorderHelper(root, result);
        return result;
    }
    
    private static void PostorderHelper(TreeNode node, List<int> result) 
    {
        if (node == null) return;
        
        PostorderHelper(node.left, result);   // Process left subtree
        PostorderHelper(node.right, result);  // Process right subtree  
        result.Add(node.val);                 // Process root last
    }
    
    /// <summary>
    /// Level order traversal (BFS): Process nodes level by level
    /// Time: O(n), Space: O(w) where w is maximum width
    /// </summary>
    /// <param name="root">Root of the tree</param>
    /// <returns>List of lists, each containing values at one level</returns>
    public static IList<IList<int>> LevelOrder(TreeNode root) 
    {
        var result = new List<IList<int>>();
        if (root == null) return result;
        
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        
        while (queue.Count > 0) 
        {
            int levelSize = queue.Count;        // Number of nodes at current level
            var currentLevel = new List<int>();
            
            // Process all nodes at current level
            for (int i = 0; i < levelSize; i++) 
            {
                TreeNode current = queue.Dequeue();
                currentLevel.Add(current.val);
                
                // Add children for next level processing
                if (current.left != null) queue.Enqueue(current.left);
                if (current.right != null) queue.Enqueue(current.right);
            }
            
            result.Add(currentLevel);
        }
        
        return result;
    }
    
    /// <summary>
    /// Zigzag level order traversal: Alternate left-to-right and right-to-left
    /// Time: O(n), Space: O(w)
    /// </summary>
    /// <param name="root">Root of the tree</param>
    /// <returns>List of lists with alternating direction per level</returns>
    public static IList<IList<int>> ZigzagLevelOrder(TreeNode root) 
    {
        var result = new List<IList<int>>();
        if (root == null) return result;
        
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        bool leftToRight = true;  // Direction flag
        
        while (queue.Count > 0) 
        {
            int levelSize = queue.Count;
            var currentLevel = new List<int>();
            
            for (int i = 0; i < levelSize; i++) 
            {
                TreeNode current = queue.Dequeue();
                
                // Add to front or back based on direction
                if (leftToRight) 
                {
                    currentLevel.Add(current.val);
                }
                else 
                {
                    currentLevel.Insert(0, current.val);  // Insert at beginning
                }
                
                if (current.left != null) queue.Enqueue(current.left);
                if (current.right != null) queue.Enqueue(current.right);
            }
            
            result.Add(currentLevel);
            leftToRight = !leftToRight;  // Flip direction for next level
        }
        
        return result;
    }
    
    /// <summary>
    /// Vertical order traversal: Group nodes by vertical position
    /// Time: O(n log n), Space: O(n)
    /// </summary>
    /// <param name="root">Root of the tree</param>
    /// <returns>List of lists grouped by vertical position</returns>
    public static IList<IList<int>> VerticalOrder(TreeNode root) 
    {
        var result = new List<IList<int>>();
        if (root == null) return result;
        
        // Map: column → list of (row, value) pairs
        var columnMap = new Dictionary<int, List<(int row, int val)>>();
        var queue = new Queue<(TreeNode node, int row, int col)>();
        
        queue.Enqueue((root, 0, 0));
        int minCol = 0, maxCol = 0;
        
        while (queue.Count > 0) 
        {
            var (node, row, col) = queue.Dequeue();
            
            if (!columnMap.ContainsKey(col)) 
            {
                columnMap[col] = new List<(int, int)>();
            }
            columnMap[col].Add((row, node.val));
            
            minCol = Math.Min(minCol, col);
            maxCol = Math.Max(maxCol, col);
            
            if (node.left != null) queue.Enqueue((node.left, row + 1, col - 1));
            if (node.right != null) queue.Enqueue((node.right, row + 1, col + 1));
        }
        
        // Build result in column order
        for (int col = minCol; col <= maxCol; col++) 
        {
            var values = columnMap[col];
            values.Sort((a, b) => a.row.CompareTo(b.row));  // Sort by row within column
            result.Add(values.Select(x => x.val).ToList());
        }
        
        return result;
    }
}
    
    private static void InorderHelper(TreeNode node, List<int> result) 
    {
        if (node == null) return;
        
        InorderHelper(node.left, result);   // Left
        result.Add(node.val);               // Root
        InorderHelper(node.right, result);  // Right
    }
    
    public static List<int> InorderIterative(TreeNode root) 
    {
        var result = new List<int>();
        var stack = new Stack<TreeNode>();
        TreeNode current = root;
        
        while (current != null || stack.Count > 0) 
        {
            while (current != null) 
            {
                stack.Push(current);
                current = current.left;
            }
            
            current = stack.Pop();
            result.Add(current.val);
            current = current.right;
        }
        
        return result;
    }
    
    public static List<int> PreorderTraversal(TreeNode root) 
    {
        var result = new List<int>();
        PreorderHelper(root, result);
        return result;
    }
    
    private static void PreorderHelper(TreeNode node, List<int> result) 
    {
        if (node == null) return;
        
        result.Add(node.val);               // Root
        PreorderHelper(node.left, result);  // Left
        PreorderHelper(node.right, result); // Right
    }
    
    public static List<int> PreorderIterative(TreeNode root) 
    {
        if (root == null) return new List<int>();
        
        var result = new List<int>();
        var stack = new Stack<TreeNode>();
        stack.Push(root);
        
        while (stack.Count > 0) 
        {
            TreeNode node = stack.Pop();
            result.Add(node.val);
            
            if (node.right != null) stack.Push(node.right);
            if (node.left != null) stack.Push(node.left);
        }
        
        return result;
    }
    
    public static List<int> PostorderTraversal(TreeNode root) 
    {
        var result = new List<int>();
        PostorderHelper(root, result);
        return result;
    }
    
    private static void PostorderHelper(TreeNode node, List<int> result) 
    {
        if (node == null) return;
        
        PostorderHelper(node.left, result);  // Left
        PostorderHelper(node.right, result); // Right
        result.Add(node.val);                // Root
    }
    
    public static List<int> PostorderIterative(TreeNode root) 
    {
        if (root == null) return new List<int>();
        
        var result = new List<int>();
        var stack = new Stack<TreeNode>();
        TreeNode lastVisited = null;
        TreeNode current = root;
        
        while (stack.Count > 0 || current != null) 
        {
            if (current != null) 
            {
                stack.Push(current);
                current = current.left;
            }
            else 
            {
                TreeNode peekNode = stack.Peek();
                if (peekNode.right != null && lastVisited != peekNode.right) 
                {
                    current = peekNode.right;
                }
                else 
                {
                    result.Add(peekNode.val);
                    lastVisited = stack.Pop();
                }
            }
        }
        
        return result;
    }
    
    // Breadth-First Search (Level Order)
    public static List<List<int>> LevelOrder(TreeNode root) 
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
    
    public static List<List<int>> ZigzagLevelOrder(TreeNode root) 
    {
        var result = new List<List<int>>();
        if (root == null) return result;
        
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        bool leftToRight = true;
        
        while (queue.Count > 0) 
        {
            int levelSize = queue.Count;
            var currentLevel = new List<int>();
            
            for (int i = 0; i < levelSize; i++) 
            {
                TreeNode node = queue.Dequeue();
                
                if (leftToRight) 
                {
                    currentLevel.Add(node.val);
                }
                else 
                {
                    currentLevel.Insert(0, node.val);
                }
                
                if (node.left != null) queue.Enqueue(node.left);
                if (node.right != null) queue.Enqueue(node.right);
            }
            
            result.Add(currentLevel);
            leftToRight = !leftToRight;
        }
        
        return result;
    }
}
```

---

### 2. Binary Search Tree Operations

#### Algorithm Steps:
1. **Property Validation**: Ensure left subtree < root < right subtree
2. **Search Strategy**: Compare target with current node, go left/right accordingly
3. **Insertion Logic**: Find correct position maintaining BST property
4. **Deletion Handling**: Consider three cases - leaf, one child, two children
5. **Balance Consideration**: Monitor tree height to prevent degeneration

#### Process Visualization:
```
BST Operations Example (target = 6):

Initial BST:           Search Process:        Insert Process:
     8                   8 (6 < 8, go left)     8
   /   \                ↙                     /   \
  3     10             3 (6 > 3, go right)   3     10
 / \      \           ↘                    / \      \
1   6      14        6 (found!)           1   6      14
   / \                                       / \
  4   7                                     4   7
                                               \
Insert 5:                                      5 (new node)
Compare 5 with 8 → go left
Compare 5 with 3 → go right  
Compare 5 with 6 → go left
Compare 5 with 4 → go right
Insert 5 as right child of 4

Delete 3 (two children):
1. Find inorder successor (4)
2. Replace 3's value with 4
3. Delete original 4 node
```

**Use Cases:** Searching, insertion, deletion, range queries

#### C# Implementation
```csharp
using System;
using System.Collections.Generic;

/// <summary>
/// Binary Search Tree implementation with core operations
/// All operations maintain BST property: left < root < right
/// </summary>
public class BinarySearchTree 
{
    public TreeNode root;
    
    public BinarySearchTree() 
    {
        root = null;
    }
    
    /// <summary>
    /// Insert a new value maintaining BST property
    /// Time: O(h) average, O(n) worst case, Space: O(h) recursive
    /// </summary>
    /// <param name="val">Value to insert</param>
    public void Insert(int val) 
    {
        root = InsertHelper(root, val);
    }
    
    private TreeNode InsertHelper(TreeNode node, int val) 
    {
        // Base case: found insertion position
        if (node == null) 
        {
            return new TreeNode(val);
        }
        
        if (val < node.val) 
        {
            node.left = InsertHelper(node.left, val);   // Insert in left subtree
        }
        else if (val > node.val) 
        {
            node.right = InsertHelper(node.right, val); // Insert in right subtree
        }
        // If val == node.val, don't insert duplicates
        
        return node;
    }
    
    /// <summary>
    /// Search for a value in BST using binary search property
    /// Time: O(h) average, O(n) worst case, Space: O(h) recursive
    /// </summary>
    /// <param name="val">Value to search for</param>
    /// <returns>True if value exists, false otherwise</returns>
    public bool Search(int val) 
    {
        return SearchHelper(root, val);
    }
    
    private bool SearchHelper(TreeNode node, int val) 
    {
        if (node == null) return false;  // Value not found
        
        if (val == node.val) return true;        // Found the value
        else if (val < node.val) return SearchHelper(node.left, val);   // Search left
        else return SearchHelper(node.right, val);                      // Search right
    }
    
    /// <summary>
    /// Iterative search implementation (more memory efficient)
    /// Time: O(h) average, O(n) worst case, Space: O(1)
    /// </summary>
    /// <param name="val">Value to search for</param>
    /// <returns>True if value exists, false otherwise</returns>
    public bool SearchIterative(int val) 
    {
        TreeNode current = root;
        
        while (current != null) 
        {
            if (val == current.val) 
            {
                return true;  // Found the value
            }
            else if (val < current.val) 
            {
                current = current.left;   // Go left for smaller values
            }
            else 
            {
                current = current.right;  // Go right for larger values
            }
        }
        
        return false;  // Value not found
    }
    
    /// <summary>
    /// Delete a value from BST maintaining BST property
    /// Time: O(h) average, O(n) worst case, Space: O(h) recursive
    /// </summary>
    /// <param name="val">Value to delete</param>
    public void Delete(int val) 
    {
        root = DeleteHelper(root, val);
    }
    
    private TreeNode DeleteHelper(TreeNode node, int val) 
    {
        if (node == null) return node;  // Value not found
        
        if (val < node.val) 
        {
            node.left = DeleteHelper(node.left, val);
        }
        else if (val > node.val) 
        {
            node.right = DeleteHelper(node.right, val);
        }
        else 
        {
            // Found node to delete - handle three cases
            
            // Case 1: Leaf node (no children)
            if (node.left == null) return node.right;  // Replace with right child (or null)
            if (node.right == null) return node.left;  // Replace with left child
            
            // Case 3: Two children
            // Find inorder successor (smallest value in right subtree)
            TreeNode minNode = FindMin(node.right);
            node.val = minNode.val;  // Replace value with successor
            
            // Delete the successor (which has at most one child)
            node.right = DeleteHelper(node.right, minNode.val);
        }
        
        return node;
    }
    
    /// <summary>
    /// Find minimum value in subtree (leftmost node)
    /// Time: O(h), Space: O(1)
    /// </summary>
    /// <param name="node">Root of subtree</param>
    /// <returns>Node with minimum value</returns>
    private TreeNode FindMin(TreeNode node) 
    {
        while (node.left != null) 
        {
            node = node.left;  // Keep going left
        }
        return node;
    }
    
    /// <summary>
    /// Find maximum value in subtree (rightmost node)
    /// Time: O(h), Space: O(1)
    /// </summary>
    /// <param name="node">Root of subtree</param>
    /// <returns>Node with maximum value</returns>
    private TreeNode FindMax(TreeNode node) 
    {
        while (node.right != null) 
        {
            node = node.right;  // Keep going right
        }
        return node;
    }
    
    /// <summary>
    /// Find kth smallest element in BST using inorder traversal
    /// Time: O(h + k), Space: O(h)
    /// </summary>
    /// <param name="k">Position (1-indexed)</param>
    /// <returns>Value of kth smallest element</returns>
    public int FindKthSmallest(int k) 
    {
        int count = 0;
        return FindKthSmallestHelper(root, k, ref count);
    }
    
    private int FindKthSmallestHelper(TreeNode node, int k, ref int count) 
    {
        if (node == null) return -1;  // Not found
        
        // Inorder traversal: left → root → right (gives sorted order)
        int result = FindKthSmallestHelper(node.left, k, ref count);
        if (result != -1) return result;  // Found in left subtree
        
        count++;
        if (count == k) return node.val;  // This is the kth smallest
        
        return FindKthSmallestHelper(node.right, k, ref count);  // Search right subtree
    }
    
    /// <summary>
    /// Range query: find all values in range [low, high]
    /// Time: O(h + m) where m is number of nodes in range, Space: O(h + m)
    /// </summary>
    /// <param name="low">Lower bound (inclusive)</param>
    /// <param name="high">Upper bound (inclusive)</param>
    /// <returns>List of values in range</returns>
    public List<int> RangeQuery(int low, int high) 
    {
        var result = new List<int>();
        RangeQueryHelper(root, low, high, result);
        return result;
    }
    
    private void RangeQueryHelper(TreeNode node, int low, int high, List<int> result) 
    {
        if (node == null) return;
        
        // If current node is in range, add it
        if (node.val >= low && node.val <= high) 
        {
            result.Add(node.val);
        }
        
        // Optimize: only search left if node value > low
        if (node.val > low) 
        {
            RangeQueryHelper(node.left, low, high, result);
        }
        
        // Optimize: only search right if node value < high
        if (node.val < high) 
        {
            RangeQueryHelper(node.right, low, high, result);
        }
    }
    
    /// <summary>
    /// Validate if tree maintains BST property
    /// Time: O(n), Space: O(h)
    /// </summary>
    /// <returns>True if valid BST, false otherwise</returns>
    public bool IsValidBST() 
    {
        return IsValidBSTHelper(root, long.MinValue, long.MaxValue);
    }
    
    private bool IsValidBSTHelper(TreeNode node, long min, long max) 
    {
        if (node == null) return true;  // Empty tree is valid BST
        
        // Check if current node violates BST property
        if (node.val <= min || node.val >= max) 
        {
            return false;
        }
        
        // Recursively validate left and right subtrees with updated bounds
        return IsValidBSTHelper(node.left, min, node.val) &&
               IsValidBSTHelper(node.right, node.val, max);
    }
    
    /// <summary>
    /// Convert BST to sorted array using inorder traversal
    /// Time: O(n), Space: O(n)
    /// </summary>
    /// <returns>Sorted array of all values</returns>
    public List<int> ToSortedArray() 
    {
        var result = new List<int>();
        InorderTraversal(root, result);
        return result;
    }
    
    private void InorderTraversal(TreeNode node, List<int> result) 
    {
        if (node == null) return;
        
        InorderTraversal(node.left, result);   // Left subtree
        result.Add(node.val);                  // Current node
        InorderTraversal(node.right, result);  // Right subtree
    }
}
    
    public bool IsValidBST() 
    {
        return IsValidBSTHelper(root, long.MinValue, long.MaxValue);
    }
    
    private bool IsValidBSTHelper(TreeNode node, long minVal, long maxVal) 
    {
        if (node == null) return true;
        
        if (node.val <= minVal || node.val >= maxVal) return false;
        
        return IsValidBSTHelper(node.left, minVal, node.val) &&
               IsValidBSTHelper(node.right, node.val, maxVal);
    }
}
```

---

### 3. Tree Validation & Properties

#### Algorithm Steps:
1. **Boundary Setting**: Establish valid range for each node based on ancestors
2. **Recursive Validation**: Check each node against its valid range
3. **Structure Analysis**: Verify balance properties and structural integrity
4. **Property Verification**: Confirm specific tree properties (BST, balanced, etc.)
5. **Edge Case Handling**: Handle null nodes and single-node trees appropriately

#### Process Visualization:
```
BST Validation Example:

Valid BST:              Invalid BST:           Boundary Tracking:
     8                      8                   8 [MIN, MAX]
   /   \                  /   \               /               \
  3     10              3     10        3 [MIN, 8]         10 [8, MAX]
 / \      \            / \      \       /         \             \
1   6      14         1   6      14   1 [MIN, 3]  6 [3, 8]      14 [10, MAX]
   / \                   / \                      / \
  4   7                 4   9 ← INVALID!       4 [3, 6] 7 [6, 8]
                           (9 > 8, violates BST)

Balance Check Example:
     1                 Height calculation:
   /   \               Node 1: max(3, 1) + 1 = 4
  2     3              Node 2: max(2, 0) + 1 = 3  
 /                     Node 4: max(0, 0) + 1 = 1
4                      Node 5: max(0, 0) + 1 = 1
  \                    |3 - 1| = 2 > 1, NOT balanced
   5

Tree Comparison:
Tree 1:    Tree 2:      Same structure & values?
  1          1          ✓ Both roots are 1
 / \        / \         ✓ Left subtrees match
2   3      2   3        ✓ Right subtrees match
                        → Trees are identical
```

**Use Cases:** Verifying tree properties, structure validation, interviews

#### C# Implementation
```csharp
using System;
using System.Collections.Generic;

public class TreeValidation 
{
    public static bool IsValidBST(TreeNode root) 
    {
        return IsValidBSTHelper(root, long.MinValue, long.MaxValue);
    }
    
    private static bool IsValidBSTHelper(TreeNode node, long minVal, long maxVal) 
    {
        if (node == null) return true;
        
        if (node.val <= minVal || node.val >= maxVal) return false;
        
        return IsValidBSTHelper(node.left, minVal, node.val) &&
               IsValidBSTHelper(node.right, node.val, maxVal);
    }
    
    public static bool IsBalanced(TreeNode root) 
    {
        return CheckHeight(root) != -1;
    }
    
    private static int CheckHeight(TreeNode node) 
    {
        if (node == null) return 0;
        
        int leftHeight = CheckHeight(node.left);
        if (leftHeight == -1) return -1;
        
        int rightHeight = CheckHeight(node.right);
        if (rightHeight == -1) return -1;
        
        if (Math.Abs(leftHeight - rightHeight) > 1) return -1;
        
        return Math.Max(leftHeight, rightHeight) + 1;
    }
    
    public static bool IsSameTree(TreeNode p, TreeNode q) 
    {
        if (p == null && q == null) return true;
        if (p == null || q == null) return false;
        
        return p.val == q.val &&
               IsSameTree(p.left, q.left) &&
               IsSameTree(p.right, q.right);
    }
    
    public static bool IsSymmetric(TreeNode root) 
    {
        if (root == null) return true;
        return IsSymmetricHelper(root.left, root.right);
    }
    
    private static bool IsSymmetricHelper(TreeNode left, TreeNode right) 
    {
        if (left == null && right == null) return true;
        if (left == null || right == null) return false;
        
        return left.val == right.val &&
               IsSymmetricHelper(left.left, right.right) &&
               IsSymmetricHelper(left.right, right.left);
    }
    
    public static bool IsSubtree(TreeNode root, TreeNode subRoot) 
    {
        if (root == null) return false;
        
        return IsSameTree(root, subRoot) ||
               IsSubtree(root.left, subRoot) ||
               IsSubtree(root.right, subRoot);
    }
    
    public static int MaxDepth(TreeNode root) 
    {
        if (root == null) return 0;
        
        return Math.Max(MaxDepth(root.left), MaxDepth(root.right)) + 1;
    }
    
    public static int MinDepth(TreeNode root) 
    {
        if (root == null) return 0;
        
        if (root.left == null && root.right == null) return 1;
        
        if (root.left == null) return MinDepth(root.right) + 1;
        if (root.right == null) return MinDepth(root.left) + 1;
        
        return Math.Min(MinDepth(root.left), MinDepth(root.right)) + 1;
    }
    
    public static bool HasPathSum(TreeNode root, int targetSum) 
    {
        if (root == null) return false;
        
        if (root.left == null && root.right == null) 
        {
            return root.val == targetSum;
        }
        
        int remainingSum = targetSum - root.val;
        return HasPathSum(root.left, remainingSum) ||
               HasPathSum(root.right, remainingSum);
    }
    
    public static List<List<int>> PathSum(TreeNode root, int targetSum) 
    {
        var result = new List<List<int>>();
        var currentPath = new List<int>();
        PathSumHelper(root, targetSum, currentPath, result);
        return result;
    }
    
    private static void PathSumHelper(TreeNode node, int targetSum, 
                                     List<int> currentPath, List<List<int>> result) 
    {
        if (node == null) return;
        
        currentPath.Add(node.val);
        
        if (node.left == null && node.right == null && node.val == targetSum) 
        {
            result.Add(new List<int>(currentPath));
        }
        else 
        {
            PathSumHelper(node.left, targetSum - node.val, currentPath, result);
            PathSumHelper(node.right, targetSum - node.val, currentPath, result);
        }
        
        currentPath.RemoveAt(currentPath.Count - 1);
    }
    
    public static int DiameterOfBinaryTree(TreeNode root) 
    {
        int diameter = 0;
        CalculateHeight(root, ref diameter);
        return diameter;
    }
    
    private static int CalculateHeight(TreeNode node, ref int diameter) 
    {
        if (node == null) return 0;
        
        int leftHeight = CalculateHeight(node.left, ref diameter);
        int rightHeight = CalculateHeight(node.right, ref diameter);
        
        diameter = Math.Max(diameter, leftHeight + rightHeight);
        
        return Math.Max(leftHeight, rightHeight) + 1;
    }
}
```

---

### 4. Lowest Common Ancestor (LCA)

**Use Cases:** Finding common ancestors, tree queries, genealogy

#### C# Implementation
```csharp
using System;
using System.Collections.Generic;

public class LowestCommonAncestor 
{
    // LCA in Binary Search Tree
    public static TreeNode LowestCommonAncestorBST(TreeNode root, TreeNode p, TreeNode q) 
    {
        if (root == null) return null;
        
        if (p.val < root.val && q.val < root.val) 
        {
            return LowestCommonAncestorBST(root.left, p, q);
        }
        else if (p.val > root.val && q.val > root.val) 
        {
            return LowestCommonAncestorBST(root.right, p, q);
        }
        else 
        {
            return root;
        }
    }
    
    public static TreeNode LowestCommonAncestorBSTIterative(TreeNode root, TreeNode p, TreeNode q) 
    {
        while (root != null) 
        {
            if (p.val < root.val && q.val < root.val) 
            {
                root = root.left;
            }
            else if (p.val > root.val && q.val > root.val) 
            {
                root = root.right;
            }
            else 
            {
                return root;
            }
        }
        
        return null;
    }
    
    // LCA in Binary Tree
    public static TreeNode LowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) 
    {
        if (root == null || root == p || root == q) 
        {
            return root;
        }
        
        TreeNode left = LowestCommonAncestor(root.left, p, q);
        TreeNode right = LowestCommonAncestor(root.right, p, q);
        
        if (left != null && right != null) return root;
        return left ?? right;
    }
    
    // LCA with Parent Pointers
    public class TreeNodeWithParent 
    {
        public int val;
        public TreeNodeWithParent left;
        public TreeNodeWithParent right;
        public TreeNodeWithParent parent;
        
        public TreeNodeWithParent(int val) 
        {
            this.val = val;
        }
    }
    
    public static TreeNodeWithParent LowestCommonAncestorWithParent(TreeNodeWithParent p, TreeNodeWithParent q) 
    {
        var ancestors = new HashSet<TreeNodeWithParent>();
        
        // Collect all ancestors of p
        TreeNodeWithParent current = p;
        while (current != null) 
        {
            ancestors.Add(current);
            current = current.parent;
        }
        
        // Find first common ancestor of q
        current = q;
        while (current != null) 
        {
            if (ancestors.Contains(current)) 
            {
                return current;
            }
            current = current.parent;
        }
        
        return null;
    }
    
    // LCA of Multiple Nodes
    public static TreeNode LowestCommonAncestorMultiple(TreeNode root, TreeNode[] nodes) 
    {
        var nodeSet = new HashSet<TreeNode>(nodes);
        return LCAMultipleHelper(root, nodeSet);
    }
    
    private static TreeNode LCAMultipleHelper(TreeNode root, HashSet<TreeNode> nodes) 
    {
        if (root == null || nodes.Contains(root)) 
        {
            return root;
        }
        
        TreeNode left = LCAMultipleHelper(root.left, nodes);
        TreeNode right = LCAMultipleHelper(root.right, nodes);
        
        if (left != null && right != null) return root;
        return left ?? right;
    }
    
    // LCA with Path Storage
    public static TreeNode LowestCommonAncestorWithPath(TreeNode root, TreeNode p, TreeNode q) 
    {
        var pathP = new List<TreeNode>();
        var pathQ = new List<TreeNode>();
        
        if (!FindPath(root, p, pathP) || !FindPath(root, q, pathQ)) 
        {
            return null;
        }
        
        TreeNode lca = null;
        int minLength = Math.Min(pathP.Count, pathQ.Count);
        
        for (int i = 0; i < minLength; i++) 
        {
            if (pathP[i] == pathQ[i]) 
            {
                lca = pathP[i];
            }
            else 
            {
                break;
            }
        }
        
        return lca;
    }
    
    private static bool FindPath(TreeNode root, TreeNode target, List<TreeNode> path) 
    {
        if (root == null) return false;
        
        path.Add(root);
        
        if (root == target) return true;
        
        if (FindPath(root.left, target, path) || FindPath(root.right, target, path)) 
        {
            return true;
        }
        
        path.RemoveAt(path.Count - 1);
        return false;
    }
    
    // Distance Between Two Nodes
    public static int DistanceBetweenNodes(TreeNode root, TreeNode p, TreeNode q) 
    {
        TreeNode lca = LowestCommonAncestor(root, p, q);
        
        int distanceP = DistanceFromNode(lca, p);
        int distanceQ = DistanceFromNode(lca, q);
        
        return distanceP + distanceQ;
    }
    
    private static int DistanceFromNode(TreeNode root, TreeNode target) 
    {
        if (root == null) return -1;
        if (root == target) return 0;
        
        int leftDistance = DistanceFromNode(root.left, target);
        if (leftDistance != -1) return leftDistance + 1;
        
        int rightDistance = DistanceFromNode(root.right, target);
        if (rightDistance != -1) return rightDistance + 1;
        
        return -1;
    }
}
```

---

### 5. Tree Serialization & Deserialization

**Use Cases:** Saving/loading trees, network transmission, persistence

#### C# Implementation
```csharp
using System;
using System.Collections.Generic;
using System.Text;

public class TreeSerialization 
{
    // Preorder Serialization
    public static string SerializePreorder(TreeNode root) 
    {
        var sb = new StringBuilder();
        SerializePreorderHelper(root, sb);
        return sb.ToString();
    }
    
    private static void SerializePreorderHelper(TreeNode node, StringBuilder sb) 
    {
        if (node == null) 
        {
            sb.Append("null,");
            return;
        }
        
        sb.Append(node.val).Append(",");
        SerializePreorderHelper(node.left, sb);
        SerializePreorderHelper(node.right, sb);
    }
    
    public static TreeNode DeserializePreorder(string data) 
    {
        var values = new Queue<string>(data.Split(','));
        return DeserializePreorderHelper(values);
    }
    
    private static TreeNode DeserializePreorderHelper(Queue<string> values) 
    {
        if (values.Count == 0) return null;
        
        string val = values.Dequeue();
        if (val == "null") return null;
        
        TreeNode node = new TreeNode(int.Parse(val));
        node.left = DeserializePreorderHelper(values);
        node.right = DeserializePreorderHelper(values);
        
        return node;
    }
    
    // Level Order Serialization
    public static string SerializeLevelOrder(TreeNode root) 
    {
        if (root == null) return "[]";
        
        var result = new List<string>();
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        
        while (queue.Count > 0) 
        {
            TreeNode node = queue.Dequeue();
            
            if (node == null) 
            {
                result.Add("null");
            }
            else 
            {
                result.Add(node.val.ToString());
                queue.Enqueue(node.left);
                queue.Enqueue(node.right);
            }
        }
        
        // Remove trailing nulls
        while (result.Count > 0 && result[result.Count - 1] == "null") 
        {
            result.RemoveAt(result.Count - 1);
        }
        
        return "[" + string.Join(",", result) + "]";
    }
    
    public static TreeNode DeserializeLevelOrder(string data) 
    {
        if (data == "[]") return null;
        
        // Remove brackets and split
        string[] values = data.Substring(1, data.Length - 2).Split(',');
        if (values.Length == 0 || values[0] == "") return null;
        
        TreeNode root = new TreeNode(int.Parse(values[0]));
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        
        int i = 1;
        while (queue.Count > 0 && i < values.Length) 
        {
            TreeNode node = queue.Dequeue();
            
            // Left child
            if (i < values.Length && values[i] != "null") 
            {
                node.left = new TreeNode(int.Parse(values[i]));
                queue.Enqueue(node.left);
            }
            i++;
            
            // Right child
            if (i < values.Length && values[i] != "null") 
            {
                node.right = new TreeNode(int.Parse(values[i]));
                queue.Enqueue(node.right);
            }
            i++;
        }
        
        return root;
    }
    
    // BST Serialization (Space Optimized)
    public static string SerializeBST(TreeNode root) 
    {
        var result = new List<int>();
        SerializeBSTHelper(root, result);
        return string.Join(",", result);
    }
    
    private static void SerializeBSTHelper(TreeNode node, List<int> result) 
    {
        if (node == null) return;
        
        result.Add(node.val);
        SerializeBSTHelper(node.left, result);
        SerializeBSTHelper(node.right, result);
    }
    
    public static TreeNode DeserializeBST(string data) 
    {
        if (string.IsNullOrEmpty(data)) return null;
        
        var values = Array.ConvertAll(data.Split(','), int.Parse);
        int index = 0;
        return DeserializeBSTHelper(values, ref index, int.MinValue, int.MaxValue);
    }
    
    private static TreeNode DeserializeBSTHelper(int[] values, ref int index, int minVal, int maxVal) 
    {
        if (index >= values.Length) return null;
        
        int val = values[index];
        if (val < minVal || val > maxVal) return null;
        
        index++;
        TreeNode node = new TreeNode(val);
        node.left = DeserializeBSTHelper(values, ref index, minVal, val);
        node.right = DeserializeBSTHelper(values, ref index, val, maxVal);
        
        return node;
    }
    
    // Generic Tree Serialization with Custom Format
    public static string SerializeCustom(TreeNode root) 
    {
        if (root == null) return "#";
        
        return $"{root.val}({SerializeCustom(root.left)},{SerializeCustom(root.right)})";
    }
    
    public static TreeNode DeserializeCustom(string data) 
    {
        int index = 0;
        return DeserializeCustomHelper(data, ref index);
    }
    
    private static TreeNode DeserializeCustomHelper(string data, ref int index) 
    {
        if (index >= data.Length || data[index] == '#') 
        {
            if (index < data.Length) index++; // Skip '#'
            return null;
        }
        
        // Parse value
        int start = index;
        while (index < data.Length && data[index] != '(') 
        {
            index++;
        }
        
        int val = int.Parse(data.Substring(start, index - start));
        TreeNode node = new TreeNode(val);
        
        if (index < data.Length && data[index] == '(') 
        {
            index++; // Skip '('
            node.left = DeserializeCustomHelper(data, ref index);
            
            if (index < data.Length && data[index] == ',') 
            {
                index++; // Skip ','
                node.right = DeserializeCustomHelper(data, ref index);
            }
            
            if (index < data.Length && data[index] == ')') 
            {
                index++; // Skip ')'
            }
        }
        
        return node;
    }
}

// Trie Implementation
public class TrieNode 
{
    public Dictionary<char, TrieNode> Children { get; set; }
    public bool IsEndOfWord { get; set; }
    
    public TrieNode() 
    {
        Children = new Dictionary<char, TrieNode>();
        IsEndOfWord = false;
    }
}

public class Trie 
{
    private TrieNode root;
    
    public Trie() 
    {
        root = new TrieNode();
    }
    
    public void Insert(string word) 
    {
        TrieNode current = root;
        
        foreach (char c in word) 
        {
            if (!current.Children.ContainsKey(c)) 
            {
                current.Children[c] = new TrieNode();
            }
            current = current.Children[c];
        }
        
        current.IsEndOfWord = true;
    }
    
    public bool Search(string word) 
    {
        TrieNode node = SearchPrefix(word);
        return node != null && node.IsEndOfWord;
    }
    
    public bool StartsWith(string prefix) 
    {
        return SearchPrefix(prefix) != null;
    }
    
    private TrieNode SearchPrefix(string prefix) 
    {
        TrieNode current = root;
        
        foreach (char c in prefix) 
        {
            if (!current.Children.ContainsKey(c)) 
            {
                return null;
            }
            current = current.Children[c];
        }
        
        return current;
    }
    
    public List<string> GetWordsWithPrefix(string prefix) 
    {
        var result = new List<string>();
        TrieNode prefixNode = SearchPrefix(prefix);
        
        if (prefixNode != null) 
        {
            DFS(prefixNode, prefix, result);
        }
        
        return result;
    }
    
    private void DFS(TrieNode node, string current, List<string> result) 
    {
        if (node.IsEndOfWord) 
        {
            result.Add(current);
        }
        
        foreach (var kvp in node.Children) 
        {
            DFS(kvp.Value, current + kvp.Key, result);
        }
    }
    
    public bool Delete(string word) 
    {
        return DeleteHelper(root, word, 0);
    }
    
    private bool DeleteHelper(TrieNode node, string word, int index) 
    {
        if (index == word.Length) 
        {
            if (!node.IsEndOfWord) return false;
            
            node.IsEndOfWord = false;
            return node.Children.Count == 0;
        }
        
        char c = word[index];
        if (!node.Children.ContainsKey(c)) return false;
        
        TrieNode child = node.Children[c];
        bool shouldDeleteChild = DeleteHelper(child, word, index + 1);
        
        if (shouldDeleteChild) 
        {
            node.Children.Remove(c);
            return !node.IsEndOfWord && node.Children.Count == 0;
        }
        
        return false;
    }
}
```

---

## 🎯 Common Patterns & Tips

### Pattern Recognition
- **Tree Traversal:** Use DFS for deep searches, BFS for level-by-level processing
- **BST Operations:** Leverage the ordered property for efficient search/insert/delete
- **Tree Validation:** Use recursive approaches with boundary checking
- **LCA Problems:** Consider parent pointers, path storage, or recursive solutions
- **Serialization:** Choose format based on use case (preorder for reconstruction, level-order for visualization)

### Optimization Tips
1. **Use iterative approaches** to avoid stack overflow on deep trees
2. **Consider parent pointers** for upward traversal problems
3. **Leverage BST properties** for O(log n) operations
4. **Use level-order traversal** for problems requiring level information
5. **Implement morris traversal** for O(1) space complexity

### Common Pitfalls
- **Null pointer exceptions** - always check for null nodes
- **Stack overflow** on unbalanced trees with recursive solutions
- **Incorrect BST validation** - don't just check parent-child relationships
- **Memory leaks** in languages requiring manual memory management
- **Edge cases** with empty trees, single nodes, or leaf nodes

---

## 📚 Related LeetCode Problems

### Easy
- [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [Same Tree](https://leetcode.com/problems/same-tree/)
- [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

### Medium
- [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
- [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

### Hard
- [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
- [Serialize and Deserialize N-ary Tree](https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/)
- [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/)

---

[← Back to Main Guide](./README.md)
