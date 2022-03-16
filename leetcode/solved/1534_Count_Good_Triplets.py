# difficulty: Easy
# Runtime: 814 ms, faster than 47.29% of Python3 online submissions for Count Good Triplets.
# Memory Usage: 13.8 MB, less than 99.65% of Python3 online submissions for Count Good Triplets.

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                        ans += 1

        return ans

