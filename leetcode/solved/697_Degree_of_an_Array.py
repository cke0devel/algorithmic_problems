# Difficulty: Easy
# Runtime: 746 ms, faster than 16.41% of Python3 online submissions for Degree of an Array.
# Memory Usage: 15.4 MB, less than 87.49% of Python3 online submissions for Degree of an Array.

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        from collections import Counter

        c = Counter(nums)
        degree = max(c.values())

        nums_reversed = nums[::-1]
        calc_length = lambda x: len(nums) - 1 - nums_reversed.index(x) - nums.index(x) + 1

        return min(calc_length(k) for k,v in c.items() if v==degree)

