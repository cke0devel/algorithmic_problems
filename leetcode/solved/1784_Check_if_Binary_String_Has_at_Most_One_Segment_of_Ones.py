# difficulty: Easy
# Runtime: 24 ms, faster than 98.79% of Python3 online submissions for Check if Binary String Has at Most One Segment of Ones.
# Memory Usage: 13.8 MB, less than 70.63% of Python3 online submissions for Check if Binary String Has at Most One Segment of Ones.

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        p = s.find("0")
        if p < 0:
            return True

        p = s.find("1", p)

        return p < 0

