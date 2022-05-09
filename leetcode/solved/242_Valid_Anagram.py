# difficulty: Easy:
# Runtime: 108 ms, faster than 9.68% of Python3 online submissions for Valid Anagram.
# Memory Usage: 15.1 MB, less than 12.10% of Python3 online submissions for Valid Anagram.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

