# difficulty: Easy
# Runtime: 1290 ms, faster than 52.50% of Python3 online submissions for Count Special Quadruplets.
# Memory Usage: 13.8 MB, less than 77.76% of Python3 online submissions for Count Special Quadruplets.

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ans = 0

        for a in range(len(nums)):
            for b in range(a+1, len(nums)):
                for c in range(b+1, len(nums)):
                    k = nums[a] + nums[b] + nums[c]

                    for d in range(c+1, len(nums)):
                        if k == nums[d]:
                            ans += 1

        return ans

