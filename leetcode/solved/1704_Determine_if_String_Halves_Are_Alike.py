# difficulty: Easy
# Runtime: 57 ms, faster than 38.68% of Python3 online submissions for Determine if String Halves Are Alike.
# Memory Usage: 13.9 MB, less than 86.19% of Python3 online submissions for Determine if String Halves Are Alike.

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = len(s)//2
        a,b = s[:l], s[l:]
        
        count_vowel = lambda x: len([c for c in x if c in 'aeiouAEIOU'])
        return count_vowel(a) == count_vowel(b)

