# difficulty: Easy
# Runtime: 108 ms, faster than 14.76% of Python3 online submissions for Find Greatest Common Divisor of Array.
# Memory Usage: 13.9 MB, less than 88.81% of Python3 online submissions for Find Greatest Common Divisor of Array.

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        from math import gcd

        return gcd(min(nums), max(nums))

