class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else stack and stack[-1] < a:
                stack.pop()