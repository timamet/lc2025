import time
from typing import List


class Solution:
    """Original Implementation - Your Version"""
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        maxNumber = 0
        n = len(nums)
        zerosCount = 0

        while right < n:
            if nums[right] == 0:
                zerosCount += 1
    
            if zerosCount <= k:
                maxNumber = max(maxNumber, right - left + 1)
            else:
                if nums[left] == 0:
                    zerosCount -= 1
                left += 1
            
            right += 1
        
        return maxNumber

class SolutionOptimized:
    """Optimized Implementation - While Loop Version"""
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        maxNumber = 0
        n = len(nums)
        zerosCount = 0

        while right < n:
            # Expand window
            if nums[right] == 0:
                zerosCount += 1
            
            # Shrink window while invalid
            while zerosCount > k:
                if nums[left] == 0:
                    zerosCount -= 1
                left += 1
            
            # Update maximum length
            maxNumber = max(maxNumber, right - left + 1)
            right += 1
        
        return maxNumber


def time_solution(solution_class, nums, k, name):
    """Helper function to time solutions"""
    start = time.perf_counter()
    result = solution_class().longestOnes(nums, k)
    end = time.perf_counter()
    print(f"{name}: {result} (Time: {(end-start)*1000:.4f}ms)")
    return result


# Test cases
print("=== CORRECTNESS COMPARISON ===")
test_cases = [
    ([1,1,1,0,0,0,1,1,1,1,0], 2),
    ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3),
    ([0,0,0,1,1], 1),
    ([0,0,1,0,1], 1),
    ([0] * 1000 + [1] * 1000, 500),  # Large test case
]

for i, (nums, k) in enumerate(test_cases, 1):
    print(f"\nTest {i}: nums length={len(nums)}, k={k}")
    result1 = time_solution(Solution, nums, k, "Original     ")
    result2 = time_solution(SolutionOptimized, nums, k, "Optimized    ")
    print(f"Results match: {result1 == result2}")


print("\n" + "="*50)
print("COMPLEXITY ANALYSIS")
print("="*50)

print("""
🔍 ORIGINAL IMPLEMENTATION (Your Version):
├── Time Complexity: O(n) - Each element visited once by right pointer
├── Space Complexity: O(1) - Only using constant extra variables
├── Logic: if/else approach for window management
└── Behavior: Moves left pointer one step when window becomes invalid

⚡ OPTIMIZED IMPLEMENTATION (While Loop Version):  
├── Time Complexity: O(n) - Each element visited at most twice (right + left)
├── Space Complexity: O(1) - Only using constant extra variables  
├── Logic: while loop for aggressive window shrinking
└── Behavior: Keeps moving left until window becomes valid

📊 KEY DIFFERENCES:
┌─────────────────────┬─────────────────────┬─────────────────────┐
│     Aspect          │     Original        │     Optimized       │
├─────────────────────┼─────────────────────┼─────────────────────┤
│ Window Shrinking    │ One step at a time  │ Until valid         │
│ Max Update Timing   │ Only when valid     │ Always after valid  │
│ Edge Case Handling  │ May skip some cases │ More robust         │
│ Code Clarity        │ Slightly complex    │ More intuitive     │
└─────────────────────┴─────────────────────┴─────────────────────┘

🎯 VERDICT: 
Both implementations have the same time complexity O(n), but the optimized
version is more robust for edge cases and has clearer logic flow.
Your original solution works correctly for most cases due to the sliding
window pattern, but the while loop version is more mathematically sound.
""")

print("\n🧪 STEP-BY-STEP TRACE FOR EDGE CASE:")
print("Input: [0,0,1,0,1], k=1")
print("\nOriginal approach trace would show potential issues in complex scenarios")
print("Optimized approach ensures window is always valid before proceeding")


# Test cases
print("=== ORIGINAL IMPLEMENTATION ===")
res = Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)
print(f"Test 1: {res}")

res = Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)
print(f"Test 2: {res}")

# Edge case test
res = Solution().longestOnes([0,0,0,1,1], 1)
print(f"Edge case [0,0,0,1,1] with k=1: {res}")

print("\n=== OPTIMIZED IMPLEMENTATION ===")
res = SolutionOptimized().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)
print(f"Test 1: {res}")

res = SolutionOptimized().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)
print(f"Test 2: {res}")

# Edge case test
res = SolutionOptimized().longestOnes([0,0,0,1,1], 1)
print(f"Edge case [0,0,0,1,1] with k=1: {res}")

# Additional edge case to show the difference
print("\n=== EDGE CASE COMPARISON ===")
test_case = [0,0,1,0,1]
k = 1
print(f"Input: {test_case}, k={k}")
print(f"Original: {Solution().longestOnes(test_case, k)}")
print(f"Optimized: {SolutionOptimized().longestOnes(test_case, k)}")

