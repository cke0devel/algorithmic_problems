# difficulty: Easy
# Runtime: 83 ms, faster than 40.32% of Python3 online submissions for Third Maximum Number.
# Memory Usage: 15.3 MB, less than 57.28% of Python3 online submissions for Third Maximum Number.

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        from collections import Counter

        nums = sorted(Counter(nums).keys(), reverse=True)

        if len(nums) < 3:
            return nums[0]

        return nums[2]

