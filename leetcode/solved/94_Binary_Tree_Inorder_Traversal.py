# difficulty: Easy
# Runtime: 79 ms, faster than 5.08% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 13.8 MB, less than 68.12% of Python3 online submissions for Binary Tree Inorder Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

