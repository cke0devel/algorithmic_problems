# difficulty: Easy
# Runtime: 61 ms, faster than 13.28% of Python3 online submissions for Backspace String Compare.
# Memory Usage: 13.9 MB, less than 28.32% of Python3 online submissions for Backspace String Compare.

class Solution:
    def _normalize(self, s: str) -> str:
        l = []
        for c in s:
            if c == '#':
                if l:
                    l.pop()
            else:
                l.append(c)

        return ''.join(l)

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self._normalize(s) == self._normalize(t)

