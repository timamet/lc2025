from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                # Optimization: Early termination if no collisions possible
                if not stack or stack[-1] < 0:
                    stack.append(a)
                    continue
                
                # Handle collisions with right-moving asteroids
                while stack and stack[-1] > 0:
                    if stack[-1] < -a:
                        stack.pop()
                        continue
                    elif stack[-1] == -a:
                        stack.pop()
                    break
                else:
                    stack.append(a)

        return list(stack)

# Test the solution with the provided examples
solution = Solution()

# Example 1
# result1 = solution.asteroidCollision([5, 10, -5])
# print(f"Example 1: [5, 10, -5] -> {result1}")

# Example 2  
# result2 = solution.asteroidCollision([8, -8])
# print(f"Example 2: [8, -8] -> {result2}")

# # Example 3
# result3 = solution.asteroidCollision([10, 2, -5])
# print(f"Example 3: [10, 2, -5] -> {result3}")

# Additional test cases
result4 = solution.asteroidCollision([-2, -1, 1, 2])
print(f"Additional: [-2, -1, 1, 2] -> {result4}")

result5 = solution.asteroidCollision([1, -2, -2, -2])
print(f"Additional: [1, -2, -2, -2] -> {result5}")
