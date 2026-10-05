# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode | None) -> int:

        self.previous: Optional[int] = None

        self.min_difference = float("inf")

        self.inorder(root)

        return self.min_difference

    def inorder(self, node: Optional[TreeNode]) -> None:
        if node is None:
            return

        # left
        self.inorder(node.left)

        if self.previous is not None:

            difference = node.val - self.previous

            self.min_difference = min(self.min_difference, difference)

        self.previous = node.val

        # right
        self.inorder(node.right)
