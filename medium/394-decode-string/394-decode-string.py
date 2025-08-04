"""
394. Decode String
Medium

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Constraints:
- 1 <= s.length <= 30
- s consists of lowercase English letters, digits, and square brackets '[]'.
- s is guaranteed to be a valid input.
- All the integers in s are in the range [1, 300].

Time Complexity: O(n * m) where n is input length, m is max repetition factor
Space Complexity: O(n * m) for stacks and result string
"""

class Solution:
    def decodeString(self, s: str) -> str:
        # Two stacks: one for numbers, one for strings
        num_stack = []
        str_stack = []
        
        # Current number and current string being built
        current_num = 0
        current_str = ""
        
        for char in s:
            if char.isdigit():
                # Build the number (handle multi-digit numbers)
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push current state to stacks and reset
                num_stack.append(current_num)
                str_stack.append(current_str)
                current_num = 0
                current_str = ""
            elif char == ']':
                # Pop from stacks and repeat current string
                repeat_count = num_stack.pop()
                prev_str = str_stack.pop()
                current_str = prev_str + current_str * repeat_count
            else:
                # Regular character, add to current string
                current_str += char
        
        return current_str


# Test cases
def test_decode_string():
    sol = Solution()
    
    # Test case 1
    assert sol.decodeString("3[a]2[bc]") == "aaabcbc"
    print("Test 1 passed: 3[a]2[bc] -> aaabcbc")
    
    # Test case 2
    assert sol.decodeString("3[a2[c]]") == "accaccacc"
    print("Test 2 passed: 3[a2[c]] -> accaccacc")
    
    # Test case 3
    assert sol.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
    print("Test 3 passed: 2[abc]3[cd]ef -> abcabccdcdcdef")
    
    # Additional test cases
    assert sol.decodeString("abc") == "abc"
    print("Test 4 passed: abc -> abc (no brackets)")
    
    assert sol.decodeString("2[3[a]]") == "aaaaaa"
    print("Test 5 passed: 2[3[a]] -> aaaaaa")
    
    assert sol.decodeString("100[a]") == "a" * 100
    print("Test 6 passed: 100[a] -> 100 a's")
    
    print("All tests passed!")


if __name__ == "__main__":
    test_decode_string()
