# difficulty: Easy
# Runtime: 66 ms, faster than 31.62% of Python3 online submissions for Find the Middle Index in Array.
# Memory Usage: 13.9 MB, less than 60.62% of Python3 online submissions for Find the Middle Index in Array.

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        left = 0

        for i, n in enumerate(nums):
            right = total - n - left

            if left == right:
                return i

            left += n

        return -1
