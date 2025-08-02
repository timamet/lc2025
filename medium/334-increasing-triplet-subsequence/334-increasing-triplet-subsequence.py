from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        numLength = len(nums)

        if numLength < 3:
            return False
        first_min  = float('inf')-1
        second_min = float('inf')

        for num in nums:
            if num <= first_min:
                first_min = num
            elif num <= second_min:
                second_min = num
            else:
                return True
        return False
            




# input = [1,2,3,4,5]
# result = Solution().increasingTriplet(input)
# print(f"Input: nums = '{input}'")
# print(result)



# input = [5,4,3,2,1]
# result = Solution().increasingTriplet(input)
# print(f"Input: nums = '{input}'")
# print(result)


input = [2,1,5,0,4,6]
result = Solution().increasingTriplet(input)
print(f"Input: nums = '{input}'")
print(result)