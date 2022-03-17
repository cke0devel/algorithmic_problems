# difficulty: Easy
# Runtime: 46 ms, faster than 62.66% of Python3 online submissions for Largest Number At Least Twice of Others.
# Memory Usage: 13.7 MB, less than 97.31% of Python3 online submissions for Largest Number At Least Twice of Others.

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums = sorted(enumerate(nums), reverse=True, key=lambda x: x[1])

        if len(nums)==1 or nums[1][1]*2 <= nums[0][1]:
            return nums[0][0]

        return -1

