# difficulty: Easy
# Runtime: 69 ms, faster than 73.35% of Python3 online submissions for Sort Even and Odd Indices Independently.
# Memory Usage: 13.8 MB, less than 98.08% of Python3 online submissions for Sort Even and Odd Indices Independently.

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = sorted(nums[1::2], reverse=True)
        even = sorted(nums[0::2])

        ans = [0] * len(nums)
        for i,n in enumerate(odd):
            ans[i*2 + 1] = n
        for i,n in enumerate(even):
            ans[i*2] = n

        return ans

