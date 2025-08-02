from typing import List


class Solution:
    
    def updateOutputAndReturnNextGroupIndex(self, chars: List[str], left: int, nextGroupIndex :int, groupSize: int) -> int:
        chars[nextGroupIndex] = chars[left]
        if groupSize > 1:
            groupSizeString = str(groupSize)
            for c in groupSizeString:
                nextGroupIndex += 1
                chars[nextGroupIndex] = c

        return nextGroupIndex + 1
    
    def compress(self, chars: List[str]) -> int:
        print(chars)

        charSize = len(chars)

        if charSize == 1: 
            return 1
        
        groupSize = 0

        left, right = 0,0
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
        print(chars)

        return nextGroupIndex


#Solution().compress(['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','b','b','b'])
#Solution().compress([''])
#Solution().compress(['a'])
Solution().compress(["a","a","b","b","c","c","c"])
        