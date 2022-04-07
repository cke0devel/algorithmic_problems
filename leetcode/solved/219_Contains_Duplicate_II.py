# difficulty: Easy
# Runtime: 1259 ms, faster than 5.02% of Python3 online submissions for Contains Duplicate II.
# Memory Usage: 35 MB, less than 5.28% of Python3 online submissions for Contains Duplicate II.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums = sorted([(v,i) for i,v in list(enumerate(nums))])

        for i in range(1, len(nums)):
            if nums[i-1][0] == nums[i][0] and nums[i][1]-nums[i-1][1] <= k:
                return True

        return False

