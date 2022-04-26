# difficulty: Easy
# Runtime: 50 ms, faster than 41.81% of Python3 online submissions for Maximum Number of Balloons.
# Memory Usage: 14.1 MB, less than 13.52% of Python3 online submissions for Maximum Number of Balloons.

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter

        c = Counter(text)
        balloon = Counter("balloon")

        ans = 0
        while True:
            c.subtract(balloon)

            if len([x for x in c.values() if x<0]) > 0:
                break

            ans += 1

        return ans


