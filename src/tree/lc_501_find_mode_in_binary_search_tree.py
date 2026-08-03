# Definition for a binary tree node.
from typing import Dict, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        frequencies: Dict[str, int] = {}

        self.calculate_frequency(root, frequencies)

        max_frequency = max(frequencies.values())

        modes = [
            value
            for value, frequency in frequencies.items()
            if frequency == max_frequency
        ]

        return modes

    def calculate_frequency(
        self, node: TreeNode, frequencies: Dict[str, int]
    ) -> Dict[str, int]:

        if not node:
            return

        if node.val in frequencies:
            frequencies[node.val] += 1
        else:
            frequencies[node.val] = 1

        self.calculate_frequency(node.left, frequencies)
        self.calculate_frequency(node.right, frequencies)
