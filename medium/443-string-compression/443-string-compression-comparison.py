"""
Performance and Code Quality Comparison: Original vs Optimized

443. String Compression - Implementation Analysis
"""

from typing import List
import time
import sys


class OriginalSolution:
    """Your original implementation"""
    
    def updateOutputAndReturnNextGroupIndex(self, chars: List[str], left: int, nextGroupIndex: int, groupSize: int) -> int:
        chars[nextGroupIndex] = chars[left]
        if groupSize > 1:
            groupSizeString = str(groupSize)
            for c in groupSizeString:
                nextGroupIndex += 1
                chars[nextGroupIndex] = c
        return nextGroupIndex + 1
    
    def compress(self, chars: List[str]) -> int:
        charSize = len(chars)
        if charSize == 1: 
            return 1
        
        groupSize = 0
        left, right = 0, 0
        nextGroupIndex = 0
        
        while right < charSize:
            if chars[left] == chars[right]:
                groupSize += 1
                right += 1
            else:
                nextGroupIndex = self.updateOutputAndReturnNextGroupIndex(chars, left, nextGroupIndex, groupSize) 
                groupSize = 0
                left = right

        nextGroupIndex = self.updateOutputAndReturnNextGroupIndex(chars, left, nextGroupIndex, groupSize)
        # Note: This line doesn't actually modify the original array
        # chars = chars[:nextGroupIndex]  
        
        return nextGroupIndex  # Fixed: was len(chars)


class OptimizedSolution:
    """Optimized implementation"""
    
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        
        write = 0
        read = 0
        
        while read < len(chars):
            current_char = chars[read]
            group_start = read
            
            # Find end of current group
            while read < len(chars) and chars[read] == current_char:
                read += 1
            
            # Write character
            chars[write] = current_char
            write += 1
            
            # Write count if > 1
            group_size = read - group_start
            if group_size > 1:
                for digit in str(group_size):
                    chars[write] = digit
                    write += 1
        
        return write


def benchmark_solutions():
    """Compare performance of both solutions"""
    
    # Test cases of varying sizes
    test_cases = [
        # Small
        ["a", "a", "b", "b", "c", "c", "c"],
        # Medium
        ["a"] * 100 + ["b"] * 200 + ["c"] * 50,
        # Large with many groups
        (["a"] * 10 + ["b"] * 15 + ["c"] * 20) * 10,
        # Large single group
        ["x"] * 1000
    ]
    
    original = OriginalSolution()
    optimized = OptimizedSolution()
    
    print("Performance Comparison:")
    print("=" * 50)
    
    for i, test_case in enumerate(test_cases):
        print(f"\nTest Case {i+1}: {len(test_case)} characters")
        
        # Test original solution
        chars_copy = test_case.copy()
        start_time = time.perf_counter()
        original_result = original.compress(chars_copy)
        original_time = time.perf_counter() - start_time
        original_output = chars_copy[:original_result]
        
        # Test optimized solution
        chars_copy = test_case.copy()
        start_time = time.perf_counter()
        optimized_result = optimized.compress(chars_copy)
        optimized_time = time.perf_counter() - start_time
        optimized_output = chars_copy[:optimized_result]
        
        print(f"Original:  {original_time:.6f}s, result length: {original_result}")
        print(f"Optimized: {optimized_time:.6f}s, result length: {optimized_result}")
        print(f"Results match: {original_output == optimized_output}")
        
        if optimized_time > 0:
            speedup = original_time / optimized_time
            print(f"Speedup: {speedup:.2f}x")


def code_quality_analysis():
    """Analyze code quality differences"""
    
    print("\n" + "=" * 60)
    print("CODE QUALITY ANALYSIS")
    print("=" * 60)
    
    print("""
ORIGINAL IMPLEMENTATION:
+ ✅ Works correctly for basic cases
+ ✅ Uses in-place modification
- ❌ Helper method adds unnecessary complexity
- ❌ Variable names could be clearer (left, right, nextGroupIndex)
- ❌ Bug: chars = chars[:nextGroupIndex] doesn't modify original array
- ❌ Doesn't handle empty array edge case
- ❌ More complex control flow

OPTIMIZED IMPLEMENTATION:
+ ✅ Cleaner, more readable code
+ ✅ Better variable names (write, read, current_char)
+ ✅ Handles all edge cases including empty arrays
+ ✅ Single method - no unnecessary helper
+ ✅ More intuitive two-pointer approach
+ ✅ Proper in-place modification
+ ✅ Better comments and documentation

KEY IMPROVEMENTS:
1. Fixed the array modification bug
2. Simplified algorithm with clearer two-pointer approach
3. Better variable naming for readability
4. Added proper edge case handling
5. Removed unnecessary helper method
6. Added comprehensive test cases

COMPLEXITY ANALYSIS:
- Time Complexity: O(n) for both implementations
- Space Complexity: O(1) for both implementations
- Code Readability: Optimized version is significantly clearer
""")


if __name__ == "__main__":
    benchmark_solutions()
    code_quality_analysis()
