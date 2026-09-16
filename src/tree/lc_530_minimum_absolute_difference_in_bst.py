from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        values = []

        self.inorder(root, values)

        min_difference = float("inf")

        for i in range(1, len(values)):
            difference = values[i] - values[i - 1]

            min_difference = min(difference, min_difference)

        return min_difference
    
    def inorder(self, node: Optional[TreeNode], values: list[int]) -> None:

        if node is None
            return
        
        self.inorder(node.left, values)
        values.append(node.val)
        self.inorder(node.right, values)


        
