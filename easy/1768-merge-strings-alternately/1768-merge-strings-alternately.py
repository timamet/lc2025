class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        print(f"word1: {word1}, word2: {word2}")

        # alternate between both strings
        i = 0
        
        m = len(word1)
        n = len(word2)

        result = [] 

        while (i<m and i<n):
            result.append(word1[i])
            result.append(word2[i])
            i += 1
        
        while i < m:
            result.append(word1[i])
            i += 1

        while i < n:
            result.append(word2[i])
            i += 1
        
        return ''.join(result)


result = Solution().mergeAlternately("abc", "pqr")
print(f"Result: {result}")

result = Solution().mergeAlternately("ab", "pqrs")
print(f"Result: {result}")

result = Solution().mergeAlternately("abcd", "pq")
print(f"Result: {result}")