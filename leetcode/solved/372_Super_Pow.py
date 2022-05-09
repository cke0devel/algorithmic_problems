# difficulty: Medium
# Runtime: 103 ms, faster than 87.61% of Python3 online submissions for Super Pow.
# Memory Usage: 14 MB, less than 60.61% of Python3 online submissions for Super Pow.

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        b = int(''.join([str(digit) for digit in b]))

        return pow(a,b, 1337)
