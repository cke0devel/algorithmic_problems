# difficulty: Easy
# Runtime: 192 ms, faster than 40.86% of Python3 online submissions for Minimum Operations to Make the Array Increasing.
# Memory Usage: 14.6 MB, less than 67.37% of Python3 online submissions for Minimum Operations to Make the Array Increasing.

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cur = nums[0]
        ans = 0

        for n in nums[1:]:
            if n <= cur:
                ans += cur + 1 - n
                cur = cur+1
            else:
                cur = n

        return ans

