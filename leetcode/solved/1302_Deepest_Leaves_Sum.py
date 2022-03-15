# difficulty: Medium
# Runtime: 294 ms, faster than 53.07% of Python3 online submissions for Deepest Leaves Sum.
# Memory Usage: 17.7 MB, less than 94.99% of Python3 online submissions for Deepest Leaves Sum.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        from collections import defaultdict

        self.depthSum = defaultdict(int)
        self.maxDepth = -1

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self._dfs(0, root)

        return self.depthSum[self.maxDepth]

    def _dfs(self, depth: int, root: Optional[TreeNode]) -> None:
        if root:
            self.maxDepth = max(self.maxDepth, depth)
            self.depthSum[depth] += root.val

            self._dfs(depth+1, root.left)
            self._dfs(depth+1, root.right)


