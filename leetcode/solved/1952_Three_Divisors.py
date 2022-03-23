# difficulty: Easy
# Runtime: 57 ms, faster than 34.21% of Python3 online submissions for Three Divisors.
# Memory Usage: 13.9 MB, less than 22.58% of Python3 online submissions for Three Divisors.

class Solution:
    def isThree(self, n: int) -> bool:
        import math

        if n == 1:
            return False

        k = int(math.sqrt(n))

        for p in range(2,k):
            if n % p == 0:
                return False

        return k*k == n

