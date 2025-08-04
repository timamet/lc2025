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


class SolutionWithDebug:
    """Version with debug output to show when optimization triggers"""
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for i, a in enumerate(asteroids):
            print(f"\nStep {i+1}: Processing asteroid {a}")
            print(f"Current stack: {stack}")
            
            if a > 0:
                stack.append(a)
                print(f"→ Right-moving asteroid added. Stack: {stack}")
            else:
                # Check optimization conditions
                if not stack:
                    print("✅ OPTIMIZATION: Stack is empty - no collisions possible")
                    stack.append(a)
                    print(f"→ Left-moving asteroid added. Stack: {stack}")
                    continue
                elif stack[-1] < 0:
                    print(f"✅ OPTIMIZATION: Top of stack ({stack[-1]}) is left-moving - no collision")
                    stack.append(a)
                    print(f"→ Left-moving asteroid added. Stack: {stack}")
                    continue
                
                print(f"⚔️  COLLISION ZONE: Left asteroid {a} vs right asteroids in stack")
                # Handle collisions with right-moving asteroids
                while stack and stack[-1] > 0:
                    top = stack[-1]
                    print(f"   Collision: {top} (right) vs {a} (left)")
                    
                    if stack[-1] < -a:
                        popped = stack.pop()
                        print(f"   → Right asteroid {popped} explodes (smaller)")
                        continue
                    elif stack[-1] == -a:
                        popped = stack.pop()
                        print(f"   → Both asteroids explode (equal size: {popped} and {a})")
                        break
                    else:
                        print(f"   → Left asteroid {a} explodes (smaller)")
                        break
                else:
                    print(f"   → Left asteroid {a} survives all collisions")
                    stack.append(a)
                
                print(f"→ Final stack after processing: {stack}")

        return list(stack)


def demonstrate_optimization_cases():
    print("=" * 60)
    print("DEMONSTRATING WHEN THE OPTIMIZATION KICKS IN")
    print("=" * 60)
    
    test_cases = [
        # Case 1: Empty stack
        ([-5], "Empty stack - first left-moving asteroid"),
        
        # Case 2: All left-moving asteroids so far  
        ([-3, -2, -1], "All left-moving asteroids - no collisions possible"),
        
        # Case 3: Mixed with left-moving on top
        ([5, 3, -2, -1, -4], "Left-moving asteroid when stack top is also left-moving"),
        
        # Case 4: No optimization - collision occurs
        ([5, 3, -2], "Collision case - optimization doesn't apply"),
        
        # Case 5: Complex mixed case
        ([-1, -2, 5, 3, -4, -6], "Complex: some optimized, some collisions")
    ]
    
    solution = SolutionWithDebug()
    
    for asteroids, description in test_cases:
        print(f"\n{'='*60}")
        print(f"TEST CASE: {description}")
        print(f"Input: {asteroids}")
        print(f"{'='*60}")
        
        result = solution.asteroidCollision(asteroids.copy())
        print(f"\nFINAL RESULT: {result}")
        print(f"{'='*60}")


if __name__ == "__main__":
    demonstrate_optimization_cases()
