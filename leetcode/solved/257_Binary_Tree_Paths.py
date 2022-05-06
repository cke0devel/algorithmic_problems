# difficulty: Easy
# Runtime: 37 ms, faster than 71.76% of Python3 online submissions for Binary Tree Paths.
# Memory Usage: 13.9 MB, less than 29.98% of Python3 online submissions for Binary Tree Paths.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], paths: List[str], cur: List[str]):
        if(root == None):
            return

        cur.append(str(root.val))

        if root.left==None and root.right==None:
            paths.append('->'.join(cur))

        self.dfs(root.left, paths, cur)
        self.dfs(root.right, paths, cur)

        cur.pop()


    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root == None:
            return []

        ans = []
        self.dfs(root, ans, [])

        return ans


