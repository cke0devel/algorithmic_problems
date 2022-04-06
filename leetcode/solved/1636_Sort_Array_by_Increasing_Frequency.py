# difficulty: Easy
# Runtime: 117 ms, faster than 5.47% of Python3 online submissions for Sort Array by Increasing Frequency.
# Memory Usage: 13.9 MB, less than 73.05% of Python3 online submissions for Sort Array by Increasing Frequency.

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter

        items = sorted(Counter(nums).items(), reverse=True, key=lambda x: x[0])
        items = sorted(items, key=lambda x: x[1])

        ans = []
        for n,c in items:
            ans += [n]*c

        return ans

