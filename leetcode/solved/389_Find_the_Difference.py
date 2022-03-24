# difficulty: Easy
# Runtime: 36 ms, faster than 87.83% of Python3 online submissions for Find the Difference.
# Memory Usage: 13.9 MB, less than 35.45% of Python3 online submissions for Find the Difference.

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter

        return list((Counter(t) - Counter(s)).keys())[0]

