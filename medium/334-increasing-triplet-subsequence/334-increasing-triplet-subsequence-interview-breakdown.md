# 334. Increasing Triplet Subsequence - Interview Breakdown

## Problem Statement

Given an integer array `nums`, return `true` if there exists a triple of indices `(i, j, k)` such that `i < j < k` and `nums[i] < nums[j] < nums[k]`. If no such indices exist, return `false`.

## Examples

### Example 1:
```
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
```

### Example 2:
```
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
```

### Example 3:
```
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
```

## Constraints

- `1 <= nums.length <= 5 * 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

---

## 🎯 UMPIRE Interview Breakdown

### U - UNDERSTAND (2-3 minutes)

#### Key Clarifying Questions to Ask:
```
"Just to confirm - we need to find three indices where the values are strictly increasing, correct?"
"The indices themselves need to be in order (i < j < k), but the values can be anywhere in the array?"
"Should I return the indices themselves, or just true/false?"
"Can the array contain duplicates? How should equal values be handled?"
"What should I return for arrays with less than 3 elements?"
"Are there any memory constraints I should be aware of given the large input size?"
```

#### Problem Restatement:
```
"So I need to find if there exists a subsequence of exactly 3 elements where:
1. The indices are in ascending order (i < j < k)
2. The values are in strictly ascending order (nums[i] < nums[j] < nums[k])
3. I only need to return true if such a triplet exists, false otherwise"
```

#### Core Requirements:
- Find exactly 3 elements (not more, not less)
- Elements must be in strictly increasing order by value
- Indices must be in ascending order (maintain relative positions)
- Return boolean result
- Handle edge cases (arrays with < 3 elements)

---

### M - MATCH (1-2 minutes)

#### Problem Pattern Recognition:

**Primary Pattern: Array Traversal with State Tracking**
- This is NOT a typical two-pointer problem (array isn't sorted)
- This is NOT a sliding window (we're not looking for contiguous elements)
- This IS a subsequence problem with ordering constraints

**Similar Problems:**
- Longest Increasing Subsequence (but we only need length 3)
- Finding patterns in unsorted arrays
- Greedy algorithms for optimization

#### Potential Approaches:
1. **Brute Force:** Check all triplets O(n³)
2. **Optimized Traversal:** Track smallest and middle values as we go O(n)
3. **Dynamic Programming:** Overkill for this specific constraint

#### Why This Matches Greedy Pattern:
```
"Since we only need to find ONE valid triplet, we can greedily track:
- The smallest value seen so far (potential first element)
- The smallest value that can be the middle element
- Check if current value can be the third element"
```

#### 🎯 **The Greedy Strategy Explained:**

**Greedy Choice:** At each step, we make the locally optimal decision:
1. **Always keep the smallest possible `first` value** - This maximizes our chances of finding a valid triplet
2. **Always keep the smallest possible `second` value** (that's > first) - This maximizes our chances of finding a third element
3. **These local choices lead to the optimal global solution**

**Why Greedy Works Here:**
- We only need to find ONE valid triplet (not all triplets)
- Keeping smaller values earlier gives us more opportunities for the third element
- If a triplet exists, our greedy approach will find it

---

### P - PLAN (3-5 minutes)

#### Approach 1: Brute Force (Baseline)
```
Time Complexity: O(n³)
Space Complexity: O(1)

For each i:
    For each j > i:
        For each k > j:
            If nums[i] < nums[j] < nums[k]:
                return True
return False
```

**Analysis:** This will work for small inputs but will timeout for large inputs (5 * 10^5 elements).

#### Approach 2: Optimized Single Pass (Target Solution)
```
Time Complexity: O(n)
Space Complexity: O(1)

Key Insight: We can greedily track two values:
1. first_min: smallest value seen so far
2. second_min: smallest value that can serve as middle element

As we traverse:
- If current < first_min: update first_min
- Else if current < second_min: update second_min  
- Else if we have both first_min and second_min: return True
```

#### Detailed Algorithm Plan:
```
1. Initialize first_min = infinity, second_min = infinity
2. For each number in array:
   a. If number <= first_min:
      - Update first_min = number
   b. Else if number <= second_min:
      - Update second_min = number (we know number > first_min)
   c. Else:
      - We found our third element! Return True
3. If we finish the loop without returning, return False
```

#### Edge Cases to Consider:
- Array length < 3: return False
- All elements equal: return False
- Strictly decreasing array: return False
- Array with only 2 distinct values: depends on arrangement

#### Trace Through Example 3: [2,1,5,0,4,6]
```
i=0, num=2: first_min=2, second_min=inf
i=1, num=1: first_min=1, second_min=inf  
i=2, num=5: first_min=1, second_min=5
i=3, num=0: first_min=0, second_min=5
i=4, num=4: first_min=0, second_min=4
i=5, num=6: 6 > second_min=4 and 4 > first_min=0, return True
```

---

## 🧠 **Detailed Greedy Examples**

### **Example 1: [2,1,5,0,4,6] → True**

**Step-by-Step Greedy Decisions:**

```
Initial: first = ∞, second = ∞

Step 1: num = 2
- Is 2 <= first(∞)? YES → first = 2
- State: first = 2, second = ∞
- Greedy choice: "Keep smallest possible first value"

Step 2: num = 1  
- Is 1 <= first(2)? YES → first = 1
- State: first = 1, second = ∞
- Greedy choice: "Found even smaller first, take it!"

Step 3: num = 5
- Is 5 <= first(1)? NO
- Is 5 <= second(∞)? YES → second = 5
- State: first = 1, second = 5
- Greedy choice: "Keep smallest possible second value"

Step 4: num = 0
- Is 0 <= first(1)? YES → first = 0
- State: first = 0, second = 5
- Greedy choice: "Even smaller first! This gives us more options"

Step 5: num = 4
- Is 4 <= first(0)? NO
- Is 4 <= second(5)? YES → second = 4  
- State: first = 0, second = 4
- Greedy choice: "Smaller second is better!"

Step 6: num = 6
- Is 6 <= first(0)? NO
- Is 6 <= second(4)? NO
- We have first(0) < second(4) < current(6) → FOUND TRIPLET!
- Return True
```

**Key Insight:** Even though we "lost" the original triplet (2,5,6), our greedy choices led us to a better triplet (0,4,6)!

### **Example 2: [1,5,2,4,3] → True**

```
Initial: first = ∞, second = ∞

Step 1: num = 1 → first = 1, second = ∞
Step 2: num = 5 → first = 1, second = 5  
Step 3: num = 2 → first = 1, second = 2 (better second!)
Step 4: num = 4 → first = 1, second = 2, found 4 > 2 → TRUE!

Final triplet: (1, 2, 4) at indices (0, 2, 3)
```

### **Example 3: [5,4,3,2,1] → False**

```
Step 1: num = 5 → first = 5, second = ∞
Step 2: num = 4 → first = 4, second = ∞ (smaller first)
Step 3: num = 3 → first = 3, second = ∞ (smaller first)  
Step 4: num = 2 → first = 2, second = ∞ (smaller first)
Step 5: num = 1 → first = 1, second = ∞ (smaller first)

Never found a second element → FALSE
```

### **Example 4: [1,0,2,0,3] → True**

```
Step 1: num = 1 → first = 1, second = ∞
Step 2: num = 0 → first = 0, second = ∞ (better first!)
Step 3: num = 2 → first = 0, second = 2
Step 4: num = 0 → first = 0, second = 2 (0 <= 0, no change to first)
Step 5: num = 3 → 3 > second(2) → TRUE!

Final triplet: (0, 2, 3)
```

### **🤔 Why This Greedy Approach Works:**

**Proof Intuition:**
1. **Optimal Substructure:** If a triplet exists, there exists one where the first two elements are the smallest possible
2. **Greedy Choice Property:** Choosing the smallest `first` and `second` never eliminates a valid solution
3. **No Backtracking Needed:** Once we make a greedy choice, we never need to reconsider it

**The "Magic" Moment:**
- When `first` gets updated after `second` is already set, we might think we "lost" our second element
- But this is actually beneficial! A smaller `first` means our existing `second` is now valid with more potential third elements
- The algorithm maintains the invariant: "If a triplet exists starting from any previous position, our current state can still find it"

---

### I - IMPLEMENT (Would code here in actual interview)

#### Function Signature:
```python
def increasingTriplet(self, nums: List[int]) -> bool:
    # Implementation would go here
    pass
```

#### Key Implementation Notes:
- Use `float('inf')` for initial values
- Be careful with <= vs < comparisons
- The algorithm maintains the invariant that if second_min is set, first_min < second_min
- We don't need to track actual indices, just the values

---

### R - REVIEW (2-3 minutes)

#### Test Cases to Verify:

**Basic Cases:**
- `[1,2,3,4,5]` → True (any triplet works)
- `[5,4,3,2,1]` → False (strictly decreasing)
- `[2,1,5,0,4,6]` → True (triplet: 0,4,6)

**Edge Cases:**
- `[1,2]` → False (less than 3 elements)
- `[1]` → False (less than 3 elements)
- `[1,1,1,1]` → False (all equal)
- `[1,0,2,0,3]` → True (triplet: 0,2,3)

**Potential Gotchas:**
- Make sure algorithm works when first_min gets updated after second_min is set
- Verify it handles negative numbers correctly
- Check boundary values (-2³¹ and 2³¹-1)

---

### E - EVALUATE (1-2 minutes)

#### Complexity Analysis:
```
Time Complexity: O(n) - single pass through array
Space Complexity: O(1) - only using two variables

This is optimal since we must examine each element at least once.
```

#### Optimization Discussion:
```
"The optimized solution is already optimal for this problem. 
We achieve O(n) time with O(1) space, which is the best possible 
since we need to examine each element at least once."
```

#### Alternative Approaches:
```
"We could use dynamic programming to solve the more general 
'Longest Increasing Subsequence' problem, but that would be 
O(n log n) time and O(n) space - overkill for this specific case."
```

#### Follow-up Questions Ready:
- "What if we needed to return the actual indices?"
- "What if we needed to find all such triplets?"
- "What if we needed to find increasing subsequences of length k?"
- "How would you modify this for non-strictly increasing (allowing equals)?"

---

## 🎯 Interview Communication Points

### Key Things to Mention:
1. **Pattern Recognition:** "This is a greedy algorithm problem, not two-pointers"
2. **Optimization Insight:** "We can track just two values instead of checking all triplets"
3. **Invariant:** "first_min will always be ≤ second_min when both are set"
4. **Edge Cases:** "Need to handle arrays with less than 3 elements"
5. **Greedy Justification:** "We make locally optimal choices (smallest possible values) that guarantee finding a solution if one exists"

### Show Your Thinking:
- Start with brute force to show understanding
- Explain why O(n³) won't work for large inputs
- Walk through the greedy insight step by step
- **Emphasize the greedy property:** "By always keeping the smallest possible first and second values, we maximize our chances of finding a valid third element"
- Trace through examples to verify logic
- **Address the 'magic' moment:** "When first gets updated after second is set, explain why this doesn't break our solution"

### Time Management:
- Understand: 2-3 minutes (clarify the subsequence vs subarray distinction)
- Match: 1-2 minutes (identify as greedy/tracking problem)
- Plan: 3-4 minutes (work through brute force → optimized)
- Implement: 8-10 minutes (careful with edge cases)
- Review: 2-3 minutes (test with provided examples)
- Evaluate: 1-2 minutes (complexity analysis and alternatives)
