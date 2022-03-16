# difficulty: Easy
# Runtime: 53 ms, faster than 49.54% of Python3 online submissions for Unique Number of Occurrences.
# Memory Usage: 14 MB, less than 48.16% of Python3 online submissions for Unique Number of Occurrences.

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter

        c = Counter(arr)

        return len(c.keys()) == len(set(c.values()))

