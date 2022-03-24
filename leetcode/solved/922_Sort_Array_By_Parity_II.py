# difficulty: Easy
# Runtime: 208 ms, faster than 95.06% of Python3 online submissions for Sort Array By Parity II.
# Memory Usage: 16.2 MB, less than 73.98% of Python3 online submissions for Sort Array By Parity II.

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: x%2)

        l = len(nums)//2
        for i in range(1, l, 2):
            a, b = i, i + l - 1 + l%2
            nums[a], nums[b] = nums[b], nums[a]

        return nums

