# difficulty: Easy
# Runtime: 395 ms, faster than 17.95% of Python3 online submissions for Count Number of Pairs With Absolute Difference K.
# Memory Usage: 13.9 MB, less than 76.54% of Python3 online submissions for Count Number of Pairs With Absolute Difference K.

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i]-nums[j]) == k:
                    ans += 1

        return ans

