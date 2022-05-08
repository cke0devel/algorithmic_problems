# difficulty: Easy
# Runtime: 253 ms, faster than 71.07% of Python3 online submissions for Squares of a Sorted Array.
# Memory Usage: 16.4 MB, less than 18.77% of Python3 online submissions for Squares of a Sorted Array.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([n**2 for n in nums])

