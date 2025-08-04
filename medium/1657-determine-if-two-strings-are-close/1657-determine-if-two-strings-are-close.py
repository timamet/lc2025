from typing import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n1 = len(word1)
        n2 = len(word2)

        if n1 != n2:
            return False

        set1 = sorted(set(word1))
        set2 = sorted(set(word2))

        if set1 != set2:
            return False
        
        counter1 = Counter(word1) 
        counter2 = Counter(word2)

        values1 = sorted(counter1.values())
        values2 = sorted(counter2.values())

        if values1 != values2:
            return False
        
        return True


res = Solution().closeStrings("abc", "bca")
print(res)

res = Solution().closeStrings("a", "aa")
print(res)



res = Solution().closeStrings("cabbba", "abbccc")
print(res)