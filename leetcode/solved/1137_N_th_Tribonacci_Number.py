# difficulty: Easy
# Runtime: 39 ms, faster than 61.58% of Python3 online submissions for N-th Tribonacci Number.
# Memory Usage: 13.9 MB, less than 24.82% of Python3 online submissions for N-th Tribonacci Number.

class Solution:
    def tribonacci(self, n: int) -> int:
        a,b,c,d = 0,1,1,2

        if n <= 2:
            return [0,1,1][n]

        for _ in range(3, n+1):
            d = a + b + c
            a,b,c,d = b,c,d,d

        return d

