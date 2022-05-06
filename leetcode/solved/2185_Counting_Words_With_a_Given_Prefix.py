# difficulty: Easy
# Runtime: 55 ms, faster than 50.69% of Python3 online submissions for Counting Words With a Given Prefix.
# Memory Usage: 14 MB, less than 29.09% of Python3 online submissions for Counting Words With a Given Prefix.

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return len([word for word in words if word.startswith(pref)])

