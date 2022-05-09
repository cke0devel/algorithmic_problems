# difficulty: Medium
# Runtime: 485 ms, faster than 92.50% of Python3 online submissions for Count Servers that Communicate.
# Memory Usage: 15.7 MB, less than 74.82% of Python3 online submissions for Count Servers that Communicate.

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        from collections import defaultdict

        m = len(grid)
        n = len(grid[0])

        ans = 0

        row = defaultdict(int)
        col = defaultdict(int)

        for y in range(m):
            for x in range(n):
                if grid[y][x] == 1:
                    row[y] += 1
                    col[x] += 1

        for y in range(m):
            for x in range(n):
                if grid[y][x] == 1 and (row[y]>1 or col[x]>1):
                    ans += 1

        return ans
