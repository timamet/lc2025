from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        maxNumber = 0
        k = 1
        n = len(nums)
        zerosCount = 0

        while right < n:
            if nums[right] == 0:
                zerosCount += 1
    
            if zerosCount <= k:
                maxNumber = max(maxNumber, right - left)
            else:
                if nums[left] == 0:
                    zerosCount -= 1
                left += 1
            
            right += 1
        
        return maxNumber
    

res = Solution().longestSubarray([1,1,0,1])
print(res)

res = Solution().longestSubarray([0,1,1,1,0,1,1,0,1])
print(res)

res = Solution().longestSubarray([1,1,1])
print(res)