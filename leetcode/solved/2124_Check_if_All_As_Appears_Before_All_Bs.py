# difficulty: Eady
# Runtime: 33 ms, faster than 76.34% of Python3 online submissions for Check if All A's Appears Before All B's.
# Memory Usage: 13.9 MB, less than 36.89% of Python3 online submissions for Check if All A's Appears Before All B's.

class Solution:
    def checkString(self, s: str) -> bool:
        b = s.find('b')
        if b == -1:
            return True
        return s.find('a', b) == -1

