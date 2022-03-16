# difficulty: Easy
# Runtime: 1236 ms, faster than 95.01% of Python3 online submissions for Maximum Average Subarray I.
#Memory Usage: 26.2 MB, less than 21.43% of Python3 online submissions for Maximum Average Subarray I.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[0:k])
        max_s = s

        for i in range(k, len(nums)):
            s = s - nums[i-k] + nums[i]
            max_s = max(max_s, s)

        return max_s / k

