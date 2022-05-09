# difficulty: Easy
# Runtime: 56 ms, faster than 91.14% of Python3 online submissions for Minimum Absolute Difference in BST.
# Memory Usage: 16 MB, less than 45.47% of Python3 online submissions for Minimum Absolute Difference in BST.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], values: List[int]) -> None:
        if not root:
            return

        if root.left:
            self.dfs(root.left, values)

        values.append(root.val)

        if root.right:
            self.dfs(root.right, values)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []

        self.dfs(root, values)

        ans = values[1] - values[0]

        for i in range(2, len(values)):
            ans = min(ans, values[i]-values[i-1])

        return ans

