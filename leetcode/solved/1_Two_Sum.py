# difficulty: Easy
# Runtime: 6207 ms, faster than 9.66% of Python3 online submissions for Two Sum.
# Memory Usage: 15 MB, less than 63.93% of Python3 online submissions for Two Sum.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

