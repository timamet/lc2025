from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        Compress array of characters in-place using two pointers approach.
        
        Time Complexity: O(n) where n is length of chars
        Space Complexity: O(1) constant extra space
        """
        if not chars:
            return 0
        
        write = 0  # Position to write compressed result
        read = 0   # Position to read from original array
        
        while read < len(chars):
            # Current character and start of current group
            current_char = chars[read]
            group_start = read
            
            # Find end of current group of same characters
            while read < len(chars) and chars[read] == current_char:
                read += 1
            
            # Write the character
            chars[write] = current_char
            write += 1
            
            # Calculate group size
            group_size = read - group_start
            
            # If group size > 1, write the count
            if group_size > 1:
                # Convert count to string and write each digit
                count_str = str(group_size)
                for digit in count_str:
                    chars[write] = digit
                    write += 1
        
        return write


class SolutionAlternative:
    """Alternative implementation with slightly different approach"""
    
    def compress(self, chars: List[str]) -> int:
        write = 0
        i = 0
        
        while i < len(chars):
            current_char = chars[i]
            count = 1
            
            # Count consecutive occurrences
            while i + 1 < len(chars) and chars[i + 1] == current_char:
                count += 1
                i += 1
            
            # Write character
            chars[write] = current_char
            write += 1
            
            # Write count if > 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            
            i += 1
        
        return write


# Test cases
def test_solutions():
    test_cases = [
        (["a","a","b","b","c","c","c"], 6, ["a","2","b","2","c","3"]),
        (["a"], 1, ["a"]),
        (["a","b","b","b","b","b","b","b","b","b","b","b","b"], 4, ["a","b","1","2"]),
        (["a","a","a","a","a","a","a","a","a","a","a","a"], 3, ["a","1","2"]),
        (["a","b","c"], 3, ["a","b","c"]),
        ([], 0, []),
    ]
    
    solution = Solution()
    alt_solution = SolutionAlternative()
    
    print("Testing Solution:")
    for i, (chars, expected_length, expected_result) in enumerate(test_cases):
        chars_copy = chars.copy()
        result_length = solution.compress(chars_copy)
        actual_result = chars_copy[:result_length]
        
        print(f"Test {i+1}: {chars}")
        print(f"Expected: length={expected_length}, result={expected_result}")
        print(f"Actual:   length={result_length}, result={actual_result}")
        print(f"✅ Pass" if result_length == expected_length and actual_result == expected_result else "❌ Fail")
        print()
    
    print("\nTesting Alternative Solution:")
    for i, (chars, expected_length, expected_result) in enumerate(test_cases):
        chars_copy = chars.copy()
        result_length = alt_solution.compress(chars_copy)
        actual_result = chars_copy[:result_length]
        
        print(f"Test {i+1}: {chars}")
        print(f"Expected: length={expected_length}, result={expected_result}")
        print(f"Actual:   length={result_length}, result={actual_result}")
        print(f"✅ Pass" if result_length == expected_length and actual_result == expected_result else "❌ Fail")
        print()


if __name__ == "__main__":
    test_solutions()
