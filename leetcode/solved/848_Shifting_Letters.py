# difficulty: Medium
# Runtime: 1299 ms, faster than 32.08% of Python3 online submissions for Shifting Letters.
# Memory Usage: 24 MB, less than 99.53% of Python3 online submissions for Shifting Letters.

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        for i in range(len(shifts)-2, -1, -1):
            shifts[i] = (shifts[i] + shifts[i+1]) % 26

        ans = [chr(((ord(c)-ord('a') + shifts[i])%26)+ord('a')) for i, c in enumerate(s)]
        return ''.join(ans)
