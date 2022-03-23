# difficulty: Easy
# Wrong Answer
#   input: 10
#   output: 10
#   Expected: 1

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 10:
            num = sum(int(d) for d in str(num))

        return num

