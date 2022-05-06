# difficulty: Easy
# Runtime: 62 ms, faster than 43.08% of Python3 online submissions for Path Sum.
# Memory Usage: 15.1 MB, less than 60.62% of Python3 online submissions for Path Sum.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False

        targetSum -= root.val

        if root.left==None and root.right==None:
            return targetSum == 0

        if root.left and self.hasPathSum(root.left, targetSum):
            return True

        if root.right and self.hasPathSum(root.right, targetSum):
            return True

        return False

