# 1768. Merge Strings Alternately

## Problem Statement
You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.

### Core Requirements

1. **Alternating merge** - Take characters from word1 and word2 in alternating order
2. **Start with word1** - First character should always come from word1
3. **Handle different lengths** - Append remaining characters from longer string
4. **Preserve order** - Maintain original character order within each string
5. **Complete merge** - Include all characters from both input strings

## Examples

### Example 1:
- **Input:** `word1 = "abc"`, `word2 = "pqr"`
- **Output:** `"apbqcr"`
- **Explanation:** Alternating merge: a-p-b-q-c-r

### Example 2:
- **Input:** `word1 = "ab"`, `word2 = "pqrs"`
- **Output:** `"apbqrs"`
- **Explanation:** After alternating, append remaining "rs" from word2

### Example 3:
- **Input:** `word1 = "abcd"`, `word2 = "pq"`
- **Output:** `"apbqcd"`
- **Explanation:** After alternating, append remaining "cd" from word1

## Solution Approach

### Algorithm:
1. Use a single pointer `i` to track current position in both strings
2. Alternate between characters from `word1` and `word2` while both have characters
3. Append remaining characters from the longer string

## Time Complexity Analysis

The time complexity is **O(m + n)** where:
- `m` = length of `word1`
- `n` = length of `word2`

### Breakdown:

1. **Phase 1 - Alternating merge:**
   ```python
   while (i < m and i < n):
       result.append(word1[i])
       result.append(word2[i])
       i += 1
   ```
   - Runs `min(m, n)` times
   - Each iteration does constant work O(1)
   - Total: O(min(m, n))

2. **Phase 2 - Remaining from word1:**
   ```python
   while i < m:
       result.append(word1[i])
       i += 1
   ```
   - Runs `max(0, m - min(m, n))` times
   - If `m > n`, runs `m - n` times
   - If `m ≤ n`, runs 0 times

3. **Phase 3 - Remaining from word2:**
   ```python
   while i < n:
       result.append(word2[i])
       i += 1
   ```
   - Runs `max(0, n - min(m, n))` times
   - If `n > m`, runs `n - m` times
   - If `n ≤ m`, runs 0 times

4. **Final join operation:**
   ```python
   return ''.join(result)
   ```
   - O(m + n) to join all characters

**Combined:** O(min(m, n)) + O(max(0, m - min(m, n))) + O(max(0, n - min(m, n))) + O(m + n)

This simplifies to **O(m + n)** because:
- We process each character from both strings exactly once
- The join operation processes all m + n characters once

### Space Complexity: O(m + n)
- For the result array that stores the merged string

## Python Implementation

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        print(f"word1: {word1}, word2: {word2}")

        # alternate between both strings
        i = 0
        
        m = len(word1)
        n = len(word2)

        result = [] 

        # Phase 1: Alternate characters while both strings have characters
        while (i < m and i < n):
            result.append(word1[i])
            result.append(word2[i])
            i += 1
        
        # Phase 2: Append remaining characters from word1 (if any)
        while i < m:
            result.append(word1[i])
            i += 1

        # Phase 3: Append remaining characters from word2 (if any)
        while i < n:
            result.append(word2[i])
            i += 1
        
        return ''.join(result)


# Test cases
result = Solution().mergeAlternately("abc", "pqr")
print(f"Result: {result}")

result = Solution().mergeAlternately("ab", "pqrs")
print(f"Result: {result}")

result = Solution().mergeAlternately("abcd", "pq")
print(f"Result: {result}")
```

## Key Points:
- **Single pointer approach:** Use one index `i` for both strings
- **List for efficiency:** Build result in a list, then join (more efficient than string concatenation)
- **Handle remainders:** Two separate loops handle leftover characters from either string
- **Edge cases:** Works correctly when strings have different lengths

## Alternative Approaches:

### Two-pointer approach:
```python
def mergeAlternately(self, word1: str, word2: str) -> str:
    result = []
    i, j = 0, 0
    
    while i < len(word1) and j < len(word2):
        result.append(word1[i])
        result.append(word2[j])
        i += 1
        j += 1
    
    result.extend(word1[i:])
    result.extend(word2[j:])
    
    return ''.join(result)
```

### Using itertools.zip_longest:
```python
from itertools import zip_longest

def mergeAlternately(self, word1: str, word2: str) -> str:
    result = []
    for c1, c2 in zip_longest(word1, word2, fillvalue=''):
        result.append(c1 + c2)
    return ''.join(result)
```

## Why O(m + n) is optimal:
- We must read every character from both input strings at least once
- We must write every character to the output string at least once
- Therefore, any correct solution must be at least O(m + n)
