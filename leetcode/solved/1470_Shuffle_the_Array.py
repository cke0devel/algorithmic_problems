# difficulty: Easy
# Runtime: 65 ms, faster than 77.45% of Python3 online submissions for Shuffle the Array.
# Memory Usage: 14 MB, less than 91.80% of Python3 online submissions for Shuffle the Array.

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []

        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[n+i])

        return ans

