# difficulty: Easy
# Wrong Answer:
#   input:
#       [1,2,2,1]
#       [2]
#   Output:
#       [2, 2]
#   Expected:
#       [2]

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        from itertools import chain

        c1, c2 = Counter(nums1), Counter(nums2)
        return list(chain(*[[k]*v for k,v in c1.items() if k in c2]))
