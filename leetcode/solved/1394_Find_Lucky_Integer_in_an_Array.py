# difficulty: Easy
# Runtime: 114 ms, faster than 23.11% of Python3 online submissions for Find Lucky Integer in an Array.
# Memory Usage: 14 MB, less than 23.73% of Python3 online submissions for Find Lucky Integer in an Array.

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter

        nums = [k for k,v in Counter(arr).items() if k==v]

        if not nums:
            return -1

        return max(nums)

