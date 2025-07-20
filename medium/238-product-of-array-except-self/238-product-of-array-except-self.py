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


result = Solution().productExceptSelf([1,2,3,4])
print(result)