# difficulty: Easy
# Runtime: 484 ms, faster than 83.05% of Python3 online submissions for Contains Duplicate.
# Memory Usage: 26.1 MB, less than 32.21% of Python3 online submissions for Contains Duplicate.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True

        return False

