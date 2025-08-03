from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        left, right = 0, len(nums) - 1

        while left < right:
            leftNum = nums[left]
            rightNum = nums[right]
            pairSum  = leftNum + rightNum
            
            if pairSum < k:
                left += 1
            elif pairSum > k:
                right -= 1
            else:
                left += 1
                right -= 1
                res += 1
        
        return res

    def maxOperations2(self, nums: List[int], k: int) -> int:
        from collections import Counter
        count = Counter(nums)
        res = 0
        
        for num in count:
            complement = k - num
            if num == complement:  # Special case: same number twice
                res += count[num] // 2
            elif complement in count and num < complement:  # Avoid double counting
                res += min(count[num], count[complement])
        
        return res

# res = Solution().maxOperations([1,2,3,4], 5)
# print("Two Pointers [1,2,3,4], k=5:", res)

# res = Solution().maxOperations2([1,2,3,4], 5)
# print("Hash Set [1,2,3,4], k=5:", res)

# # Test the failing case
# res = Solution().maxOperations([2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], 3)
# print("Two Pointers failing case, k=3:", res)

res = Solution().maxOperations2([2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], 3)
print("Hash Set failing case, k=3:", res)