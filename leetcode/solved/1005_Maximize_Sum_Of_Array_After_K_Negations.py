# difficulty: Easy
# Runtime: 55 ms, faster than 79.49% of Python3 online submissions for Maximize Sum Of Array After K Negations.
# Memory Usage: 14 MB, less than 57.55% of Python3 online submissions for Maximize Sum Of Array After K Negations.

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)

        p = 0
        while p<len(nums) and k>0:
            if nums[p] < 0:
                nums[p] = -nums[p]
                p += 1
                k -= 1
            else:
                break

        nums = sorted(nums)

        if k%2 == 1:
            nums[0] = -nums[0]

        return sum(nums)

