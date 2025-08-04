import time
import random
from typing import List


def benchmark_solutions():
    # Generate large test cases
    def generate_test_case(size):
        return [random.randint(-1000, 1000) for _ in range(size) if random.randint(-1000, 1000) != 0]
    
    test_sizes = [100, 1000, 5000]
    num_trials = 100
    
    for size in test_sizes:
        print(f"\n{'='*50}")
        print(f"Benchmarking with {size} asteroids, {num_trials} trials")
        print(f"{'='*50}")
        
        # Generate test cases
        test_cases = [generate_test_case(size) for _ in range(num_trials)]
        
        # Test original solution
        start_time = time.time()
        solution1 = Solution()
        for test in test_cases:
            solution1.asteroidCollision(test.copy())
        time1 = time.time() - start_time
        
        # Test optimized solution
        start_time = time.time()
        solution2 = SolutionOptimized2()
        for test in test_cases:
            solution2.asteroidCollision(test.copy())
        time2 = time.time() - start_time
        
        # Test space-optimized solution
        start_time = time.time()
        solution3 = SolutionSpaceOptimized()
        for test in test_cases:
            solution3.asteroidCollision(test.copy())
        time3 = time.time() - start_time
        
        print(f"Original Solution:      {time1:.4f}s")
        print(f"Optimized Solution:     {time2:.4f}s ({time2/time1:.2f}x)")
        print(f"Space Optimized:        {time3:.4f}s ({time3/time1:.2f}x)")


# Most optimized version for your use
class SolutionFinal:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                # Quick check: if no collisions possible, add directly
                if not stack or stack[-1] < 0:
                    stack.append(a)
                    continue
                
                # Handle collisions
                while stack and stack[-1] > 0:
                    if stack[-1] < -a:
                        stack.pop()
                    elif stack[-1] == -a:
                        stack.pop()
                        break
                    else:
                        # Left asteroid explodes
                        break
                else:
                    # No collision or all right asteroids destroyed
                    stack.append(a)
        
        return stack


if __name__ == "__main__":
    # Quick functionality test
    solution = SolutionFinal()
    print("Final optimized solution test:")
    test_cases = [
        [5, 10, -5],
        [8, -8], 
        [10, 2, -5],
        [-2, -1, 1, 2],
        [1, -2, -2, -2]
    ]
    
    for test in test_cases:
        result = solution.asteroidCollision(test)
        print(f"{test} -> {result}")
    
    # Uncomment to run benchmark (may take a moment)
    # benchmark_solutions()
