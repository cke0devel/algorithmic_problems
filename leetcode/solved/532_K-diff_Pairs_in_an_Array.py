# difficulty: Medium
# Runtime: 75 ms, faster than 93.52% of Python3 online submissions for K-diff Pairs in an Array.
# Memory Usage: 16 MB, less than 27.62% of Python3 online submissions for K-diff Pairs in an Array.

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        from collections import Counter

        c = Counter(nums)

        if k == 0:
            return len([n for n in c.values() if n > 1])

        s = set(nums)
        ans = 0

        for n in s:
            m = k + n

            if m in s:
                ans += 1

        return ans

