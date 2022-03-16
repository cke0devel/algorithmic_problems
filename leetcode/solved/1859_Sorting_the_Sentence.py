# difficulty: Easy
# Runtime: 38 ms, faster than 64.92% of Python3 online submissions for Sorting the Sentence.
# Memory Usage: 13.9 MB, less than 71.47% of Python3 online submissions for Sorting the Sentence.

class Solution:
    def sortSentence(self, s: str) -> str:
        l = sorted(s.split(), key=lambda x: x[-1])

        return ' '.join([e[:-1] for e in l])

