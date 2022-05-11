# difficulty: Easy
# Runtime: 186 ms, faster than 58.70% of Python3 online submissions for Find Pivot Index.
# Memory Usage: 15.3 MB, less than 11.87% of Python3 online submissions for Find Pivot Index.

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        left = 0

        for i, n in enumerate(nums):
            right = total - n - left

            if left == right:
                return i

            left += n

        return -1
