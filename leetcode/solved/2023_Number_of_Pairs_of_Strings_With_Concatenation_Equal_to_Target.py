# difficulty: Medium
# Runtime: 93 ms, faster than 36.32% of Python3 online submissions for Number of Pairs of Strings With Concatenation Equal to Target.
# Memory Usage: 13.9 MB, less than 98.38% of Python3 online submissions for Number of Pairs of Strings With Concatenation Equal to Target.

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        ans = 0

        for i,prefix in enumerate(nums):
            for j,postfix in enumerate(nums):
                if i == j:
                    continue

                if prefix+postfix == target:
                    ans += 1

        return ans

