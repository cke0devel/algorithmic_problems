# difficulty: Easy
# Runtime: 37 ms, faster than 68.54% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
# Memory Usage: 13.9 MB, less than 15.10% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        import math

        digits = [int(d) for d in str(n)]

        return math.prod(digits) - sum(digits)

