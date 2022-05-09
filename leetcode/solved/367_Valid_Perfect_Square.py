# difficulty: Easy
# Runtime: 93 ms, faster than 5.11% of Python3 online submissions for Valid Perfect Square.
# Memory Usage: 13.9 MB, less than 11.34% of Python3 online submissions for Valid Perfect Square.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        k = 1

        while True:
            n = k**2
            if n > num:
                break

            if n == num:
                return True

            k += 1

        return False

