# difficulty: Easy
# Runtime: 209 ms, faster than 5.78% of Python3 online submissions for Count Equal and Divisible Pairs in an Array.
# Memory Usage: 13.9 MB, less than 73.79% of Python3 online submissions for Count Equal and Divisible Pairs in an Array.

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and (i*j) % k == 0:
                    ans += 1

        return ans

