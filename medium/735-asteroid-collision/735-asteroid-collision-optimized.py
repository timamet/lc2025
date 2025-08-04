from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                # Optimization 1: Early termination if no right-moving asteroids
                if not stack or stack[-1] < 0:
                    stack.append(a)
                    continue
                    
                # Process collisions
                while stack and stack[-1] > 0:
                    if stack[-1] < -a:
                        stack.pop()
                        continue
                    elif stack[-1] == -a:
                        stack.pop()
                    break
                else:
                    stack.append(a)

        return stack


class SolutionOptimized2:
    """
    Alternative approach: Process in-place when possible
    """
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            alive = True
            
            # Only check collisions for left-moving asteroids
            while alive and asteroid < 0 and stack and stack[-1] > 0:
                # Collision occurs
                if stack[-1] < -asteroid:
                    stack.pop()  # Right asteroid explodes
                elif stack[-1] == -asteroid:
                    stack.pop()  # Both explode
                    alive = False
                else:
                    alive = False  # Left asteroid explodes
            
            if alive:
                stack.append(asteroid)
        
        return stack


class SolutionSpaceOptimized:
    """
    Memory optimization: Reuse input array when possible
    Note: This modifies the input array
    """
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        write_idx = 0
        
        for asteroid in asteroids:
            # Check for collisions with previously placed asteroids
            while (write_idx > 0 and 
                   asteroids[write_idx - 1] > 0 and 
                   asteroid < 0):
                
                top = asteroids[write_idx - 1]
                if top < -asteroid:
                    write_idx -= 1  # Right asteroid explodes
                elif top == -asteroid:
                    write_idx -= 1  # Both explode
                    asteroid = 0   # Mark as exploded
                    break
                else:
                    asteroid = 0   # Left asteroid explodes
                    break
            
            if asteroid != 0:  # If asteroid survived
                asteroids[write_idx] = asteroid
                write_idx += 1
        
        return asteroids[:write_idx]


# Performance comparison
def test_solutions():
    test_cases = [
        [5, 10, -5],
        [8, -8],
        [10, 2, -5],
        [-2, -1, 1, 2],
        [1, -2, -2, -2],
        [1, 2, 3, -4],
        [-1, -2, 1, 2],
        [1, -1, -2, -2]
    ]
    
    solutions = [
        ("Original", Solution()),
        ("Optimized", SolutionOptimized2()),
        ("Space Optimized", SolutionSpaceOptimized())
    ]
    
    for name, solution in solutions:
        print(f"\n{name} Solution:")
        for test in test_cases:
            # Make copy for space-optimized version since it modifies input
            test_copy = test.copy()
            result = solution.asteroidCollision(test_copy)
            print(f"  {test} -> {result}")


if __name__ == "__main__":
    test_solutions()
