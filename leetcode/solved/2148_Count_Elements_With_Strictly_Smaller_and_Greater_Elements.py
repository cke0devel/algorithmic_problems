# difficulty: Easy
# Runtime: 71 ms, faster than 26.39% of Python3 online submissions for Count Elements With Strictly Smaller and Greater Elements .
# Memory Usage: 13.9 MB, less than 89.83% of Python3 online submissions for Count Elements With Strictly Smaller and Greater Elements .

class Solution:
    def countElements(self, nums: List[int]) -> int:
        low, high = min(nums), max(nums)

        return len([n for n in nums if low<n and n<high])



