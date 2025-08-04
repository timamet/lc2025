from typing import List
from collections import defaultdict


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Count frequency of each row pattern using tuples
        row_count = defaultdict(int)
        for row in grid:
            row_count[tuple(row)] += 1
        
        result = 0
        
        # For each column, add count of matching row patterns
        for col_idx in range(n):
            column = tuple(grid[row_idx][col_idx] for row_idx in range(n))
            result += row_count[column]
        
        return result
    
    # Alternative: O(n^3) solution without hash map (your original approach optimized)
    def equalPairs_simple(self, grid: List[List[int]]) -> int:
        n = len(grid)
        result = 0
        
        # For each column, count how many rows match it
        for col_idx in range(n):
            # Extract column
            column = [grid[row_idx][col_idx] for row_idx in range(n)]
            
            # Count matching rows (use original grid rows directly)
            for row_idx in range(n):
                if grid[row_idx] == column:
                    result += 1
        
        return result
    

grid = [[3,2,1],[1,7,6],[2,7,7]]
res = Solution().equalPairs(grid)

print(res)