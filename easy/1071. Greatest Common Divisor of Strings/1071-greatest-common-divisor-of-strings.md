# 1071. Greatest Common Divisor of Strings

## Problem Statement

For two strings `s` and `t`, we say "`t` divides `s`" if and only if `s = t + t + t + ... + t + t` (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return the largest string `x` such that `x` divides both `str1` and `str2`.

## Examples

### Example 1:
- **Input**: `str1 = "ABCABC"`, `str2 = "ABC"`
- **Output**: `"ABC"`
- **Explanation**: `"ABC"` divides `"ABCABC"` (ABC + ABC) and divides `"ABC"` (ABC)

### Example 2:
- **Input**: `str1 = "ABABAB"`, `str2 = "ABAB"`
- **Output**: `"AB"`
- **Explanation**: `"AB"` divides `"ABABAB"` (AB + AB + AB) and divides `"ABAB"` (AB + AB)

### Example 3:
- **Input**: `str1 = "LEET"`, `str2 = "CODE"`
- **Output**: `""`
- **Explanation**: No common divisor exists

## Constraints

- `1 <= str1.length, str2.length <= 1000`
- `str1` and `str2` consist of English uppercase letters

## Solution Approaches

### Approach 1: Brute Force (Easier to Understand)

The simplest approach is to try all possible divisor lengths from the largest to smallest and check if they actually divide both strings.

#### Algorithm Steps
1. Start with the minimum length of both strings as the maximum possible divisor length
2. For each possible length `i` from max to 1:
   - Take the first `i` characters as a candidate divisor
   - Check if this candidate can divide both strings
3. Return the first valid divisor found, or empty string if none exists

#### Code Implementation (Brute Force)
```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def divides(s, t):
            """Check if string t divides string s"""
            if len(s) % len(t) != 0:
                return False
            return s == t * (len(s) // len(t))
        
        # Try all possible divisor lengths from largest to smallest
        for i in range(min(len(str1), len(str2)), 0, -1):
            candidate = str1[:i]
            if divides(str1, candidate) and divides(str2, candidate):
                return candidate
        
        return ""
```

**Time Complexity**: O(min(m,n) * (m+n)) - we try min(m,n) candidates and each check takes O(m+n)
**Space Complexity**: O(min(m,n)) - for storing candidates

### Approach 2: Optimized Mathematical Solution

This approach uses a key mathematical insight to solve the problem more efficiently.

#### Key Insight
**If there exists a common divisor string, then `str1 + str2` must equal `str2 + str1`**.

#### Why This Works
1. If string `x` divides both `str1` and `str2`, then:
   - `str1 = x + x + ... + x` (repeated `a` times)
   - `str2 = x + x + ... + x` (repeated `b` times)

2. Therefore:
   - `str1 + str2 = x*(a+b)`
   - `str2 + str1 = x*(b+a)`
   - Since addition is commutative: `str1 + str2 = str2 + str1`

3. If no common divisor exists, the concatenations will be different.

#### Algorithm Steps
1. **Check if concatenations are equal**: If `str1 + str2 != str2 + str1`, return empty string
2. **Find GCD of lengths**: Use Euclidean algorithm to find GCD of string lengths
3. **Return the prefix**: The answer is `str1[:gcd_length]`

## Code Implementation (Optimized)

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Find the largest string x such that x divides both str1 and str2.
        
        Key insight: If there's a common divisor, then str1 + str2 == str2 + str1
        The GCD length will be the GCD of the lengths of both strings.
        """
        # If str1 + str2 != str2 + str1, there's no common divisor
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find GCD of the lengths using Euclidean algorithm
        a, b = len(str1), len(str2)
        while b:
            a, b = b, a % b
        gcd_length = a
        
        # Return the prefix of length gcd_length
        return str1[:gcd_length]
```

**Time Complexity**: O(m + n) where m and n are the lengths of str1 and str2
**Space Complexity**: O(m + n) for the concatenated strings

## Comparison of Approaches

| Aspect | Brute Force | Optimized |
|--------|-------------|-----------|
| **Difficulty** | Easier to understand | Requires mathematical insight |
| **Time Complexity** | O(min(m,n) * (m+n)) | O(m + n) |
| **Space Complexity** | O(min(m,n)) | O(m + n) |
| **Interview Approach** | Good starting point | Impressive optimization |

### When to Use Each Approach

1. **Brute Force**: 
   - When you need to explain the problem clearly
   - As a starting point in interviews
   - When the constraints are small

2. **Optimized**:
   - When performance matters
   - To demonstrate mathematical problem-solving skills
   - For production code

## Time and Space Complexity

### Brute Force Approach
- **Time Complexity**: O(min(m,n) * (m+n))
  - We try min(m,n) possible divisor lengths
  - Each divisibility check takes O(m+n) time
- **Space Complexity**: O(min(m,n)) for storing candidate strings

### Optimized Approach  
- **Time Complexity**: O(m + n)
  - String concatenation: O(m + n)
  - GCD calculation: O(log(min(m, n)))
  - Overall: O(m + n)
- **Space Complexity**: O(m + n) for the concatenated strings

## Test Cases

### Test Case 1
```
Input: str1 = "ABCABC", str2 = "ABC"
Expected Output: "ABC"
```

### Test Case 2
```
Input: str1 = "ABABAB", str2 = "ABAB"
Expected Output: "AB"
```

### Test Case 3
```
Input: str1 = "LEET", str2 = "CODE"
Expected Output: ""
```

## Edge Cases

1. **One string is empty**: Not possible due to constraints
2. **Strings are identical**: GCD is the string itself
3. **No common divisor**: Return empty string
4. **One string is a prefix of another**: Common divisor exists

## Alternative Approaches

### Recursive Approach
```python
def gcdOfStrings(self, str1: str, str2: str) -> str:
    # Base case: if one string is empty, return the other
    if len(str1) == len(str2):
        return str1 if str1 == str2 else ""
    
    # Make sure str1 is the longer string
    if len(str1) < len(str2):
        str1, str2 = str2, str1
    
    # If str1 doesn't start with str2, no common divisor
    if not str1.startswith(str2):
        return ""
    
    # Recursively find GCD of str1[len(str2):] and str2
    return self.gcdOfStrings(str1[len(str2):], str2)
```

**Time Complexity**: O(m + n)
**Space Complexity**: O(m + n) due to recursion stack

### Interview Strategy

1. **Start with Brute Force**: Demonstrate understanding of the problem
2. **Optimize with Mathematical Insight**: Show problem-solving skills
3. **Discuss Trade-offs**: Compare time/space complexity
4. **Consider Edge Cases**: Empty strings, identical strings, no common divisor

## Why the Optimal Solution Works

The mathematical insight that `str1 + str2 == str2 + str1` if and only if they have a common divisor is based on the property that if two strings have a common period, their concatenations in any order will be identical.

This approach is elegant because it:
1. Quickly eliminates impossible cases
2. Uses mathematical properties to find the answer directly
3. Avoids the need to test multiple candidates

## Related Problems

- **28. Implement strStr()**: String pattern matching
- **459. Repeated Substring Pattern**: Check if string is made of repeated pattern
- **1169. Invalid Transactions**: String processing with constraints
