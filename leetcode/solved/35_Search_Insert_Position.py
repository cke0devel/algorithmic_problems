# difficulty: Easy
# Runtime: 53 ms, faster than 78.40% of Python3 online submissions for Search Insert Position.
# Memory Usage: 14.7 MB, less than 54.69% of Python3 online submissions for Search Insert Position.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        import bisect

        return bisect.bisect_left(nums, target)

