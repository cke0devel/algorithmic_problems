# difficulty: Medium
# Runtime: 32 ms, faster than 91.90% of Python3 online submissions for Flip Equivalent Binary Trees.
# Memory Usage: 13.8 MB, less than 83.93% of Python3 online submissions for Flip Equivalent Binary Trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False

        ret = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        if not ret:
            ret = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)

        return ret
