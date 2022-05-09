# difficulty: Easy
# Runtime: 51 ms, faster than 91.05% of Python3 online submissions for Reverse Vowels of a String.
# Memory Usage: 14.8 MB, less than 91.34% of Python3 online submissions for Reverse Vowels of a String.

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = list(reversed([c for c in s if c in 'aeiouAEIOU']))

        ans = ''
        vi = 0
        for c in s:
            if c in 'aeiouAEIOU':
                ans += vowels[vi]
                vi += 1
            else:
                ans += c

        return ans

