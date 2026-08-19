# Definition for a Node.
from collections import deque
from typing import List, Optional


class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node"]] = None
    ):
        self.val = val
        self.children = children


class Solution:
    def maxDepth_method_1(self, root: "Node") -> int:
        """
        Iterative DFS + Stack
        """

        if not root:
            return 0

        # 目前走到哪個節點 & 第幾層
        stack: list[tuple[Node, int]] = [(root, 1)]
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            max_depth = max(depth, max_depth)
            for child in node.children:
                stack.append((child, depth + 1))

        return max_depth

    def maxDepth_method_2(self, root: "Node") -> int:
        """
        Recursive DFS
        """
        if root is None:
            return 0

        if not root.children:
            return 1

        child_depths = []

        for child in root.children:
            child_depths.append(self.maxDepth_method_2(child))

        return 1 + max(child_depths)

    def maxDepth_method_3(self, root: "Node") -> int:
        """
        BFS / Level Order
        """
        if root is None:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()

                for child in node.children:
                    queue.append(child)

            depth += 1

        return depth
