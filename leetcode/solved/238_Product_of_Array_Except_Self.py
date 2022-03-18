# difficulty: Medium
# Runtime: 346 ms, faster than 40.88% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 21.2 MB, less than 59.76% of Python3 online submissions for Product of Array Except Self.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from math import prod

        all = prod(nums)
        zeros = nums.count(0)

        if zeros > 1:
            return [0] * len(nums)

        ans = []
        for num in nums:
            if num == 0:
                ans.append(prod([num for num in nums if num]))
            else:
                if zeros:
                    ans.append(0)
                else:
                    ans.append(all // num)

        return ans

