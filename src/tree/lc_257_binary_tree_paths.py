# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        path = ""

        self.dfs(root, path, result)

        return result

    def dfs(self, node: TreeNode, path: str, result: List):
        if not node:
            return

        if path:
            current_path = f"{path}->{node.val}"
        else:
            current_path = str(node.val)

        if not node.left and not node.right:
            result.append(current_path)
            return

        self.dfs(node.left, current_path, result)
        self.dfs(node.right, current_path, result)
