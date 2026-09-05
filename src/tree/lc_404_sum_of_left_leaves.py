from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return self.dfs(root, False)

    def dfs(self, node: TreeNode, is_left: bool):
        if not node:
            return 0

        # Leaf node
        if not node.left and not node.right:
            return node.val if is_left else 0

        left_sum = self.dfs(node.left, True)
        right_sum = self.dfs(node.right, False)

        return left_sum + right_sum
