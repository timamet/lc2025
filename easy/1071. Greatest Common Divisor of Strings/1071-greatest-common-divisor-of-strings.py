class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Find the largest string x such that x divides both str1 and str2.
        
        Key insight: If there's a common divisor, then str1 + str2 == str2 + str1
        The GCD length will be the GCD of the lengths of both strings.
        """
        # If str1 + str2 != str2 + str1, there's no common divisor
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find GCD of the lengths using Euclidean algorithm
        a, b = len(str1), len(str2)
        while b:
            a, b = b, a % b
        gcd_length = a
        
        # Return the prefix of length gcd_length
        return str1[:gcd_length]

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
