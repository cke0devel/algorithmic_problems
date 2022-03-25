# difficulty: Medium
# Runtime: 3912 ms, faster than 5.07% of Python3 online submissions for Number of Good Ways to Split a String.
# Memory Usage: 14.6 MB, less than 93.97% of Python3 online submissions for Number of Good Ways to Split a String.

class Solution:
    def numSplits(self, s: str) -> int:
        from collections import Counter

        left, right = Counter(""), Counter(s)

        ans = 0
        for c in s:
            left = left + Counter(c)
            right = right - Counter(c)

            if len(set(left.keys())) == len(set(right.keys())):
                ans += 1

        return ans

