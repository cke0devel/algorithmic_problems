# difficulty: Easy
# Runtime Error:
#   input:
#       [4,3,9,3,1,9,7,6,9,7]
#       [5,0,8]

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter

        c1, c2 = Counter(nums1), Counter(nums2)

        return list(reduce(lambda x,y: x+y,
                           [[k]*min(v, c2[k]) for k, v in c1.items() if k in c2]))
