# difficulty: Easy
# Runtime: 28 ms, faster than 94.17% of Python3 online submissions for Check if Numbers Are Ascending in a Sentence.
# Memory Usage: 13.8 MB, less than 73.78% of Python3 online submissions for Check if Numbers Are Ascending in a Sentence.

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l = [int(token) for token in s.split() if token.isdigit()]

        for i in range(1, len(l)):
            if l[i-1] >= l[i]:
                return False

        return True

