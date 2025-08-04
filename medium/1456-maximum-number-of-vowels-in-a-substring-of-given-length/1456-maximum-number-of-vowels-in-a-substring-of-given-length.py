class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Count vowels in the first window
        current_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
        
        max_vowels = current_vowels
        
        # Slide the window: remove left character, add right character
        for i in range(k, len(s)):
            # Remove the leftmost character of previous window
            if s[i - k] in vowels:
                current_vowels -= 1
            
            # Add the new rightmost character
            if s[i] in vowels:
                current_vowels += 1
            
            # Update maximum
            max_vowels = max(max_vowels, current_vowels)
        
        return max_vowels


res = Solution().maxVowels("abciiidef", 3)
print(res)


res = Solution().maxVowels("aeiou", 2)
print(res)

res = Solution().maxVowels("leetcode", 3)
print(res)
