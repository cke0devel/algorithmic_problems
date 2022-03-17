# difficulty: Easy
# Runtime: 269 ms, faster than 31.68% of Python3 online submissions for Largest Triangle Area.
# Memory Usage: 13.8 MB, less than 99.01% of Python3 online submissions for Largest Triangle Area.

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ans = 0

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                for k in range(j+1, len(points)):
                    a,b,c = points[i], points[j], points[k]

                    area = (a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) - (a[0]*c[1] + b[0]*a[1] + c[0]*b[1])
                    area = abs(area) / 2

                    ans = max(ans, area)

        return ans

