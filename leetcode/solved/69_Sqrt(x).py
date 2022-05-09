# difficulty: Easy
# Runtime: 8000 ms, faster than 5.00% of Python3 online submissions for Sqrt(x).
# Memory Usage: 13.8 MB, less than 58.14% of Python3 online submissions for Sqrt(x).

class Solution:
    def mySqrt(self, x: int) -> int:
        k = 1

        while True:
            n = k**2
            if n == x:
                return k
            if n > x:
                return k-1

            k += 1

        return 0

