# difficulty: Easy
# Runtime: 37 ms, faster than 66.38% of Python3 online submissions for Count of Matches in Tournament.
# Memory Usage: 14 MB, less than 31.88% of Python3 online submissions for Count of Matches in Tournament.

class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0

        while n>1:
            matches += n//2
            n = n//2 + n%2

        return matches

