# difficulty: Easy
# Runtime: 43 ms, faster than 62.96% of Python3 online submissions for Add Digits.
# Memory Usage: 13.9 MB, less than 13.34% of Python3 online submissions for Add Digits.

class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum(int(d) for d in str(num))

        return num

