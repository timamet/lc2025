class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) <= 0 and s.strip() == "":
            return ""
        
        #split 
        words = s.split()
        print(words)

        result = []
        for word in words[::-1]:
            if len(result) > 0:
                result.append(" ")
            result += word
        return "".join(result)

result = Solution().reverseWords(' hello world  ')

print(result)