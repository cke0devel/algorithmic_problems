# difficulty: Easy
# Runtime: 48 ms, faster than 35.14% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 13.9 MB, less than 66.55% of Python3 online submissions for Climbing Stairs.

class Solution:
    def climbStairs(self, n: int) -> int:
        stair = [0] * (n+1)

        stair[0] = 1
        stair[1] = 1

        for i in range(2, n+1):
            stair[i] = stair[i-1] + stair[i-2]

        return stair[-1]


