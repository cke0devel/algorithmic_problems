# difficulty: Easy
# Runtime: 103 ms, faster than 5.32% of Python3 online submissions for Count Integers With Even Digit Sum.
# Memory Usage: 13.9 MB, less than 12.15% of Python3 online submissions for Count Integers With Even Digit Sum.

class Solution:
    def countEven(self, num: int) -> int:
        return sum([sum(map(int, list(str(n))))%2 == 0 for n in range(1, num+1)])

