# dificulty: Easy
# Runtime: 61 ms, faster than 48.06% of Python3 online submissions for Maximum Number of Words Found in Sentences.
# Memory Usage: 13.9 MB, less than 87.77% of Python3 online submissions for Maximum Number of Words Found in Sentences.

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(s.split()) for s in sentences)

