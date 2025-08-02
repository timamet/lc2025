# 🔤 Arrays & Strings

## 📋 Overview

**Arrays** are fixed-size, indexed collections that store elements of the same type in contiguous memory locations. **Strings** are immutable sequences of characters that can be treated as character arrays in many contexts.

---

## 🎯 Key Properties

- **Random Access:** O(1) time to access any element by index
- **Memory Layout:** Contiguous memory allocation for cache efficiency
- **Fixed Size:** Traditional arrays have fixed size (dynamic arrays like Python lists are resizable)
- **Type Homogeneity:** All elements must be of the same type (in statically typed languages)

---

## 📊 Time & Space Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Access by index | O(1) | O(1) |
| Search (unsorted) | O(n) | O(1) |
| Search (sorted) | O(log n) | O(1) |
| Insertion | O(n) | O(1) |
| Deletion | O(n) | O(1) |

---

## 🔍 Visual Representation

```
Array Structure:
Index:     0     1     2     3     4
Array:   [10]  [20]  [30]  [40]  [50]
Memory:  1000  1004  1008  1012  1016  (byte addresses)

String Structure:
Index:     0     1     2     3     4
String:   'h'   'e'   'l'   'l'   'o'
```

---

## 🚀 Top 5 Essential Algorithms

### 1. Two Pointers Technique

**Use Cases:** Finding pairs, palindrome checking, array partitioning

**Algorithm Steps:**
1. **Initialize:** Place two pointers at different positions (typically start and end)
2. **Compare:** Evaluate the condition based on pointer values
3. **Move:** Adjust pointers based on comparison result
4. **Converge:** Continue until pointers meet or cross
5. **Result:** Return the answer when condition is satisfied

**Process Visualization:**
```
Two Sum in Sorted Array [1, 2, 3, 4, 6], target = 6

Step 1: left=0, right=4  →  arr[0] + arr[4] = 1 + 6 = 7 > 6  →  move right--
Step 2: left=0, right=3  →  arr[0] + arr[3] = 1 + 4 = 5 < 6  →  move left++
Step 3: left=1, right=3  →  arr[1] + arr[3] = 2 + 4 = 6 = 6  →  FOUND!

Palindrome Check "racecar"
Step 1: left=0, right=6  →  'r' == 'r' ✓  →  move both inward
Step 2: left=1, right=5  →  'a' == 'a' ✓  →  move both inward  
Step 3: left=2, right=4  →  'c' == 'c' ✓  →  move both inward
Step 4: left=3, right=3  →  pointers met  →  PALINDROME!
```

#### C# Implementation
```csharp
using System;

public class TwoPointers 
{
    /// <summary>
    /// Finds two numbers in a sorted array that add up to target
    /// Time: O(n), Space: O(1)
    /// </summary>
    /// <param name="arr">Sorted integer array</param>
    /// <param name="target">Target sum to find</param>
    /// <returns>Indices of the two numbers, empty array if not found</returns>
    public static int[] TwoSumSorted(int[] arr, int target) 
    {
        int left = 0, right = arr.Length - 1;  // Initialize pointers at both ends
        
        while (left < right)  // Continue until pointers meet
        {
            int currentSum = arr[left] + arr[right];  // Calculate current sum
            
            if (currentSum == target)
                return new int[] { left, right };     // Found the pair!
            else if (currentSum < target)
                left++;                               // Sum too small, move left pointer right
            else
                right--;                              // Sum too large, move right pointer left
        }
        
        return new int[] { };  // No valid pair found
    }
    
    /// <summary>
    /// Checks if a string is a palindrome using two pointers
    /// Time: O(n), Space: O(1)
    /// </summary>
    /// <param name="s">Input string to check</param>
    /// <returns>True if palindrome, false otherwise</returns>
    public static bool IsPalindrome(string s) 
    {
        int left = 0, right = s.Length - 1;  // Start from both ends
        
        while (left < right)  // Check characters moving inward
        {
            if (s[left] != s[right])  // Characters don't match
                return false;         // Not a palindrome
            
            left++;   // Move left pointer forward
            right--;  // Move right pointer backward
        }
        
        return true;  // All characters matched, it's a palindrome!
    }
    
    /// <summary>
    /// Advanced: Remove duplicates from sorted array in-place
    /// Time: O(n), Space: O(1)
    /// </summary>
    /// <param name="nums">Sorted array with duplicates</param>
    /// <returns>Length of array after removing duplicates</returns>
    public static int RemoveDuplicates(int[] nums) 
    {
        if (nums.Length <= 1) return nums.Length;
        
        int writePtr = 1;  // Pointer for next unique element position
        
        for (int readPtr = 1; readPtr < nums.Length; readPtr++) 
        {
            // If current element is different from previous
            if (nums[readPtr] != nums[readPtr - 1]) 
            {
                nums[writePtr] = nums[readPtr];  // Place at write position
                writePtr++;                      // Move write pointer forward
            }
            // If duplicate, just continue reading (skip it)
        }
        
        return writePtr;  // Return new length
    }
}
```

---

### 2. Sliding Window

**Use Cases:** Subarray problems, maximum/minimum in window, string matching

**Algorithm Steps:**
1. **Initialize:** Create window with initial size and calculate initial result
2. **Expand:** Extend window to the right by adding new elements
3. **Contract:** Shrink window from left when conditions are violated
4. **Update:** Track the optimal result as window slides
5. **Continue:** Repeat until entire array/string is processed

**Process Visualization:**
```
Fixed Window - Max Sum of Size 3 in [1, 4, 2, 9, 3]:

Step 1: [1, 4, 2] 9, 3     window_sum = 7, max_sum = 7
Step 2:  1 [4, 2, 9] 3     window_sum = 15, max_sum = 15  
Step 3:  1, 4 [2, 9, 3]    window_sum = 14, max_sum = 15

Variable Window - Longest Substring with K=2 Distinct in "araaci":

Step 1: a          window="a", distinct=1, max_len=1
Step 2: ar         window="ar", distinct=2, max_len=2
Step 3: ara        window="ara", distinct=2, max_len=3
Step 4: araa       window="araa", distinct=2, max_len=4
Step 5: araac      window="araac", distinct=3 > k, shrink!
        →  raac    window="raac", distinct=2, max_len=4
Step 6: araaci     window="raaci", distinct=3 > k, shrink!
        →  aaci    window="aaci", distinct=2, max_len=4
```



#### C# Implementation
```csharp
using System;
using System.Collections.Generic;

public class SlidingWindow 
{
    /// <summary>
    /// Finds maximum sum of subarray with fixed size k (Fixed Window)
    /// Time: O(n), Space: O(1)
    /// </summary>
    /// <param name="arr">Input array of integers</param>
    /// <param name="k">Fixed window size</param>
    /// <returns>Maximum sum of any subarray of size k</returns>
    public static int MaxSumSubarrayK(int[] arr, int k) 
    {
        if (arr.Length < k) return -1;  // Not enough elements
        
        // Step 1: Calculate sum of first window
        int windowSum = 0;
        for (int i = 0; i < k; i++) 
        {
            windowSum += arr[i];  // Build initial window
        }
        
        int maxSum = windowSum;  // Track maximum sum found
        
        // Step 2: Slide the window across remaining elements
        for (int i = 0; i < arr.Length - k; i++) 
        {
            // Remove leftmost element, add new rightmost element
            windowSum = windowSum - arr[i] + arr[i + k];
            maxSum = Math.Max(maxSum, windowSum);  // Update maximum if needed
        }
        
        return maxSum;
    }
    
    /// <summary>
    /// Finds longest substring with at most k distinct characters (Variable Window)
    /// Time: O(n), Space: O(k)
    /// </summary>
    /// <param name="s">Input string</param>
    /// <param name="k">Maximum number of distinct characters allowed</param>
    /// <returns>Length of longest valid substring</returns>
    public static int LongestSubstringKDistinct(string s, int k) 
    {
        if (k == 0) return 0;  // No distinct characters allowed
        
        var charCount = new Dictionary<char, int>();  // Track character frequencies
        int left = 0, maxLength = 0;  // Window boundaries and result
        
        // Expand window by moving right pointer
        for (int right = 0; right < s.Length; right++) 
        {
            // Step 1: Add current character to window
            char rightChar = s[right];
            charCount[rightChar] = charCount.GetValueOrDefault(rightChar, 0) + 1;
            
            // Step 2: Contract window if we have too many distinct characters
            while (charCount.Count > k) 
            {
                char leftChar = s[left];
                charCount[leftChar]--;  // Decrease frequency
                
                // Remove character if frequency becomes 0
                if (charCount[leftChar] == 0) 
                {
                    charCount.Remove(leftChar);
                }
                left++;  // Shrink window from left
            }
            
            // Step 3: Update maximum length found
            maxLength = Math.Max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
    
    /// <summary>
    /// Advanced: Minimum window substring containing all characters of pattern
    /// Time: O(n + m), Space: O(m) where n=text length, m=pattern length
    /// </summary>
    /// <param name="text">Source text to search in</param>
    /// <param name="pattern">Pattern to find</param>
    /// <returns>Smallest window containing all pattern characters</returns>
    public static string MinWindowSubstring(string text, string pattern) 
    {
        if (string.IsNullOrEmpty(text) || string.IsNullOrEmpty(pattern)) 
            return "";
        
        // Step 1: Count characters in pattern
        var patternCount = new Dictionary<char, int>();
        foreach (char c in pattern) 
        {
            patternCount[c] = patternCount.GetValueOrDefault(c, 0) + 1;
        }
        
        var windowCount = new Dictionary<char, int>();
        int left = 0, minLen = int.MaxValue, minStart = 0;
        int formed = 0;  // Number of unique characters in window with desired frequency
        int required = patternCount.Count;  // Number of unique characters in pattern
        
        // Step 2: Expand and contract window
        for (int right = 0; right < text.Length; right++) 
        {
            // Expand window
            char rightChar = text[right];
            windowCount[rightChar] = windowCount.GetValueOrDefault(rightChar, 0) + 1;
            
            // Check if frequency matches pattern requirement
            if (patternCount.ContainsKey(rightChar) && 
                windowCount[rightChar] == patternCount[rightChar]) 
            {
                formed++;
            }
            
            // Contract window if all characters are satisfied
            while (left <= right && formed == required) 
            {
                // Update minimum window if current is smaller
                if (right - left + 1 < minLen) 
                {
                    minLen = right - left + 1;
                    minStart = left;
                }
                
                // Try to shrink window
                char leftChar = text[left];
                windowCount[leftChar]--;
                if (patternCount.ContainsKey(leftChar) && 
                    windowCount[leftChar] < patternCount[leftChar]) 
                {
                    formed--;
                }
                left++;
            }
        }
        
        return minLen == int.MaxValue ? "" : text.Substring(minStart, minLen);
    }
}
            
            while (charCount.Count > k) 
            {
                charCount[s[left]]--;
                if (charCount[s[left]] == 0) 
                {
                    charCount.Remove(s[left]);
                }
                left++;
            }
            
            maxLength = Math.Max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
}
```

---

### 3. Binary Search

**Use Cases:** Searching in sorted arrays, finding boundaries, optimization problems

**Algorithm Steps:**
1. **Initialize:** Set left=0, right=length-1 boundaries  
2. **Calculate:** Find middle index: mid = left + (right-left)/2
3. **Compare:** Check if arr[mid] equals, is less than, or greater than target
4. **Narrow:** Eliminate half the search space based on comparison
5. **Repeat:** Continue until found or search space exhausted

**Process Visualization:**
```
Binary Search for target=5 in [1, 3, 5, 7, 9, 11, 13]:

Initial: [1, 3, 5, 7, 9, 11, 13]  left=0, right=6
         L     M           R

Step 1:  mid=3, arr[3]=7 > 5  →  search left half
         [1, 3, 5] 7, 9, 11, 13  left=0, right=2
          L  M  R

Step 2:  mid=1, arr[1]=3 < 5  →  search right half  
         1 [3, 5] 7, 9, 11, 13  left=2, right=2
             L/M/R

Step 3:  mid=2, arr[2]=5 = 5  →  FOUND! Return index 2

Binary Search Template for "Find First Occurrence":
[1, 2, 2, 2, 3] find first 2

Step 1: mid=2, arr[2]=2 = target, but keep searching left
Step 2: right = mid - 1, continue until left > right
Result: First occurrence at index 1
```



#### C# Implementation
```csharp
using System;

public class BinarySearch 
{
    /// <summary>
    /// Standard binary search in sorted array
    /// Time: O(log n), Space: O(1)
    /// </summary>
    /// <param name="arr">Sorted array to search in</param>
    /// <param name="target">Value to find</param>
    /// <returns>Index of target, -1 if not found</returns>
    public static int Search(int[] arr, int target) 
    {
        int left = 0, right = arr.Length - 1;  // Define search boundaries
        
        while (left <= right)  // Continue while valid search space exists
        {
            // Calculate middle index (avoids overflow compared to (left+right)/2)
            int mid = left + (right - left) / 2;
            
            if (arr[mid] == target)
                return mid;           // Found target at middle position
            else if (arr[mid] < target)
                left = mid + 1;       // Target is in right half, eliminate left half
            else
                right = mid - 1;      // Target is in left half, eliminate right half
        }
        
        return -1;  // Target not found in array
    }
    
    /// <summary>
    /// Find first occurrence of target in sorted array with duplicates
    /// Time: O(log n), Space: O(1)
    /// </summary>
    /// <param name="arr">Sorted array (may contain duplicates)</param>
    /// <param name="target">Value to find first occurrence of</param>
    /// <returns>Index of first occurrence, -1 if not found</returns>
    public static int FindFirstOccurrence(int[] arr, int target) 
    {
        int left = 0, right = arr.Length - 1;
        int result = -1;  // Store the leftmost occurrence found
        
        while (left <= right) 
        {
            int mid = left + (right - left) / 2;
            
            if (arr[mid] == target) 
            {
                result = mid;         // Found an occurrence, but continue searching left
                right = mid - 1;      // Continue searching in left half for earlier occurrence
            }
            else if (arr[mid] < target)
                left = mid + 1;       // Target is in right half
            else
                right = mid - 1;      // Target is in left half
        }
        
        return result;  // Return leftmost occurrence (or -1 if not found)
    }
    
    /// <summary>
    /// Search in rotated sorted array
    /// Time: O(log n), Space: O(1)
    /// </summary>
    /// <param name="arr">Rotated sorted array</param>
    /// <param name="target">Value to search for</param>
    /// <returns>Index of target, -1 if not found</returns>
    public static int SearchRotatedArray(int[] arr, int target) 
    {
        int left = 0, right = arr.Length - 1;
        
        while (left <= right) 
        {
            int mid = left + (right - left) / 2;
            
            if (arr[mid] == target)
                return mid;  // Found target
            
            // Determine which half is properly sorted
            if (arr[left] <= arr[mid])  // Left half is sorted
            {
                // Check if target is in the sorted left half
                if (arr[left] <= target && target < arr[mid])
                    right = mid - 1;    // Search in left half
                else
                    left = mid + 1;     // Search in right half
            }
            else  // Right half is sorted (arr[mid] < arr[right])
            {
                // Check if target is in the sorted right half  
                if (arr[mid] < target && target <= arr[right])
                    left = mid + 1;     // Search in right half
                else
                    right = mid - 1;    // Search in left half
            }
        }
        
        return -1;  // Target not found
    }
    
    /// <summary>
    /// Find peak element in array (element greater than its neighbors)
    /// Time: O(log n), Space: O(1)
    /// </summary>
    /// <param name="arr">Array to search in</param>
    /// <returns>Index of any peak element</returns>
    public static int FindPeakElement(int[] arr) 
    {
        int left = 0, right = arr.Length - 1;
        
        while (left < right) 
        {
            int mid = left + (right - left) / 2;
            
            // Compare middle element with its right neighbor
            if (arr[mid] > arr[mid + 1])
                right = mid;        // Peak is in left half (including mid)
            else
                left = mid + 1;     // Peak is in right half (excluding mid)
        }
        
        return left;  // left == right, pointing to peak element
    }
    
    /// <summary>
    /// Square root using binary search (integer part only)
    /// Time: O(log n), Space: O(1)
    /// </summary>
    /// <param name="x">Number to find square root of</param>
    /// <returns>Integer part of square root</returns>
    public static int MySqrt(int x) 
    {
        if (x < 2) return x;  // Handle edge cases: 0 and 1
        
        int left = 1, right = x / 2;  // Search space: [1, x/2]
        
        while (left <= right) 
        {
            int mid = left + (right - left) / 2;
            long square = (long)mid * mid;  // Use long to prevent overflow
            
            if (square == x)
                return mid;           // Perfect square found
            else if (square < x)
                left = mid + 1;       // Need larger number
            else
                right = mid - 1;      // Need smaller number
        }
        
        return right;  // Return floor of square root
    }
}
            
            if (arr[left] <= arr[mid]) 
            {
                if (arr[left] <= target && target < arr[mid])
                    right = mid - 1;
                else
                    left = mid + 1;
            }
            else 
            {
                if (arr[mid] < target && target <= arr[right])
                    left = mid + 1;
                else
                    right = mid - 1;
            }
        }
        
        return -1;
    }
}
```

---

### 4. Kadane's Algorithm (Maximum Subarray)

**Use Cases:** Finding maximum sum subarray, maximum product subarray

**Algorithm Steps:**
1. **Initialize:** Set maxEndingHere and maxSoFar to first element
2. **Iterate:** For each element, decide to extend or start new subarray
3. **Choice:** Take max(current_element, current_element + maxEndingHere)
4. **Update:** Update global maximum if current subarray sum is better
5. **Continue:** Process all elements to find optimal subarray

**Process Visualization:**
```
Kadane's Algorithm on [-2, 1, -3, 4, -1, 2, 1, -5, 4]:

i=0: arr[0]=-2    maxEndingHere=-2,  maxSoFar=-2
i=1: arr[1]=1     maxEndingHere=1,   maxSoFar=1    (start new: 1 > -2+1)
i=2: arr[2]=-3    maxEndingHere=-2,  maxSoFar=1    (extend: -3+1=-2)
i=3: arr[3]=4     maxEndingHere=4,   maxSoFar=4    (start new: 4 > -2+4)  
i=4: arr[4]=-1    maxEndingHere=3,   maxSoFar=4    (extend: -1+4=3)
i=5: arr[5]=2     maxEndingHere=5,   maxSoFar=5    (extend: 2+3=5)
i=6: arr[6]=1     maxEndingHere=6,   maxSoFar=6    (extend: 1+5=6)
i=7: arr[7]=-5    maxEndingHere=1,   maxSoFar=6    (extend: -5+6=1)
i=8: arr[8]=4     maxEndingHere=5,   maxSoFar=6    (extend: 4+1=5)

Best subarray: [4, -1, 2, 1] with sum = 6

Key Insight: At each step, choose between:
- Starting fresh from current element: arr[i]
- Extending previous subarray: maxEndingHere + arr[i]
```



#### C# Implementation
```csharp
using System;

public class KadaneAlgorithm 
{
    /// <summary>
    /// Classic Kadane's algorithm to find maximum sum subarray
    /// Time: O(n), Space: O(1)
    /// </summary>
    /// <param name="arr">Input array of integers</param>
    /// <returns>Maximum sum of any contiguous subarray</returns>
    public static int MaxSubarraySum(int[] arr) 
    {
        if (arr.Length == 0) return 0;
        
        // maxEndingHere: maximum sum ending at current position
        // maxSoFar: global maximum sum found so far
        int maxEndingHere = arr[0];
        int maxSoFar = arr[0];
        
        for (int i = 1; i < arr.Length; i++) 
        {
            // Key decision: start new subarray or extend current one
            // Take maximum of: current element alone vs current + previous sum
            maxEndingHere = Math.Max(arr[i], maxEndingHere + arr[i]);
            
            // Update global maximum if current subarray is better
            maxSoFar = Math.Max(maxSoFar, maxEndingHere);
        }
        
        return maxSoFar;
    }
    
    /// <summary>
    /// Enhanced Kadane's: returns sum and indices of optimal subarray
    /// Time: O(n), Space: O(1)
    /// </summary>
    /// <param name="arr">Input array</param>
    /// <returns>Tuple of (max_sum, start_index, end_index)</returns>
    public static (int sum, int start, int end) MaxSubarrayWithIndices(int[] arr) 
    {
        if (arr.Length == 0) return (0, -1, -1);
        
        int maxEndingHere = arr[0];
        int maxSoFar = arr[0];
        int start = 0, end = 0, tempStart = 0;  // Track subarray boundaries
        
        for (int i = 1; i < arr.Length; i++) 
        {
            // If starting fresh gives better result than extending
            if (arr[i] > maxEndingHere + arr[i]) 
            {
                maxEndingHere = arr[i];
                tempStart = i;        // New subarray starts here
            }
            else 
            {
                maxEndingHere = maxEndingHere + arr[i];  // Extend current subarray
            }
            
            // Update global maximum and finalize subarray boundaries
            if (maxEndingHere > maxSoFar) 
            {
                maxSoFar = maxEndingHere;
                start = tempStart;    // Set final start index
                end = i;              // Set final end index
            }
        }
        
        return (maxSoFar, start, end);
    }
    
    /// <summary>
    /// Maximum product subarray (handles negative numbers differently)
    /// Time: O(n), Space: O(1)
    /// </summary>
    /// <param name="arr">Input array</param>
    /// <returns>Maximum product of any contiguous subarray</returns>
    public static int MaxProductSubarray(int[] arr) 
    {
        if (arr.Length == 0) return 0;
        
        // Track both maximum and minimum products (for negative numbers)
        int maxProd = arr[0];    // Maximum product ending here
        int minProd = arr[0];    // Minimum product ending here (can become max if next is negative)
        int result = arr[0];     // Global maximum product
        
        for (int i = 1; i < arr.Length; i++) 
        {
            // If current number is negative, swap max and min
            // (negative * max_positive = min_negative, negative * min_negative = max_positive)
            if (arr[i] < 0) 
            {
                (maxProd, minProd) = (minProd, maxProd);
            }
            
            // Calculate new maximum and minimum products
            maxProd = Math.Max(arr[i], maxProd * arr[i]);  // Start fresh or extend
            minProd = Math.Min(arr[i], minProd * arr[i]);  // Track minimum for future negatives
            
            // Update global maximum
            result = Math.Max(result, maxProd);
        }
        
        return result;
    }
    
    /// <summary>
    /// Circular array maximum sum subarray (allows wraparound)
    /// Time: O(n), Space: O(1)
    /// </summary>
    /// <param name="arr">Input circular array</param>
    /// <returns>Maximum sum considering circular nature</returns>
    public static int MaxSubarrayCircular(int[] arr) 
    {
        if (arr.Length == 0) return 0;
        
        // Case 1: Maximum subarray is non-circular (standard Kadane's)
        int maxKadane = MaxSubarraySum(arr);
        
        // Case 2: Maximum subarray is circular
        // This equals: total_sum - minimum_subarray_sum
        int totalSum = 0;
        for (int i = 0; i < arr.Length; i++) 
        {
            totalSum += arr[i];
            arr[i] = -arr[i];  // Negate for minimum subarray calculation
        }
        
        int maxCircular = totalSum + MaxSubarraySum(arr);  // Add because we negated
        
        // Restore original array
        for (int i = 0; i < arr.Length; i++) 
        {
            arr[i] = -arr[i];
        }
        
        // Handle edge case: all numbers are negative
        return maxCircular == 0 ? maxKadane : Math.Max(maxKadane, maxCircular);
    }
}
                end = i;
            }
        }
        
        return (maxSoFar, start, end);
    }
    
    public static int MaxProductSubarray(int[] arr) 
    {
        if (arr.Length == 0) return 0;
        
        int maxProd = arr[0];
        int minProd = arr[0];
        int result = arr[0];
        
        for (int i = 1; i < arr.Length; i++) 
        {
            if (arr[i] < 0) 
            {
                int temp = maxProd;
                maxProd = minProd;
                minProd = temp;
            }
            
            maxProd = Math.Max(arr[i], maxProd * arr[i]);
            minProd = Math.Min(arr[i], minProd * arr[i]);
            
            result = Math.Max(result, maxProd);
        }
        
        return result;
    }
}
```

---

### 5. Boyer-Moore Majority Element

**Use Cases:** Finding majority element, voting algorithms, stream processing

**Algorithm Steps:**
1. **Initialize:** Set candidate=null, count=0
2. **Voting Phase:** For each element, if count=0 set as candidate, else increment/decrement count
3. **Count Logic:** +1 if same as candidate, -1 if different
4. **Result:** After voting, candidate is the majority element (if it exists)
5. **Verify:** Optional verification phase to confirm majority

**Process Visualization:**
```
Boyer-Moore on [3, 2, 3, 1, 3]:

Step 1: 3  →  candidate=3, count=1    (first element becomes candidate)
Step 2: 2  →  candidate=3, count=0    (different element, decrement)
Step 3: 3  →  candidate=3, count=1    (same as candidate, increment)
Step 4: 1  →  candidate=3, count=0    (different element, decrement)  
Step 5: 3  →  candidate=3, count=1    (same as candidate, increment)

Final: candidate=3, count=1 > 0  →  3 is majority element

Intuition: Majority element appears more than n/2 times
- If we pair each majority element with a different element, 
  majority will still have elements left over
- Boyer-Moore simulates this pairing process with counter

Two Candidates (n/3 threshold):
[1, 1, 1, 2, 2, 3] - find elements appearing > n/3 times

At most 2 elements can appear more than n/3 times
Use two candidates and two counters simultaneously
```



#### C# Implementation
```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class BoyerMoore 
{
    /// <summary>
    /// Boyer-Moore algorithm to find majority element (appears > n/2 times)
    /// Time: O(n), Space: O(1)
    /// </summary>
    /// <param name="arr">Input array</param>
    /// <returns>Majority element if exists, null otherwise</returns>
    public static int? MajorityElement(int[] arr) 
    {
        int? candidate = null;  // Current majority candidate
        int count = 0;          // Vote count for current candidate
        
        // Phase 1: Voting - find potential majority candidate
        foreach (int num in arr) 
        {
            if (count == 0) 
            {
                candidate = num;    // New candidate when count reaches 0
                count = 1;
            }
            else if (candidate == num) 
            {
                count++;            // Vote for current candidate
            }
            else 
            {
                count--;            // Vote against current candidate
            }
        }
        
        // Phase 2: Verification - check if candidate is actually majority
        // (This phase is optional if problem guarantees majority exists)
        if (candidate.HasValue) 
        {
            int actualCount = arr.Count(x => x == candidate);
            return actualCount > arr.Length / 2 ? candidate : null;
        }
        
        return null;  // No majority element found
    }
    
    /// <summary>
    /// Find all elements that appear more than n/3 times (at most 2 such elements)
    /// Time: O(n), Space: O(1)
    /// </summary>
    /// <param name="arr">Input array</param>
    /// <returns>List of elements appearing more than n/3 times</returns>
    public static List<int> MajorityElementsThird(int[] arr) 
    {
        if (arr.Length <= 1) return arr.ToList();
        
        // At most 2 elements can appear more than n/3 times
        int? candidate1 = null, candidate2 = null;  // Two potential candidates
        int count1 = 0, count2 = 0;                 // Vote counts for each candidate
        
        // Phase 1: Voting with two candidates
        foreach (int num in arr) 
        {
            if (candidate1 == num) 
            {
                count1++;                    // Vote for candidate1
            }
            else if (candidate2 == num) 
            {
                count2++;                    // Vote for candidate2
            }
            else if (count1 == 0) 
            {
                candidate1 = num;            // New candidate1
                count1 = 1;
            }
            else if (count2 == 0) 
            {
                candidate2 = num;            // New candidate2
                count2 = 1;
            }
            else 
            {
                // Vote against both candidates
                count1--;
                count2--;
            }
        }
        
        // Phase 2: Verification - check which candidates actually exceed n/3
        var result = new List<int>();
        int threshold = arr.Length / 3;
        
        if (candidate1.HasValue && arr.Count(x => x == candidate1) > threshold) 
        {
            result.Add(candidate1.Value);
        }
        if (candidate2.HasValue && arr.Count(x => x == candidate2) > threshold) 
        {
            result.Add(candidate2.Value);
        }
        
        return result;
    }
    
    /// <summary>
    /// Find celebrity problem using Boyer-Moore approach
    /// Celebrity: known by everyone, knows nobody
    /// Time: O(n), Space: O(1)
    /// </summary>
    /// <param name="knows">2D array where knows[i][j] = true if person i knows person j</param>
    /// <returns>Index of celebrity, -1 if none exists</returns>
    public static int FindCelebrity(bool[,] knows) 
    {
        int n = knows.GetLength(0);
        int candidate = 0;  // Start with person 0 as potential celebrity
        
        // Phase 1: Find potential celebrity candidate
        // If candidate knows someone, that someone could be celebrity (not candidate)
        for (int i = 1; i < n; i++) 
        {
            if (knows[candidate, i]) 
            {
                candidate = i;      // Switch to person i as new candidate
            }
            // If candidate doesn't know i, then i cannot be celebrity
            // (celebrity should be known by candidate)
        }
        
        // Phase 2: Verify the candidate
        for (int i = 0; i < n; i++) 
        {
            if (i != candidate) 
            {
                // Celebrity should not know anyone AND everyone should know celebrity
                if (knows[candidate, i] || !knows[i, candidate]) 
                {
                    return -1;      // Not a valid celebrity
                }
            }
        }
        
        return candidate;           // Valid celebrity found
    }
    
    /// <summary>
    /// Water and Jug problem using Boyer-Moore-like approach
    /// Determine if you can measure exactly targetCapacity liters
    /// Time: O(log(min(jug1, jug2))), Space: O(1)
    /// </summary>
    /// <param name="jug1Capacity">Capacity of first jug</param>
    /// <param name="jug2Capacity">Capacity of second jug</param>
    /// <param name="targetCapacity">Target amount to measure</param>
    /// <returns>True if target can be measured</returns>
    public static bool CanMeasureWater(int jug1Capacity, int jug2Capacity, int targetCapacity) 
    {
        // Mathematical insight: can measure target if target is multiple of GCD(jug1, jug2)
        // and target doesn't exceed sum of both jugs
        
        if (targetCapacity > jug1Capacity + jug2Capacity) return false;
        if (targetCapacity == 0) return true;
        
        // Find GCD using Euclidean algorithm (similar to Boyer-Moore elimination principle)
        int gcd = FindGCD(jug1Capacity, jug2Capacity);
        return targetCapacity % gcd == 0;
    }
    
    /// <summary>
    /// Helper method to find Greatest Common Divisor
    /// </summary>
    private static int FindGCD(int a, int b) 
    {
        while (b != 0) 
        {
            int temp = b;
            b = a % b;      // Eliminate multiples, similar to Boyer-Moore elimination
            a = temp;
        }
        return a;
    }
}
        
        // Verification
        int actualCount = arr.Count(x => x == candidate);
        return actualCount > arr.Length / 2 ? candidate : null;
    }
    
    public static List<int> MajorityElementsThird(int[] arr) 
    {
        if (arr.Length <= 1) return arr.ToList();
        
        int? candidate1 = null, candidate2 = null;
        int count1 = 0, count2 = 0;
        
        foreach (int num in arr) 
        {
            if (candidate1 == num) 
            {
                count1++;
            }
            else if (candidate2 == num) 
            {
                count2++;
            }
            else if (count1 == 0) 
            {
                candidate1 = num;
                count1 = 1;
            }
            else if (count2 == 0) 
            {
                candidate2 = num;
                count2 = 1;
            }
            else 
            {
                count1--;
                count2--;
            }
        }
        
        var result = new List<int>();
        int threshold = arr.Length / 3;
        
        if (candidate1.HasValue && arr.Count(x => x == candidate1) > threshold)
            result.Add(candidate1.Value);
        if (candidate2.HasValue && arr.Count(x => x == candidate2) > threshold)
            result.Add(candidate2.Value);
        
        return result;
    }
    
    public static int FindCelebrity(bool[,] knows) 
    {
        int n = knows.GetLength(0);
        int candidate = 0;
        
        for (int i = 1; i < n; i++) 
        {
            if (knows[candidate, i]) 
            {
                candidate = i;
            }
        }
        
        for (int i = 0; i < n; i++) 
        {
            if (i != candidate) 
            {
                if (knows[candidate, i] || !knows[i, candidate]) 
                {
                    return -1;
                }
            }
        }
        
        return candidate;
    }
}
```

---

## 🎯 Common Patterns & Tips

### Pattern Recognition
- **Two Pointers:** Use when you need to find pairs or check from both ends
- **Sliding Window:** Use for subarray/substring problems with constraints
- **Binary Search:** Use when data is sorted or you're searching for boundaries
- **Kadane's:** Use for maximum/minimum subarray problems
- **Boyer-Moore:** Use for majority/voting problems

### Optimization Tips
1. **Avoid nested loops** when possible using two pointers or sliding window
2. **Use binary search** on sorted data instead of linear search
3. **Consider in-place algorithms** to reduce space complexity
4. **Cache frequently accessed data** in hash maps
5. **Use string builder** for multiple string concatenations

### Common Pitfalls
- **Off-by-one errors** in array indexing
- **Integer overflow** in sum calculations
- **Empty array edge cases**
- **String immutability** in repeated concatenations
- **Unicode handling** in string problems

---

## 📚 Related LeetCode Problems

### Easy
- [Two Sum](https://leetcode.com/problems/two-sum/)
- [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

### Medium
- [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
- [3Sum](https://leetcode.com/problems/3sum/)
- [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

### Hard
- [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
- [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
- [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

---

[← Back to Main Guide](./README.md)
