# 🗂️ Hash Maps & Sets

## 📋 Overview

**Hash Maps** (dictionaries) store key-value pairs with O(1) average access time using hash functions. **Sets** store unique elements and are typically implemented using hash tables for fast membership testing.

---

## 🎯 Key Properties

- **Fast Access:** O(1) average time for search, insert, and delete operations
- **Hash Function:** Maps keys to array indices for efficient storage
- **Collision Handling:** Uses chaining or open addressing for hash collisions
- **Dynamic Size:** Automatically resizes when load factor exceeds threshold
- **Unordered:** Elements don't maintain insertion order (unless specified)

---

## 📊 Time & Space Complexity

| Operation | Average Case | Worst Case | Space |
|-----------|-------------|------------|-------|
| Search | O(1) | O(n) | O(n) |
| Insert | O(1) | O(n) | O(n) |
| Delete | O(1) | O(n) | O(n) |
| Iteration | O(n) | O(n) | O(1) |

---

## 🔍 Visual Representation

```
Hash Map Structure:
Keys → Hash Function → Index → Bucket

Example with Chaining:
Index 0: "apple" → 5
Index 1: "banana" → 7, "grape" → 3  (collision handled by chaining)
Index 2: (empty)
Index 3: "orange" → 2

Hash Set Structure:
Values → Hash Function → Index → Bucket
{"red", "blue", "green"} → [true, false, true, true, false]
```

---

## 🚀 Top 5 Essential Algorithms

### 1. Two Sum Pattern

**Use Cases:** Finding pairs with target sum, complement searching, duplicate detection

**Algorithm Steps:**
1. **Initialize:** Create hash map to store seen values and their indices
2. **Iterate:** For each number, calculate its complement (target - current)
3. **Check:** Look up complement in hash map for O(1) access
4. **Found:** If complement exists, return indices immediately
5. **Store:** Add current number and index to hash map for future lookups

**Process Visualization:**
```
Two Sum: nums=[2, 7, 11, 15], target=9

Step 1: i=0, nums[0]=2, complement=9-2=7
        seen={} → 7 not found → seen={2:0}

Step 2: i=1, nums[1]=7, complement=9-7=2  
        seen={2:0} → 2 found at index 0! → return [0,1]

Three Sum: nums=[-1,0,1,2,-1,-4], target=0

Sort: [-4,-1,-1,0,1,2]
i=0: nums[0]=-4, target=-(-4)=4, need pairs that sum to 4
     j=1: nums[1]=-1, complement=4-(-1)=5, seen={}
     j=2: nums[2]=-1, complement=4-(-1)=5, seen={-1}, no 5
     j=3: nums[3]=0, complement=4-0=4, seen={-1,-1}, no 4
     ...no valid triplets with -4

i=1: nums[1]=-1, target=-(-1)=1, need pairs that sum to 1
     j=2: nums[2]=-1, complement=1-(-1)=2, seen={}
     j=3: nums[3]=0, complement=1-0=1, seen={-1}, no 1
     j=4: nums[4]=1, complement=1-1=0, seen={-1,0}, found 0!
     → triplet [-1,-1,1,0] but wait, need 0 before 1
     → found: [-1,0,1] ✓
```



#### C# Implementation
```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class TwoSumPattern 
{
    /// <summary>
    /// Classic Two Sum: Find indices of two numbers that add up to target
    /// Time: O(n), Space: O(n)
    /// </summary>
    /// <param name="nums">Array of integers</param>
    /// <param name="target">Target sum</param>
    /// <returns>Indices of the two numbers</returns>
    public static int[] TwoSum(int[] nums, int target) 
    {
        // Hash map to store: value → index
        var seen = new Dictionary<int, int>();
        
        for (int i = 0; i < nums.Length; i++) 
        {
            int complement = target - nums[i];  // What we need to find
            
            // Check if complement exists in our seen values
            if (seen.ContainsKey(complement)) 
            {
                return new int[] { seen[complement], i };  // Found pair!
            }
            
            // Store current number and its index for future complement checks
            seen[nums[i]] = i;
        }
        
        return new int[] { };  // No valid pair found
    }
    
    /// <summary>
    /// Three Sum: Find all unique triplets that sum to zero
    /// Time: O(n²), Space: O(n) for hash set + O(k) for result where k is triplets count
    /// </summary>
    /// <param name="nums">Array of integers</param>
    /// <returns>List of unique triplets that sum to zero</returns>
    public static IList<IList<int>> ThreeSum(int[] nums) 
    {
        Array.Sort(nums);  // Sort to handle duplicates and enable early termination
        var result = new List<IList<int>>();
        
        for (int i = 0; i < nums.Length - 2; i++) 
        {
            // Skip duplicates for first element
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            var seen = new HashSet<int>();  // Track seen numbers for current iteration
            int target = -nums[i];          // We want nums[j] + nums[k] = -nums[i]
            
            for (int j = i + 1; j < nums.Length; j++) 
            {
                int complement = target - nums[j];  // What we need to complete the triplet
                
                if (seen.Contains(complement)) 
                {
                    result.Add(new List<int> { nums[i], complement, nums[j] });
                    
                    // Skip duplicates for second element
                    while (j + 1 < nums.Length && nums[j] == nums[j + 1]) 
                    {
                        j++;
                    }
                }
                
                seen.Add(nums[j]);  // Add current number to seen set
            }
        }
        
        return result;
    }
    
    /// <summary>
    /// Four Sum: Find all unique quadruplets that sum to target
    /// Time: O(n³), Space: O(n)
    /// </summary>
    /// <param name="nums">Array of integers</param>
    /// <param name="target">Target sum</param>
    /// <returns>List of unique quadruplets</returns>
    public static IList<IList<int>> FourSum(int[] nums, int target) 
    {
        Array.Sort(nums);
        var result = new List<IList<int>>();
        int n = nums.Length;
        
        for (int i = 0; i < n - 3; i++) 
        {
            // Skip duplicates for first element
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            for (int j = i + 1; j < n - 2; j++) 
            {
                // Skip duplicates for second element
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;
                
                var seen = new HashSet<int>();
                long currentTarget = (long)target - nums[i] - nums[j];  // Prevent overflow
                
                for (int k = j + 1; k < n; k++) 
                {
                    long complement = currentTarget - nums[k];
                    
                    // Check if complement fits in int range and exists in seen
                    if (complement >= int.MinValue && complement <= int.MaxValue && 
                        seen.Contains((int)complement)) 
                    {
                        result.Add(new List<int> { nums[i], nums[j], (int)complement, nums[k] });
                        
                        // Skip duplicates for third element
                        while (k + 1 < n && nums[k] == nums[k + 1]) 
                        {
                            k++;
                        }
                    }
                    
                    seen.Add(nums[k]);
                }
            }
        }
        
        return result;
    }
    
    /// <summary>
    /// Two Sum with multiple solutions: Find all pairs that sum to target
    /// Time: O(n), Space: O(n)
    /// </summary>
    /// <param name="nums">Array of integers (may contain duplicates)</param>
    /// <param name="target">Target sum</param>
    /// <returns>List of all valid index pairs</returns>
    public static IList<int[]> TwoSumAllPairs(int[] nums, int target) 
    {
        var result = new List<int[]>();
        var indexMap = new Dictionary<int, List<int>>();  // value → list of indices
        
        // Build index map for all numbers
        for (int i = 0; i < nums.Length; i++) 
        {
            if (!indexMap.ContainsKey(nums[i])) 
            {
                indexMap[nums[i]] = new List<int>();
            }
            indexMap[nums[i]].Add(i);
        }
        
        var processedValues = new HashSet<int>();  // Avoid duplicate processing
        
        for (int i = 0; i < nums.Length; i++) 
        {
            int current = nums[i];
            int complement = target - current;
            
            if (processedValues.Contains(current)) continue;
            
            if (indexMap.ContainsKey(complement)) 
            {
                if (current == complement) 
                {
                    // Handle same number case: need at least 2 occurrences
                    var indices = indexMap[current];
                    for (int j = 0; j < indices.Count; j++) 
                    {
                        for (int k = j + 1; k < indices.Count; k++) 
                        {
                            result.Add(new int[] { indices[j], indices[k] });
                        }
                    }
                }
                else 
                {
                    // Different numbers case
                    foreach (int idx1 in indexMap[current]) 
                    {
                        foreach (int idx2 in indexMap[complement]) 
                        {
                            if (idx1 < idx2)  // Ensure consistent ordering
                            {
                                result.Add(new int[] { idx1, idx2 });
                            }
                        }
                    }
                }
                
                processedValues.Add(current);
                processedValues.Add(complement);
            }
        }
        
        return result;
    }
}
                    while (j + 1 < nums.Length && nums[j] == nums[j + 1]) j++;
                }
                
                seen.Add(nums[j]);
            }
        }
        
        return result;
    }
    
    public static IList<IList<int>> FourSum(int[] nums, int target) 
    {
        Array.Sort(nums);
        var result = new List<IList<int>>();
        int n = nums.Length;
        
        for (int i = 0; i < n - 3; i++) 
        {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            for (int j = i + 1; j < n - 2; j++) 
            {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;
                
                var seen = new HashSet<int>();
                long currentTarget = (long)target - nums[i] - nums[j];
                
                for (int k = j + 1; k < n; k++) 
                {
                    int complement = (int)(currentTarget - nums[k]);
                    
                    if (seen.Contains(complement)) 
                    {
                        result.Add(new List<int> { nums[i], nums[j], complement, nums[k] });
                        while (k + 1 < n && nums[k] == nums[k + 1]) k++;
                    }
                    
                    seen.Add(nums[k]);
                }
            }
        }
        
        return result;
    }
}
```

---

### 2. Group Anagrams

**Use Cases:** String grouping, character frequency analysis, pattern matching

**Algorithm Steps:**
1. **Choose Key Strategy:** Sort characters OR count character frequencies
2. **Generate Key:** Create identical keys for anagrams 
3. **Group by Key:** Use hash map with key → list of anagrams
4. **Process All:** Iterate through all strings, generating keys and grouping
5. **Extract Groups:** Return all grouped lists as result

**Process Visualization:**
```
Group Anagrams: ["eat","tea","tan","ate","nat","bat"]

Method 1: Sorted Characters as Key
"eat" → sort → "aet" → groups["aet"] = ["eat"]
"tea" → sort → "aet" → groups["aet"] = ["eat", "tea"]  
"tan" → sort → "ant" → groups["ant"] = ["tan"]
"ate" → sort → "aet" → groups["aet"] = ["eat", "tea", "ate"]
"nat" → sort → "ant" → groups["ant"] = ["tan", "nat"]
"bat" → sort → "abt" → groups["abt"] = ["bat"]

Result: [["eat","tea","ate"], ["tan","nat"], ["bat"]]

Method 2: Character Count as Key  
"eat" → count → [1,0,0,0,1,0...1,0] → "1e1t1a"
"tea" → count → [1,0,0,0,1,0...1,0] → "1e1t1a" (same key!)

Frequency Encoding:
"abcabc" → a:2,b:2,c:2 → "a2b2c2"
"cbabac" → a:2,b:2,c:2 → "a2b2c2" (same signature)
```



#### C# Implementation
```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class AnagramAlgorithms 
{
    /// <summary>
    /// Group anagrams using sorted characters as key
    /// Time: O(n * k log k) where n=number of strings, k=max string length
    /// Space: O(n * k) for storing groups
    /// </summary>
    /// <param name="strs">Array of strings to group</param>
    /// <returns>Groups of anagrams</returns>
    public static IList<IList<string>> GroupAnagrams(string[] strs) 
    {
        var groups = new Dictionary<string, List<string>>();
        
        foreach (string s in strs) 
        {
            // Create canonical key by sorting characters
            var chars = s.ToCharArray();
            Array.Sort(chars);                    // O(k log k) sorting
            string key = new string(chars);       // Anagrams will have identical keys
            
            // Group strings with same key
            if (!groups.ContainsKey(key)) 
            {
                groups[key] = new List<string>();
            }
            groups[key].Add(s);                   // Add to appropriate group
        }
        
        // Convert dictionary values to required return type
        return groups.Values.Cast<IList<string>>().ToList();
    }
    
    /// <summary>
    /// Group anagrams using character frequency counting (more efficient for long strings)
    /// Time: O(n * k) where n=number of strings, k=max string length
    /// Space: O(n * k)
    /// </summary>
    /// <param name="strs">Array of strings to group</param>
    /// <returns>Groups of anagrams</returns>
    public static IList<IList<string>> GroupAnagramsByCount(string[] strs) 
    {
        var groups = new Dictionary<string, List<string>>();
        
        foreach (string s in strs) 
        {
            // Create character frequency signature
            var count = new int[26];              // Assuming only lowercase letters
            foreach (char c in s) 
            {
                count[c - 'a']++;                 // Count frequency of each character
            }
            
            // Create unique key from frequency array
            string key = string.Join(",", count); // e.g., "1,0,1,0,1,0,..." for "ace"
            
            if (!groups.ContainsKey(key)) 
            {
                groups[key] = new List<string>();
            }
            groups[key].Add(s);
        }
        
        return groups.Values.Cast<IList<string>>().ToList();
    }
    
    /// <summary>
    /// Check if two strings are anagrams of each other
    /// Time: O(n), Space: O(1) for lowercase letters only
    /// </summary>
    /// <param name="s">First string</param>
    /// <param name="t">Second string</param>
    /// <returns>True if strings are anagrams</returns>
    public static bool IsAnagram(string s, string t) 
    {
        if (s.Length != t.Length) return false;  // Different lengths can't be anagrams
        
        var count = new Dictionary<char, int>();
        
        // Count characters in first string
        foreach (char c in s) 
        {
            count[c] = count.GetValueOrDefault(c, 0) + 1;
        }
        
        // Subtract characters from second string
        foreach (char c in t) 
        {
            if (!count.ContainsKey(c)) return false;  // Character not in first string
            count[c]--;
            if (count[c] == 0) count.Remove(c);       // Remove when count reaches 0
        }
        
        return count.Count == 0;  // All characters should be consumed
    }
    
    /// <summary>
    /// Find all starting indices of anagrams of pattern in string (sliding window approach)
    /// Time: O(n) where n=length of string s, Space: O(1) for fixed alphabet
    /// </summary>
    /// <param name="s">Source string to search in</param>
    /// <param name="p">Pattern to find anagrams of</param>
    /// <returns>List of starting indices where anagrams are found</returns>
    public static IList<int> FindAnagrams(string s, string p) 
    {
        var result = new List<int>();
        if (p.Length > s.Length) return result;
        
        // Count characters in pattern
        var pCount = new Dictionary<char, int>();
        foreach (char c in p) 
        {
            pCount[c] = pCount.GetValueOrDefault(c, 0) + 1;
        }
        
        var windowCount = new Dictionary<char, int>();
        int windowSize = p.Length;
        
        // Process sliding window
        for (int i = 0; i < s.Length; i++) 
        {
            // Expand window: add character at right
            char rightChar = s[i];
            windowCount[rightChar] = windowCount.GetValueOrDefault(rightChar, 0) + 1;
            
            // Contract window: remove character at left (if window is too large)
            if (i >= windowSize) 
            {
                char leftChar = s[i - windowSize];
                windowCount[leftChar]--;
                if (windowCount[leftChar] == 0) 
                {
                    windowCount.Remove(leftChar);
                }
            }
            
            // Check if current window is anagram of pattern
            if (i >= windowSize - 1 && DictionariesEqual(windowCount, pCount)) 
            {
                result.Add(i - windowSize + 1);  // Add starting index
            }
        }
        
        return result;
    }
    
    /// <summary>
    /// Helper method to compare two dictionaries for equality
    /// </summary>
    private static bool DictionariesEqual(Dictionary<char, int> dict1, Dictionary<char, int> dict2) 
    {
        if (dict1.Count != dict2.Count) return false;
        
        foreach (var kvp in dict1) 
        {
            if (!dict2.ContainsKey(kvp.Key) || dict2[kvp.Key] != kvp.Value) 
            {
                return false;
            }
        }
        return true;
    }
    
    /// <summary>
    /// Advanced: Find shortest anagram substring that contains all characters of pattern
    /// Time: O(n + m), Space: O(m) where n=string length, m=pattern length
    /// </summary>
    /// <param name="s">Source string</param>
    /// <param name="p">Pattern string</param>
    /// <returns>Shortest substring that is anagram containing all pattern characters</returns>
    public static string ShortestAnagramSubstring(string s, string p) 
    {
        if (string.IsNullOrEmpty(s) || string.IsNullOrEmpty(p)) return "";
        
        var pCount = new Dictionary<char, int>();
        foreach (char c in p) 
        {
            pCount[c] = pCount.GetValueOrDefault(c, 0) + 1;
        }
        
        var windowCount = new Dictionary<char, int>();
        int left = 0, minLen = int.MaxValue, minStart = 0;
        int formed = 0;  // Number of unique chars in window with desired frequency
        int required = pCount.Count;
        
        for (int right = 0; right < s.Length; right++) 
        {
            // Expand window
            char rightChar = s[right];
            windowCount[rightChar] = windowCount.GetValueOrDefault(rightChar, 0) + 1;
            
            if (pCount.ContainsKey(rightChar) && 
                windowCount[rightChar] == pCount[rightChar]) 
            {
                formed++;
            }
            
            // Contract window while it's valid
            while (left <= right && formed == required) 
            {
                // Update minimum window
                if (right - left + 1 < minLen) 
                {
                    minLen = right - left + 1;
                    minStart = left;
                }
                
                // Remove leftmost character
                char leftChar = s[left];
                windowCount[leftChar]--;
                if (pCount.ContainsKey(leftChar) && 
                    windowCount[leftChar] < pCount[leftChar]) 
                {
                    formed--;
                }
                left++;
            }
        }
        
        return minLen == int.MaxValue ? "" : s.Substring(minStart, minLen);
    }
}
        var windowCount = new Dictionary<char, int>();
        var result = new List<int>();
        
        foreach (char c in p) 
        {
            pCount[c] = pCount.GetValueOrDefault(c, 0) + 1;
        }
        
        for (int i = 0; i < s.Length; i++) 
        {
            windowCount[s[i]] = windowCount.GetValueOrDefault(s[i], 0) + 1;
            
            if (i >= p.Length) 
            {
                char leftChar = s[i - p.Length];
                windowCount[leftChar]--;
                if (windowCount[leftChar] == 0) 
                {
                    windowCount.Remove(leftChar);
                }
            }
            
            if (windowCount.Count == pCount.Count && 
                windowCount.All(kv => pCount.ContainsKey(kv.Key) && pCount[kv.Key] == kv.Value)) 
            {
                result.Add(i - p.Length + 1);
            }
        }
        
        return result;
    }
}
```

---

### 3. LRU Cache Implementation

**Use Cases:** Caching systems, memory management, most recently used tracking

**Algorithm Steps:**
1. **Combine Structures:** Use HashMap for O(1) access + Doubly Linked List for O(1) insertion/deletion
2. **Track Usage:** Move accessed nodes to head (most recently used)
3. **Manage Capacity:** Remove tail node (least recently used) when capacity exceeded
4. **Maintain Invariant:** Head = most recent, Tail = least recent
5. **Update Atomically:** Every get/put operation updates both HashMap and LinkedList

**Process Visualization:**
```
LRU Cache with capacity=3:

Initial: Head ↔ Tail (empty)

put(1,1): Head ↔ (1,1) ↔ Tail
put(2,2): Head ↔ (2,2) ↔ (1,1) ↔ Tail  
put(3,3): Head ↔ (3,3) ↔ (2,2) ↔ (1,1) ↔ Tail

get(2):   Head ↔ (2,2) ↔ (3,3) ↔ (1,1) ↔ Tail  (move 2 to head)

put(4,4): Head ↔ (4,4) ↔ (2,2) ↔ (3,3) ↔ Tail  (evict 1,1)
          HashMap: {2→node2, 3→node3, 4→node4}

Data Structure Combination:
- HashMap: key → DoublyLinkedListNode (O(1) lookup)
- DoublyLinkedList: maintains usage order (O(1) move to head/remove tail)
```



#### C# Implementation
```csharp
using System;
using System.Collections.Generic;

public class LRUCache 
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
    
    public LRUCache(int capacity) 
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

public class LFUCache 
{
    private readonly int capacity;
    private int minFreq;
    private readonly Dictionary<int, int> keyToVal;
    private readonly Dictionary<int, int> keyToFreq;
    private readonly Dictionary<int, HashSet<int>> freqToKeys;
    
    public LFUCache(int capacity) 
    {
        this.capacity = capacity;
        this.minFreq = 0;
        this.keyToVal = new Dictionary<int, int>();
        this.keyToFreq = new Dictionary<int, int>();
        this.freqToKeys = new Dictionary<int, HashSet<int>>();
    }
    
    private void UpdateFreq(int key) 
    {
        int freq = keyToFreq[key];
        freqToKeys[freq].Remove(key);
        
        if (freq == minFreq && freqToKeys[freq].Count == 0) 
        {
            minFreq++;
        }
        
        int newFreq = freq + 1;
        keyToFreq[key] = newFreq;
        
        if (!freqToKeys.ContainsKey(newFreq)) 
        {
            freqToKeys[newFreq] = new HashSet<int>();
        }
        freqToKeys[newFreq].Add(key);
    }
    
    public int Get(int key) 
    {
        if (!keyToVal.ContainsKey(key)) 
        {
            return -1;
        }
        
        UpdateFreq(key);
        return keyToVal[key];
    }
    
    public void Put(int key, int value) 
    {
        if (capacity <= 0) return;
        
        if (keyToVal.ContainsKey(key)) 
        {
            keyToVal[key] = value;
            UpdateFreq(key);
            return;
        }
        
        if (keyToVal.Count >= capacity) 
        {
            var keyToRemove = freqToKeys[minFreq].First();
            freqToKeys[minFreq].Remove(keyToRemove);
            keyToVal.Remove(keyToRemove);
            keyToFreq.Remove(keyToRemove);
        }
        
        keyToVal[key] = value;
        keyToFreq[key] = 1;
        minFreq = 1;
        
        if (!freqToKeys.ContainsKey(1)) 
        {
            freqToKeys[1] = new HashSet<int>();
        }
        freqToKeys[1].Add(key);
    }
}
```

---

### 4. Consistent Hashing

**Use Cases:** Distributed systems, load balancing, cache partitioning



#### C# Implementation
```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;

public class ConsistentHash 
{
    private readonly int replicas;
    private readonly SortedDictionary<uint, string> ring;
    private readonly MD5 md5;
    
    public ConsistentHash(IEnumerable<string> nodes = null, int replicas = 3) 
    {
        this.replicas = replicas;
        this.ring = new SortedDictionary<uint, string>();
        this.md5 = MD5.Create();
        
        if (nodes != null) 
        {
            foreach (var node in nodes) 
            {
                AddNode(node);
            }
        }
    }
    
    private uint Hash(string input) 
    {
        byte[] data = md5.ComputeHash(Encoding.UTF8.GetBytes(input));
        return BitConverter.ToUInt32(data, 0);
    }
    
    public void AddNode(string node) 
    {
        for (int i = 0; i < replicas; i++) 
        {
            string replicaKey = $"{node}:{i}";
            uint hashValue = Hash(replicaKey);
            ring[hashValue] = node;
        }
    }
    
    public void RemoveNode(string node) 
    {
        for (int i = 0; i < replicas; i++) 
        {
            string replicaKey = $"{node}:{i}";
            uint hashValue = Hash(replicaKey);
            ring.Remove(hashValue);
        }
    }
    
    public string GetNode(string key) 
    {
        if (ring.Count == 0) return null;
        
        uint hashValue = Hash(key);
        
        var nodeHash = ring.Keys.FirstOrDefault(k => k >= hashValue);
        if (nodeHash == 0) 
        {
            nodeHash = ring.Keys.First();
        }
        
        return ring[nodeHash];
    }
    
    public List<string> GetNodes(string key, int count) 
    {
        if (ring.Count == 0 || count <= 0) return new List<string>();
        
        uint hashValue = Hash(key);
        var nodes = new List<string>();
        var seen = new HashSet<string>();
        
        var sortedHashes = ring.Keys.ToArray();
        int startIndex = Array.BinarySearch(sortedHashes, hashValue);
        if (startIndex < 0) startIndex = ~startIndex;
        
        for (int i = 0; i < ring.Count && nodes.Count < count; i++) 
        {
            int index = (startIndex + i) % sortedHashes.Length;
            string node = ring[sortedHashes[index]];
            
            if (!seen.Contains(node)) 
            {
                nodes.Add(node);
                seen.Add(node);
            }
        }
        
        return nodes;
    }
}

public class RendezvousHash 
{
    private readonly HashSet<string> nodes;
    private readonly MD5 md5;
    
    public RendezvousHash(IEnumerable<string> nodes = null) 
    {
        this.nodes = new HashSet<string>(nodes ?? Enumerable.Empty<string>());
        this.md5 = MD5.Create();
    }
    
    private uint Hash(string key, string node) 
    {
        string combined = $"{key}:{node}";
        byte[] data = md5.ComputeHash(Encoding.UTF8.GetBytes(combined));
        return BitConverter.ToUInt32(data, 0);
    }
    
    public void AddNode(string node) 
    {
        nodes.Add(node);
    }
    
    public void RemoveNode(string node) 
    {
        nodes.Remove(node);
    }
    
    public string GetNode(string key) 
    {
        if (nodes.Count == 0) return null;
        
        uint maxHash = 0;
        string selectedNode = null;
        
        foreach (var node in nodes) 
        {
            uint hashValue = Hash(key, node);
            if (hashValue > maxHash) 
            {
                maxHash = hashValue;
                selectedNode = node;
            }
        }
        
        return selectedNode;
    }
    
    public List<string> GetNodes(string key, int count) 
    {
        if (nodes.Count == 0 || count <= 0) return new List<string>();
        
        var nodeHashes = nodes.Select(node => new { 
            Node = node, 
            Hash = Hash(key, node) 
        }).OrderByDescending(x => x.Hash).Take(count);
        
        return nodeHashes.Select(x => x.Node).ToList();
    }
}
```

---

### 5. Bloom Filter

**Use Cases:** Membership testing, spell checkers, web crawling, database optimization



#### C# Implementation
```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;

public class BloomFilter 
{
    private readonly int expectedItems;
    private readonly double falsePositiveRate;
    private readonly int bitArraySize;
    private readonly int numHashFunctions;
    private readonly bool[] bitArray;
    private readonly MD5 md5;
    
    public int ItemsAdded { get; private set; }
    
    public BloomFilter(int expectedItems, double falsePositiveRate = 0.1) 
    {
        this.expectedItems = expectedItems;
        this.falsePositiveRate = falsePositiveRate;
        
        this.bitArraySize = CalculateBitArraySize();
        this.numHashFunctions = CalculateNumHashFunctions();
        this.bitArray = new bool[bitArraySize];
        this.md5 = MD5.Create();
        this.ItemsAdded = 0;
    }
    
    private int CalculateBitArraySize() 
    {
        double m = -(expectedItems * Math.Log(falsePositiveRate)) / (Math.Log(2) * Math.Log(2));
        return (int)m;
    }
    
    private int CalculateNumHashFunctions() 
    {
        double k = (bitArraySize / (double)expectedItems) * Math.Log(2);
        return (int)k;
    }
    
    private int Hash(string item, int seed) 
    {
        string hashInput = $"{item}{seed}";
        byte[] data = md5.ComputeHash(Encoding.UTF8.GetBytes(hashInput));
        int hashValue = Math.Abs(BitConverter.ToInt32(data, 0));
        return hashValue % bitArraySize;
    }
    
    public void Add(string item) 
    {
        for (int i = 0; i < numHashFunctions; i++) 
        {
            int index = Hash(item, i);
            bitArray[index] = true;
        }
        ItemsAdded++;
    }
    
    public bool MightContain(string item) 
    {
        for (int i = 0; i < numHashFunctions; i++) 
        {
            int index = Hash(item, i);
            if (!bitArray[index]) 
            {
                return false;
            }
        }
        return true;
    }
    
    public double CurrentFalsePositiveRate() 
    {
        if (ItemsAdded == 0) return 0.0;
        
        double probBitZero = Math.Pow(1 - 1.0 / bitArraySize, numHashFunctions * ItemsAdded);
        return Math.Pow(1 - probBitZero, numHashFunctions);
    }
}

public class CountingBloomFilter 
{
    private readonly int expectedItems;
    private readonly double falsePositiveRate;
    private readonly int arraySize;
    private readonly int numHashFunctions;
    private readonly int[] counters;
    private readonly MD5 md5;
    
    public int ItemsAdded { get; private set; }
    
    public CountingBloomFilter(int expectedItems, double falsePositiveRate = 0.1) 
    {
        this.expectedItems = expectedItems;
        this.falsePositiveRate = falsePositiveRate;
        
        this.arraySize = CalculateArraySize();
        this.numHashFunctions = CalculateNumHashFunctions();
        this.counters = new int[arraySize];
        this.md5 = MD5.Create();
        this.ItemsAdded = 0;
    }
    
    private int CalculateArraySize() 
    {
        double m = -(expectedItems * Math.Log(falsePositiveRate)) / (Math.Log(2) * Math.Log(2));
        return (int)m;
    }
    
    private int CalculateNumHashFunctions() 
    {
        double k = (arraySize / (double)expectedItems) * Math.Log(2);
        return (int)k;
    }
    
    private int Hash(string item, int seed) 
    {
        string hashInput = $"{item}{seed}";
        byte[] data = md5.ComputeHash(Encoding.UTF8.GetBytes(hashInput));
        int hashValue = Math.Abs(BitConverter.ToInt32(data, 0));
        return hashValue % arraySize;
    }
    
    public void Add(string item) 
    {
        for (int i = 0; i < numHashFunctions; i++) 
        {
            int index = Hash(item, i);
            counters[index]++;
        }
        ItemsAdded++;
    }
    
    public bool Remove(string item) 
    {
        if (!MightContain(item)) return false;
        
        for (int i = 0; i < numHashFunctions; i++) 
        {
            int index = Hash(item, i);
            if (counters[index] > 0) 
            {
                counters[index]--;
            }
        }
        
        ItemsAdded = Math.Max(0, ItemsAdded - 1);
        return true;
    }
    
    public bool MightContain(string item) 
    {
        for (int i = 0; i < numHashFunctions; i++) 
        {
            int index = Hash(item, i);
            if (counters[index] == 0) 
            {
                return false;
            }
        }
        return true;
    }
}

public class ScalableBloomFilter 
{
    private readonly int initialCapacity;
    private readonly double errorRate;
    private readonly int growthFactor;
    private readonly List<BloomFilter> filters;
    
    public ScalableBloomFilter(int initialCapacity = 1000, double errorRate = 0.1, int growthFactor = 2) 
    {
        this.initialCapacity = initialCapacity;
        this.errorRate = errorRate;
        this.growthFactor = growthFactor;
        this.filters = new List<BloomFilter>();
        
        AddFilter();
    }
    
    private void AddFilter() 
    {
        int capacity = initialCapacity * (int)Math.Pow(growthFactor, filters.Count);
        double filterErrorRate = errorRate / Math.Pow(growthFactor, filters.Count);
        
        var newFilter = new BloomFilter(capacity, filterErrorRate);
        filters.Add(newFilter);
    }
    
    public void Add(string item) 
    {
        var currentFilter = filters.Last();
        if (currentFilter.ItemsAdded >= initialCapacity * Math.Pow(growthFactor, filters.Count - 1)) 
        {
            AddFilter();
            currentFilter = filters.Last();
        }
        
        currentFilter.Add(item);
    }
    
    public bool MightContain(string item) 
    {
        return filters.Any(filter => filter.MightContain(item));
    }
    
    public double CurrentFalsePositiveRate() 
    {
        if (!filters.Any()) return 0.0;
        
        double probNotFp = 1.0;
        foreach (var filter in filters) 
        {
            double fpRate = filter.CurrentFalsePositiveRate();
            probNotFp *= (1 - fpRate);
        }
        
        return 1 - probNotFp;
    }
    
    public int FilterCount => filters.Count;
}
```

---

## 🎯 Common Patterns & Tips

### Pattern Recognition
- **Two Sum Pattern:** Use hash map to find complements in O(1) time
- **Group Anagrams:** Use sorted string or character count as hash key
- **LRU Cache:** Combine hash map with doubly linked list for O(1) operations
- **Consistent Hashing:** Use for distributed systems and load balancing
- **Bloom Filter:** Use for fast membership testing with acceptable false positives

### Optimization Tips
1. **Choose right data structure:** HashMap for lookups, HashSet for uniqueness
2. **Handle collisions properly:** Use chaining or open addressing
3. **Monitor load factor:** Resize when load factor exceeds 0.75
4. **Use appropriate hash functions:** Avoid clustering and ensure uniform distribution
5. **Consider memory usage:** Trade-off between space and time complexity

### Common Pitfalls
- **Hash collision handling** - ensure your implementation handles collisions properly
- **Integer overflow in hash functions** - use appropriate data types
- **Floating point precision** in bloom filter calculations
- **Thread safety** in concurrent environments
- **Memory leaks** in cache implementations

---

## 📚 Related LeetCode Problems

### Easy
- [Two Sum](https://leetcode.com/problems/two-sum/)
- [Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

### Medium
- [Group Anagrams](https://leetcode.com/problems/group-anagrams/)
- [LRU Cache](https://leetcode.com/problems/lru-cache/)
- [Design HashMap](https://leetcode.com/problems/design-hashmap/)

### Hard
- [LFU Cache](https://leetcode.com/problems/lfu-cache/)
- [Design Twitter](https://leetcode.com/problems/design-twitter/)
- [All O`one Data Structure](https://leetcode.com/problems/all-oone-data-structure/)

---

[← Back to Main Guide](./README.md)
