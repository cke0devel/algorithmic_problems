# difficulty: Easy
# Runtime: 56 ms, faster than 36.01% of Python3 online submissions for Happy Number.
# Memory Usage: 13.9 MB, less than 23.80% of Python3 online submissions for Happy Number.

class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        while True:
            s.add(n)
            n = sum(int(d)**2 for d in str(n))

            if n in s or n == 1:
                break

        return n == 1

