# difficulty: Easy
# Runtime: 574 ms, faster than 23.30% of Python3 online submissions for Max Consecutive Ones.
# Memory Usage: 14.4 MB, less than 39.61% of Python3 online submissions for Max Consecutive Ones.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        cnt = 0

        for n in nums:
            if n == 0:
                ans = max(ans, cnt)
                cnt = 0
            else:
                cnt += 1

        return max(ans, cnt)

