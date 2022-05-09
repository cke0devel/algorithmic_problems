# difficulty: Easy
# Runtime: 89 ms, faster than 40.75% of Python3 online submissions for Find Subsequence of Length K With the Largest Sum.
# Memory Usage: 14.2 MB, less than 22.52% of Python3 online submissions for Find Subsequence of Length K With the Largest Sum.


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        l = sorted(list(enumerate(nums)), reverse=True, key=lambda x: x[1])[:k]
        l = sorted(l)

        return [v for _,v in l]
