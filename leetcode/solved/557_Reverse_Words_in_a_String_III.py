# difficulty: Easy
# Runtime: 39 ms, faster than 82.06% of Python3 online submissions for Reverse Words in a String III.
# Memory Usage: 14.6 MB, less than 48.18% of Python3 online submissions for Reverse Words in a String III.

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(''.join(reversed(word)) for word in s.split())

