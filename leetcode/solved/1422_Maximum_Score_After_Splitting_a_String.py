# difficulty: Easy
# Runtime: 32 ms, faster than 94.46% of Python3 online submissions for Maximum Score After Splitting a String.
# Memory Usage: 13.8 MB, less than 65.54% of Python3 online submissions for Maximum Score After Splitting a String.

class Solution:
    def maxScore(self, s: str) -> int:
        one = [0]*len(s)
        zero = [0]*len(s)

        cnt = 0
        for i, c in enumerate(s):
            if c == '0':
                cnt += 1
            zero[i] = cnt

        cnt = 0
        for i, c in enumerate(reversed(s)):
            if c == '1':
                cnt += 1
            one[i] = cnt
        one.reverse()

        ans = 0
        for i in range(len(s)-1):
            ans = max(ans, zero[i] + one[i+1])

        return ans
