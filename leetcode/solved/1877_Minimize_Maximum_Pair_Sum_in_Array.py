# difficulty: Medium
# Runtime: 2075 ms, faster than 13.92% of Python3 online submissions for Minimize Maximum Pair Sum in Array.
# Memory Usage: 27.5 MB, less than 89.86% of Python3 online submissions for Minimize Maximum Pair Sum in Array.

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        ans = 0
        for i in range(len(nums)):
            ans = max(ans, nums[i]+nums[-i-1])

        return ans
