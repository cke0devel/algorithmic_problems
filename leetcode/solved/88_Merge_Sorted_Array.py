# difficulty: Easy
# Runtime: 40 ms, faster than 81.89% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 13.8 MB, less than 86.71% of Python3 online submissions for Merge Sorted Array.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m+n - 1
        m, n = m-1, n-1

        while m>=0 or n>=0:
            if n<0 or (m>=0 and nums1[m] >= nums2[n]):
                nums1[p] = nums1[m]
                m -= 1
            else:
                nums1[p] = nums2[n]
                n -= 1

            p -= 1
