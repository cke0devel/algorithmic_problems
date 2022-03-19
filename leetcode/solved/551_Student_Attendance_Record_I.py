# difficulty: Easy
# Runtime: 58 ms, faster than 15.51% of Python3 online submissions for Student Attendance Record I.
# Memory Usage: 13.8 MB, less than 68.25% of Python3 online submissions for Student Attendance Record I.

class Solution:
    def checkRecord(self, s: str) -> bool:
        return not (s.count('A') > 1 or 'LLL' in s)

