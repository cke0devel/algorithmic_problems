# diffidulty: Easy
# Runtime Error:
#   input:[[0,0,0],[0,1,1]]
#         1
#         1
#         1

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        H,W = len(image), len(image[0])

        oldColor = image[sr][sc]

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

