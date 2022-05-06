# difficulty: Medium
# Runtime: 215 ms, faster than 47.85% of Python3 online submissions for Path Sum III.
# Memory Usage: 19.2 MB, less than 9.47% of Python3 online submissions for Path Sum III.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], targetSum: int, path: List[int]) -> int:
        if root == None:
            return 0

        cnt = 0
        curPath = path +[root.val]
        s = targetSum
        for n in reversed(curPath):
            s -= n
            if s == 0:
                cnt += 1

        left, right = 0, 0
        if root.left:
            cnt += self.dfs(root.left, targetSum, curPath)
        if root.right:
            cnt += self.dfs(root.right, targetSum, curPath)

        return cnt

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.dfs(root, targetSum, [])

