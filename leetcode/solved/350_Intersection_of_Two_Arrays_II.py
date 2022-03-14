# difficulty: Easy
# Runtime: 91 ms, faster than 23.91% of Python3 online submissions for Intersection of Two Arrays II.
#Memory Usage: 14.2 MB, less than 26.97% of Python3 online submissions for Intersection of Two Arrays II.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter

        intersection = Counter(nums1) & Counter(nums2)

        if not intersection:
            return []

        return list(reduce(lambda x,y: x+y,
                           [[k]*v for k, v in intersection.items()]))
