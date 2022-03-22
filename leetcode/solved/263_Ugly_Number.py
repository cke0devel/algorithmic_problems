# difficulty: Easy
# Runtime: 54 ms, faster than 33.33% of Python3 online submissions for Ugly Number.
# Memory Usage: 13.9 MB, less than 24.32% of Python3 online submissions for Ugly Number.

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        while n%2 == 0:
            n = n // 2

        while n%3 == 0:
            n = n // 3

        while n%5 == 0:
            n = n // 5

        return n == 1

