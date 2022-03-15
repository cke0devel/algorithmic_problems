# difficulty: Easy
# Runtime: 40 ms, faster than 97.86% of Python3 online submissions for Largest Odd Number in String.
# Memory Usage: 15.4 MB, less than 26.74% of Python3 online submissions for Largest Odd Number in String.

class Solution:
    def largestOddNumber(self, num: str) -> str:
        def rfind_if(l: str, f:Callable) -> int:
            for i,v in enumerate(l[::-1]):
                if f(v):
                    return len(l) - 1 - i

            return -1

        last_idx = rfind_if(num, lambda x: x in '13579')
        if last_idx < 0:
            return ""

        return num[:last_idx+1]

