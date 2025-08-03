from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxArea = 0
        while left < right:
            left_height, right_height = height[left], height[right]
            maxArea = max(maxArea, (right - left) * min(left_height, right_height))
            
            if left_height < right_height:
                left += 1
            else:
                right -= 1
        return maxArea

# Test cases
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))  # Expected: 49
print(Solution().maxArea([1,1]))  # Expected: 1
print(Solution().maxArea([2,1]))  # Expected: 1
print(Solution().maxArea([1,2,1]))  # Expected: 2
print(Solution().maxArea([1,3,2,5,25,24,5]))  # Expected: 24