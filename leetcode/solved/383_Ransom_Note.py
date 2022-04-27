# difficulty: Easy
# Runtime: 65 ms, faster than 71.30% of Python3 online submissions for Ransom Note.
# Memory Usage: 14.1 MB, less than 54.48% of Python3 online submissions for Ransom Note.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter

        return Counter(ransomNote) <= Counter(magazine)

