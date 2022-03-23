# difficulty: Easy
# Runtime: 36 ms, faster than 77.28% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.8 MB, less than 96.78% of Python3 online submissions for Fibonacci Number.

class Solution:
    def fib(self, n: int) -> int:
        a,b,c = 0,1,1

        if n <= 1:
            return n

        for _ in range(2, n+1):
            c = a+b
            a,b,c = b,c,c

        return c


