# difficulty: Easy
# Runtime: 159 ms, faster than 90.45% of Python3 online submissions for Binary Prefix Divisible By 5.
# Memory Usage: 15.2 MB, less than 35.11% of Python3 online submissions for Binary Prefix Divisible By 5.

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = 0

        ret = []
        for k in nums:
            n = (n*2 + k) % 5

            ret.append(n == 0)

        return ret

