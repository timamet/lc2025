class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Find the largest string x such that x divides both str1 and str2.
        
        Brute Force Approach: Try all possible divisor lengths from largest to smallest
        and check if they actually divide both strings.
        """
        def divides(s, t):
            """Check if string t divides string s"""
            # If length of s is not divisible by length of t, t cannot divide s
            if len(s) % len(t) != 0:
                return False
            # Check if s equals t repeated (len(s) // len(t)) times
            return s == t * (len(s) // len(t))
        
        # Try all possible divisor lengths from largest to smallest
        for i in range(min(len(str1), len(str2)), 0, -1):
            candidate = str1[:i]  # Take first i characters as candidate divisor
            # Check if this candidate divides both strings
            if divides(str1, candidate) and divides(str2, candidate):
                return candidate
        
        # If no divisor found, return empty string
        return ""

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    str1 = "ABCABC"
    str2 = "ABC"
    result = solution.gcdOfStrings(str1, str2)
    print(f"Input: str1 = '{str1}', str2 = '{str2}'")
    print(f"Output: '{result}'")
    print()
    
    # Test case 2
    str1 = "ABABAB"
    str2 = "ABAB"
    result = solution.gcdOfStrings(str1, str2)
    print(f"Input: str1 = '{str1}', str2 = '{str2}'")
    print(f"Output: '{result}'")
    print()
    
    # Test case 3
    str1 = "LEET"
    str2 = "CODE"
    result = solution.gcdOfStrings(str1, str2)
    print(f"Input: str1 = '{str1}', str2 = '{str2}'")
    print(f"Output: '{result}'")
    print()
    
    # Additional test cases
    print("Additional Test Cases:")
    print("=" * 30)
    
    # Test case 4: Same strings
    str1 = "ABCABC"
    str2 = "ABCABC"
    result = solution.gcdOfStrings(str1, str2)
    print(f"Input: str1 = '{str1}', str2 = '{str2}'")
    print(f"Output: '{result}'")
    print()
    
    # Test case 5: One character strings
    str1 = "A"
    str2 = "AA"
    result = solution.gcdOfStrings(str1, str2)
    print(f"Input: str1 = '{str1}', str2 = '{str2}'")
    print(f"Output: '{result}'")
    print()
    
    # Test case 6: No common divisor
    str1 = "ABCD"
    str2 = "EFGH"
    result = solution.gcdOfStrings(str1, str2)
    print(f"Input: str1 = '{str1}', str2 = '{str2}'")
    print(f"Output: '{result}'")
    print()
