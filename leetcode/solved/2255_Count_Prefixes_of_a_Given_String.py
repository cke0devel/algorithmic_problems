# difficulty: Easy
# Runtime: 110 ms, faster than 12.12% of Python3 online submissions for Count Prefixes of a Given String.
# Memory Usage: 14.1 MB, less than 92.83% of Python3 online submissions for Count Prefixes of a Given String.

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return len([word for word in words if s.startswith(word)])

