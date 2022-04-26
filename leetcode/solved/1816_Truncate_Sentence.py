# difficulty: Easy
# Runtime: 33 ms, faster than 74.97% of Python3 online submissions for Truncate Sentence.
# Memory Usage: 13.9 MB, less than 17.76% of Python3 online submissions for Truncate Sentence.
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split()[:k])

