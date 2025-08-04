class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "*":
                stack.append(c)
            elif stack:
                stack.pop()
        
        res = ''.join(stack)
        return res

res = Solution().removeStars("leet**cod*e")
print(res)

res = Solution().removeStars("erase*****")
print(res)