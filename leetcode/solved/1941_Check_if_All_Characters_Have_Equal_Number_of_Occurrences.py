# difficulty: Easy
# Runtime: 49 ms, faster than 53.27% of Python3 online submissions for Check if All Characters Have Equal Number of Occurrences.
# Memory Usage: 13.8 MB, less than 82.99% of Python3 online submissions for Check if All Characters Have Equal Number of Occurrences.

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import Counter

        return len(set(Counter(s).values())) == 1

