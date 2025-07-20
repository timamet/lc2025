# 238. Product of Array Except Self

## Problem Statement

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in **O(n) time** and **without using the division operation**.

## Examples

### Example 1:
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

### Example 2:
```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

## Constraints

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The input is generated such that `answer[i]` is guaranteed to fit in a 32-bit integer

## Follow-up
Can you solve the problem in **O(1) extra space complexity**? (The output array does not count as extra space for space complexity analysis.)

## Core Requirements

### 1. **Functional Requirements**
- **Input**: Integer array `nums` of length `n` (2 ≤ n ≤ 10^5)
- **Output**: Array `answer` where `answer[i]` = product of all elements except `nums[i]`
- **Element Range**: -30 ≤ nums[i] ≤ 30
- **Result Guarantee**: All products fit in 32-bit integers

### 2. **Performance Constraints**
- **Time Complexity**: Must be **O(n)** - linear time only
- **Space Complexity**: 
  - **Primary Goal**: Solve the problem (any reasonable space)
  - **Follow-up Goal**: **O(1) extra space** (output array doesn't count)

### 3. **Algorithm Restrictions**
- **Forbidden Operations**: Cannot use `/` or `//` operators
- **Special Considerations**: Cannot calculate total product and divide
- **Edge Case Handling**: Must work with zeros, negatives, minimum arrays

### 4. **Critical Edge Cases**
- **Single Zero**: `[1,0,3,4]` → `[0,12,0,0]` - Only the zero position gets a non-zero product
- **Multiple Zeros**: `[1,0,0,4]` → `[0,0,0,0]` - All products become 0
- **All Negatives**: `[-1,-2,-3]` → `[6,3,2]` - Signs are handled naturally by multiplication
- **Minimum Length**: `[2,3]` → `[3,2]` - Simplest case with two elements

### 5. **Success Criteria**
- ✅ Correct output for all test cases
- ✅ O(n) time complexity achieved
- ✅ No division operation used
- ✅ Handles all edge cases properly
- ✅ (Bonus) O(1) extra space complexity

### 6. **Pattern Recognition Requirements**
- **Identify**: This is a **Left-Right Product Accumulation** problem
- **Approach**: Two-pass algorithm (left products, then right products)
- **Key Insight**: `result[i] = left_product[i] × right_product[i]`

## Pattern Recognition

This problem follows the **Left-Right Product Accumulation** pattern:
- **Pattern Type**: Two-Pass Array Processing
- **Core Idea**: Combine products from left and right sides
- **Key Insight**: `result[i] = left_product[i] × right_product[i]`

## Solution Approach

### Algorithm: Two-Pass Left-Right Product

1. **Pass 1 (Left → Right)**: Calculate products of all elements to the left of each index
2. **Pass 2 (Right → Left)**: Calculate products of all elements to the right and multiply with left products

### Visual Walkthrough

For `nums = [1, 2, 3, 4]`:

```
Index:        0   1   2   3
Original:    [1,  2,  3,  4]

Pass 1 (Left products):
result[0] = 1           (no elements to the left)
result[1] = 1           (product of [1])
result[2] = 1 × 2 = 2   (product of [1, 2])
result[3] = 2 × 3 = 6   (product of [1, 2, 3])

After Pass 1: [1, 1, 2, 6]

Pass 2 (Right products):
right_product = 1
i=3: result[3] = 6 × 1 = 6,   right_product = 1 × 4 = 4
i=2: result[2] = 2 × 4 = 8,   right_product = 4 × 3 = 12
i=1: result[1] = 1 × 12 = 12, right_product = 12 × 2 = 24
i=0: result[0] = 1 × 24 = 24, right_product = 24 × 1 = 24

Final Result: [24, 12, 8, 6]
```

## Implementation

```python
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        
        # Fill result with left products
        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]
        
        # Multiply with right products in-place
        right_product = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result
```

## Complexity Analysis

### Time Complexity: O(n)
- **Pass 1**: O(n) - Single traversal left to right
- **Pass 2**: O(n) - Single traversal right to left
- **Total**: O(n)

### Space Complexity: O(1)
- Only using constant extra space (excluding output array)
- `right_product` variable: O(1)
- No additional arrays created

## Edge Cases

### 1. Single Zero
```python
Input: [1, 0, 3, 4]
Output: [0, 12, 0, 0]
```
- Only the zero position gets a non-zero product
- All other positions become 0 due to multiplication with zero

### 2. Multiple Zeros
```python
Input: [1, 0, 0, 4]
Output: [0, 0, 0, 0]
```
- All products become 0
- Multiple zeros ensure no position can have a non-zero product

### 3. Negative Numbers
```python
Input: [-1, 2, -3, 4]
Output: [-24, 12, -8, 6]
```
- Signs are handled naturally by multiplication
- Even number of negatives results in positive products

### 4. Minimum Length
```python
Input: [2, 3]
Output: [3, 2]
```
- Simplest case with two elements
- Each element is the product excluding the other

## Alternative Approaches

### Approach 1: Using Division (Not Allowed)
```python
# This violates the constraint - division operation forbidden
def productExceptSelf_division(self, nums):
    total_product = 1
    for num in nums:
        total_product *= num
    
    return [total_product // num for num in nums]  # Division not allowed!
```

### Approach 2: Brute Force O(n²)
```python
# This violates time complexity requirement - must be O(n)
def productExceptSelf_brute_force(self, nums):
    result = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        result.append(product)
    return result
```

### Approach 3: Two Separate Arrays O(n) Space
```python
# Uses extra space but clearer logic - doesn't meet follow-up requirement
def productExceptSelf_two_arrays(self, nums):
    n = len(nums)
    left = [1] * n
    right = [1] * n
    
    # Build left products
    for i in range(1, n):
        left[i] = left[i-1] * nums[i-1]
    
    # Build right products
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]
    
    # Combine results
    return [left[i] * right[i] for i in range(n)]
```

## Optimization Notes

1. **Space Optimization**: The optimal solution reuses the output array to store intermediate results
2. **Single Pass Optimization**: Cannot be done in a single pass due to the nature of the problem
3. **Zero Handling**: Could add special handling for zeros, but it doesn't improve asymptotic complexity

## Common Mistakes

1. **Using Division**: Violates problem constraints
2. **Not Handling Zeros**: Zeros require special consideration
3. **Off-by-One Errors**: Careful with array indices in both passes
4. **Forgetting Edge Cases**: Arrays with length 2, all zeros, etc.

## Related Problems

- **42. Trapping Rain Water** - Similar left-right pattern
- **121. Best Time to Buy and Sell Stock** - Prefix-suffix optimization
- **152. Maximum Product Subarray** - Product calculations
- **303. Range Sum Query - Immutable** - Prefix sum pattern

## Test Cases

```python
def test_solution():
    solution = Solution()
    
    # Basic test cases
    assert solution.productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert solution.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]
    
    # Edge cases
    assert solution.productExceptSelf([1,0]) == [0,1]
    assert solution.productExceptSelf([0,0]) == [0,0]
    assert solution.productExceptSelf([1,2]) == [2,1]
    assert solution.productExceptSelf([-1,-2,-3]) == [6,3,2]
    
    print("All test cases passed!")
```

## Key Takeaways

1. **Pattern Recognition**: Identify when you need information from both sides of each element
2. **Space Optimization**: Use the output array to store intermediate results
3. **Two-Pass Strategy**: Sometimes the optimal solution requires multiple passes
4. **Constraint Handling**: Division restriction forces creative solutions
5. **Edge Case Awareness**: Zeros and negative numbers need special consideration

This problem is an excellent example of how constraints (no division, O(1) space) can lead to elegant algorithmic solutions using the left-right accumulation pattern.
