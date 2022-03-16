# difficulty: Easy
# Runtime: 59 ms, faster than 86.24% of Python3 online submissions for Count Operations to Obtain Zero.
# Memory Usage: 13.9 MB, less than 21.07% of Python3 online submissions for Count Operations to Obtain Zero.

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        steps = 0

        if num1 >= num2:
            num1, num2 = num2, num1

        while num1:
            steps += num2 // num1
            num2 = num2 % num1
            num1, num2 = num2, num1

        return steps

