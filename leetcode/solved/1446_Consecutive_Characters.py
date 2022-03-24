# difficulty: Easy
# Runtime: 48 ms, faster than 80.91% of Python3 online submissions for Consecutive Characters.
#Memory Usage: 14 MB, less than 21.99% of Python3 online submissions for Consecutive Characters.

class Solution:
    def maxPower(self, s: str) -> int:
        power = 1
        cnt = 1
        prev = s[0]

        for c in s[1:]:
            if c != prev:
                power = max(power, cnt)
                cnt = 1
            else:
                cnt += 1

            prev = c

        return max(power, cnt)

