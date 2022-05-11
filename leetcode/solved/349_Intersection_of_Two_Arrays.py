# difficulty: Easy
# Runtime: 63 ms, faster than 57.50% of Python3 online submissions for Intersection of Two Arrays.
# Memory Usage: 14.1 MB, less than 25.63% of Python3 online submissions for Intersection of Two Arrays.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))

