# difficulty: Easy
# Runtime: 56 ms, faster than 88.39% of Python3 online submissions for Find Numbers with Even Number of Digits.
# Memory Usage: 13.9 MB, less than 88.24% of Python3 online submissions for Find Numbers with Even Number of Digits.

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([n for n in nums if len(str(n)) % 2 == 0])

