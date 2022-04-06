# difficulty: Easy
# Runtime: 94 ms, faster than 85.92% of Python3 online submissions for Divide Array Into Equal Pairs.
# Memory Usage: 13.9 MB, less than 90.83% of Python3 online submissions for Divide Array Into Equal Pairs.

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        from collections import Counter

        return all(v%2 == 0 for v in Counter(nums).values())

