# difficulty: Easy
# Runtime: 432 ms, faster than 9.99% of Python3 online submissions for N-Repeated Element in Size 2N Array.
# Memory Usage: 15.5 MB, less than 57.25% of Python3 online submissions for N-Repeated Element in Size 2N Array.

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums) // 2
        for i in range(len(nums)):
            if i+n-1 >= len(nums):
                break

            if nums[i] == nums[i+n-1]:
                return nums[i]

