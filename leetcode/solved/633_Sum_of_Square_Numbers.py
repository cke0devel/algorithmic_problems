# difficulty: Medium
# Runtime: 311 ms, faster than 54.14% of Python3 online submissions for Sum of Square Numbers.
# Memory Usage: 18.5 MB, less than 5.96% of Python3 online submissions for Sum of Square Numbers.

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        square = set([n**2 for n in range(int(sqrt(c)+1))])

        for n in square:
            if c-n in square:
                return True

        return False

