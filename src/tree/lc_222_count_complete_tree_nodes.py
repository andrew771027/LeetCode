# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_height = self.get_left_height(root)
        right_height = self.get_right_height(root)

        # 左右高度相同，代表這是一棵 perfect binary tree
        if left_height == right_height:
            return (2**left_height) - 1

        # 否則繼續遞迴計算左右子樹
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def get_left_height(self, node: TreeNode) -> int:
        height = 0

        while node is not None:
            height += 1
            node = node.left

        return height

    def get_right_height(self, node: TreeNode) -> int:
        height = 0

        while node is not None:
            height += 1
            node = node.right

        return height
