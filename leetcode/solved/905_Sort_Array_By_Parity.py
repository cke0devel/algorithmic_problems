# difficulty: Easy
# Runtime: 130 ms, faster than 32.60% of Python3 online submissions for Sort Array By Parity.
# Memory Usage: 14.7 MB, less than 68.08% of Python3 online submissions for Sort Array By Parity.

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x: x%2)

