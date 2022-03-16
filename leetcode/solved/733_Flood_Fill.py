# diffidulty: Easy
# Runtime: 80 ms, faster than 85.04% of Python3 online submissions for Flood Fill.
# Memory Usage: 14 MB, less than 92.97% of Python3 online submissions for Flood Fill.

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        H,W = len(image), len(image[0])

        oldColor = image[sr][sc]

        if oldColor == newColor:
            return image

        image[sr][sc] = newColor

        if sr>0 and image[sr-1][sc] == oldColor:
            self.floodFill(image, sr-1, sc, newColor)

        if sr<H-1 and image[sr+1][sc] == oldColor:
            self.floodFill(image, sr+1, sc, newColor)

        if sc>0 and image[sr][sc-1] == oldColor:
            self.floodFill(image, sr, sc-1, newColor)

        if sc<W-1 and image[sr][sc+1] == oldColor:
            self.floodFill(image, sr, sc+1, newColor)

        return image

