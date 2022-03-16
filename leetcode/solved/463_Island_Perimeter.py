# difficulty: Easy
# Runtime: 641 ms, faster than 70.84% of Python3 online submissions for Island Perimeter.
# Memory Usage: 14.3 MB, less than 78.01% of Python3 online submissions for Island Perimeter.

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0

        H,W = len(grid), len(grid[0])

        for r in range(H):
            for c in range(W):
                if grid[r][c] == 0:
                    continue

                if r==0 or grid[r-1][c]==0:
                    perimeter += 1
                if c==W-1 or grid[r][c+1]==0:
                    perimeter += 1
                if r==H-1 or grid[r+1][c]==0:
                    perimeter += 1
                if c==0 or grid[r][c-1]==0:
                    perimeter += 1

        return perimeter



