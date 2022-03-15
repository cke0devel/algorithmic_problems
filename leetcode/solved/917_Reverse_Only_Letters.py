# difficulty: Easy
# Runtime: 51 ms, faster than 31.36% of Python3 online submissions for Reverse Only Letters.
# Memory Usage: 13.8 MB, less than 74.08% of Python3 online submissions for Reverse Only Letters.

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left, right = 0, len(s)-1

        l = list(s)
        while left < right:
            if l[left].isalpha():
                if l[right].isalpha():
                    l[left], l[right] = l[right], l[left]
                    left += 1
                    right -= 1
                else:
                    right -= 1
            else:
                left += 1

        return ''.join(l)

