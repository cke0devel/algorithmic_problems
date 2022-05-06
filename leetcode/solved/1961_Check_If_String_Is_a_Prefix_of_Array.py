# difficulry: Easy
# Runtime: 49 ms, faster than 47.23% of Python3 online submissions for Check If String Is a Prefix of Array.
# Memory Usage: 13.8 MB, less than 70.42% of Python3 online submissions for Check If String Is a Prefix of Array.

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        for word in words:
            if s.startswith(word):
                s = s[len(word):]

                if len(s) == 0:
                    return True
            else:
                return False

        return False


