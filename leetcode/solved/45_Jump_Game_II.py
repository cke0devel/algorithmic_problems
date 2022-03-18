# difficulty: Medium
# Runtime: 6664 ms, faster than 24.34% of Python3 online submissions for Jump Game II.
# Memory Usage: 15.1 MB, less than 35.55% of Python3 online submissions for Jump Game II.


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = list(range(len(nums)))

        for i in range(len(nums)):
            for j in range(i+1, min(i+nums[i]+1, len(nums))):
                jumps[j] = min(jumps[j], jumps[i]+1)

        return jumps[-1]

