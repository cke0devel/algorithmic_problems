# difficulty: Easy
# Runtime: 40 ms, faster than 60.95% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
# Memory Usage: 13.9 MB, less than 30.92% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.

class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0

        while num>0:
            if num%2:
                num = num - 1
            else:
                num = num // 2

            steps += 1

        return steps

