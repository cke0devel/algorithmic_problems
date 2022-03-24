# difficulty: Medium
# Runtime: 2852 ms, faster than 13.52% of Python3 online submissions for Rearrange Array Elements by Sign.
# Memory Usage: 44.6 MB, less than 85.03% of Python3 online submissions for Rearrange Array Elements by Sign.

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        plus = [n for n in nums if n>0]
        minus = [n for n in nums if n<0]

        ans = []
        for i in range(0, len(nums), 2):
            ans.append(plus[i//2])
            ans.append(minus[i//2])

        return ans

