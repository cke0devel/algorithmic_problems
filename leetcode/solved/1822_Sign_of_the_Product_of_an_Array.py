# difficulty: Easy
# Runtime: 101 ms, faster than 26.37% of Python3 online submissions for Sign of the Product of an Array.
# Memory Usage: 14 MB, less than 79.43% of Python3 online submissions for Sign of the Product of an Array.

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1

        for n in nums:
            if n == 0:
                return 0

            if n > 0:
                ans *= 1
            else:
                ans *= -1

        return ans

