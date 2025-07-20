class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) <= 0 and s.strip() == "":
            return ""
        
        #split 
        words = s.split(" ")
        print(words)

        result = ""
        for word in words[::-1]:
            if (word != ""):
                if len(result) > 0:
                    result += " "
                result += word
        return result

    def reverseWordsInPlace(self, s: str) -> str:
        """
        In-place approach (simulated with char array since Python strings are immutable)
        Steps:
        1. Convert to char array
        2. Remove extra spaces
        3. Reverse entire string
        4. Reverse each word individually
        """
        # Convert to char array to simulate mutable string
        chars = list(s)
        
        # Step 1: Remove extra spaces and normalize
        chars = self._removeExtraSpaces(chars)
        
        # Step 2: Reverse the entire string
        self._reverse(chars, 0, len(chars) - 1)
        
        # Step 3: Reverse each word individually
        self._reverseEachWord(chars)
        
        return ''.join(chars)
    
    def _removeExtraSpaces(self, chars):
        """Remove leading, trailing, and extra spaces between words"""
        result = []
        i = 0
        n = len(chars)
        
        # Skip leading spaces
        while i < n and chars[i] == ' ':
            i += 1
        
        # Process characters
        while i < n:
            # Add non-space characters
            if chars[i] != ' ':
                result.append(chars[i])
            # Add single space for word separation
            elif result and result[-1] != ' ':
                result.append(' ')
            i += 1
        
        # Remove trailing space if exists
        if result and result[-1] == ' ':
            result.pop()
        
        return result
    
    def _reverse(self, chars, left, right):
        """Reverse characters in place between left and right indices"""
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
    
    def _reverseEachWord(self, chars):
        """Reverse each word in the normalized string"""
        start = 0
        n = len(chars)
        
        for end in range(n + 1):
            # When we hit a space or end of string, reverse the current word
            if end == n or chars[end] == ' ':
                self._reverse(chars, start, end - 1)
                start = end + 1

# Test both approaches
solution = Solution()

# Original approach
result1 = solution.reverseWords(' hello world  ')
print("Original approach:", result1)

# In-place approach (simulated)
result2 = solution.reverseWordsInPlace(' hello world  ')
print("In-place approach:", result2)

# Test with more examples
test_cases = [
    "the sky is blue",
    "  hello world  ",
    "a good   example",
    "  single  "
]

print("\nTesting both approaches:")
for test in test_cases:
    original = solution.reverseWords(test)
    in_place = solution.reverseWordsInPlace(test)
    print(f"Input: '{test}'")
    print(f"Original: '{original}'")
    print(f"In-place: '{in_place}'")
    print(f"Match: {original == in_place}")
    print("---")