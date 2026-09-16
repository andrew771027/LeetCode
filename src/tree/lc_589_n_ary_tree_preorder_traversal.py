from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node"]] = None
    ):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        """
        stack = LIFO
        要 reverse children 才能維持順序
        preorder: 由左到右

        # Preorder：到一個節點就處理（top-down）
        # Postorder：等子樹全部處理完才處理（bottom-up）
        """
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.children:
                # key point
                stack.extend(node.children[::-1])

        # key point
        return result
