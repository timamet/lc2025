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
        n = len(chars)

        if n <= 1: 
            return n
        
        left, right = 0,0
        write_pos = 0

        while right < n:
            if chars[left] == chars[right]:
                right += 1
            else:
                count = right - left
                write_pos = self.updateOutputAndReturnNextGroupIndex(chars, left, write_pos, count) 
                left = right

        count = right - left
        write_pos = self.updateOutputAndReturnNextGroupIndex(chars, left, write_pos, count)
        return write_pos


#Solution().compress(['a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','a','b','b','b'])
#Solution().compress([''])
#Solution().compress(['a'])
Solution().compress(["a","a","b","b","c","c","c"])
        