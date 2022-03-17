# difficulty: Easy
# Runtime: 279 ms, faster than 43.96% of Python3 online submissions for Largest Perimeter Triangle.
# Memory Usage: 15.5 MB, less than 52.01% of Python3 online submissions for Largest Perimeter Triangle.

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)

        for i in range(len(nums)-2):
            if nums[i] < nums[i+1]+nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]

        return 0
