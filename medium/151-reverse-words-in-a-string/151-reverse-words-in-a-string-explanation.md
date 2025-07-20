# 151. Reverse Words in a String

## Problem Statement

Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

**Note:** `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

### Core Requirements

1. **Reverse word order** - Words should appear in opposite sequence
2. **Preserve word integrity** - Individual words remain spelled correctly
3. **Single space separation** - Words separated by exactly one space
4. **Remove extra spaces** - Eliminate leading, trailing, and multiple consecutive spaces
5. **Handle edge cases** - Empty strings, single words, all spaces

### Examples

```
Input: s = "the sky is blue"
Output: "blue is sky the"

Input: s = "  hello world  "
Output: "world hello"

Input: s = "a good   example"
Output: "example good a"
```

### Constraints
- `1 <= s.length <= 10^4`
- `s` contains English letters, digits, and spaces `' '`
- There is at least one word in `s`

---

## Solution Approaches

### Approach 1: Built-in String Methods (Simple)

**Algorithm:**
1. Use `split()` to automatically handle multiple spaces and create word list
2. Reverse the list using slicing `[::-1]`
3. Filter out empty strings and join with single spaces

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```python
def reverseWords(self, s: str) -> str:
    if len(s) <= 0 and s.strip() == "":
        return ""
    
    words = s.split(" ")
    result = ""
    
    for word in words[::-1]:
        if word != "":
            if len(result) > 0:
                result += " "
            result += word
    
    return result
```

**Pros:**
- Simple and readable
- Handles edge cases automatically
- Less error-prone

**Cons:**
- Uses additional space for word array
- Less control over the process

---

### Approach 2: In-Place Simulation (Advanced)

**Algorithm:**
1. Convert string to character array (simulate mutable string)
2. Remove extra spaces and normalize
3. Reverse the entire string
4. Reverse each individual word

**Time Complexity:** O(n)  
**Space Complexity:** O(1) extra space (if string were mutable)

```python
def reverseWordsInPlace(self, s: str) -> str:
    """
    In-place approach (simulated with char array since Python strings are immutable)
    Steps:
    1. Convert to char array
    2. Remove extra spaces
    3. Reverse entire string
    4. Reverse each word individually
    """
    # Convert to char array to simulate mutable string
    chars = list(s)
    
    # Step 1: Remove extra spaces and normalize
    chars = self._removeExtraSpaces(chars)
    
    # Step 2: Reverse the entire string
    self._reverse(chars, 0, len(chars) - 1)
    
    # Step 3: Reverse each word individually
    self._reverseEachWord(chars)
    
    return ''.join(chars)
```

#### Helper Functions

**1. Remove Extra Spaces**
```python
def _removeExtraSpaces(self, chars):
    """Remove leading, trailing, and extra spaces between words"""
    result = []
    i = 0
    n = len(chars)
    
    # Skip leading spaces
    while i < n and chars[i] == ' ':
        i += 1
    
    # Process characters
    while i < n:
        # Add non-space characters
        if chars[i] != ' ':
            result.append(chars[i])
        # Add single space for word separation
        elif result and result[-1] != ' ':
            result.append(' ')
        i += 1
    
    # Remove trailing space if exists
    if result and result[-1] == ' ':
        result.pop()
    
    return result
```

**2. Reverse Characters**
```python
def _reverse(self, chars, left, right):
    """Reverse characters in place between left and right indices"""
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
```

**3. Reverse Each Word**
```python
def _reverseEachWord(self, chars):
    """Reverse each word in the normalized string"""
    start = 0
    n = len(chars)
    
    for end in range(n + 1):
        # When we hit a space or end of string, reverse the current word
        if end == n or chars[end] == ' ':
            self._reverse(chars, start, end - 1)
            start = end + 1
```

---

## In-Place Algorithm Walkthrough

**Input:** `"  hello world  "`

### Step 1: Remove Extra Spaces
```
Original: [' ', ' ', 'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', ' ', ' ']
After:    ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
```

### Step 2: Reverse Entire String
```
Before: ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
After:  ['d', 'l', 'r', 'o', 'w', ' ', 'o', 'l', 'l', 'e', 'h']
```

### Step 3: Reverse Each Word
```
Word 1: ['d', 'l', 'r', 'o', 'w'] → ['w', 'o', 'r', 'l', 'd']
Word 2: ['o', 'l', 'l', 'e', 'h'] → ['h', 'e', 'l', 'l', 'o']
Final:  ['w', 'o', 'r', 'l', 'd', ' ', 'h', 'e', 'l', 'l', 'o']
```

**Result:** `"world hello"`

---

## Key Insights

### Why the "Reverse Twice" Technique Works

1. **First Reversal:** Gets words in the correct order but spelled backwards
2. **Second Reversal:** Fixes the spelling of each individual word

This is a classic technique used in many array/string manipulation problems.

### Edge Cases Handled

- **Leading spaces:** `"  hello world"`
- **Trailing spaces:** `"hello world  "`
- **Multiple spaces:** `"a  good   example"`
- **Single word:** `"hello"`

---

## Complexity Analysis

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Built-in Methods | O(n) | O(n) | Simple, readable |
| In-Place Simulation | O(n) | O(1)* | Memory efficient |

*O(1) extra space if string were truly mutable (like in C++)

---

## When to Use Each Approach

### Use Built-in Methods When:
- Code readability is prioritized
- Interview doesn't restrict built-in functions
- Prototype development

### Use In-Place When:
- Memory constraints are critical
- Interviewer asks for space optimization
- Demonstrating algorithm knowledge

---

## Alternative Approaches

### 3. Two-Pointer Approach
- Identify word boundaries manually
- Build result string in reverse order
- **Time:** O(n), **Space:** O(n)

### 4. Stack-Based Approach
- Push words onto stack
- Pop words to build result
- **Time:** O(n), **Space:** O(n)

### 5. Recursive Approach
- Recursively process each word
- Build result on return
- **Time:** O(n), **Space:** O(n) due to call stack

---

## Implementation Tips

1. **Handle Edge Cases First:** Empty strings, single words, all spaces
2. **Test Thoroughly:** Include various space configurations
3. **Consider Language Constraints:** Python strings are immutable
4. **Optimize Based on Requirements:** Choose approach based on space/time trade-offs

---

## Related Problems

- **186. Reverse Words in a String II** (mutable input)
- **557. Reverse Words in a String III** (reverse characters in each word)
- **344. Reverse String** (basic reversal)
- **151. Reverse Words in a String** (this problem)
