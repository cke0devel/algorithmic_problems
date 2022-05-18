# difficulty: Easy
# Runtime: 73 ms, faster than 9.39% of Python3 online submissions for Sum of Digits of String After Convert.
# Memory Usage: 13.9 MB, less than 22.58% of Python3 online submissions for Sum of Digits of String After Convert.

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        digits = map(int, list(''.join(map(lambda x: str(ord(x)-ord('a')+1), list(s)))))

        for _ in range(k):
            ans = sum(digits)

            digits = map(int, list(str(ans)))

        return ans

