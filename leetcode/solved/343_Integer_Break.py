# difficulty: Medium
# Runtime: 38 ms, faster than 76.44% of Python3 online submissions for Integer Break.
# Memory Usage: 13.8 MB, less than 74.13% of Python3 online submissions for Integer Break.

class Solution:
    def integerBreak(self, n: int) -> int:
        ans = 1
        k = 2

        while n//k >= 1:
            a,b = n//k, n%k
            ans = max(ans, math.prod([a+1]*b + [a]*(k-b)))

            k += 1

        return ans
