from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node"]] = None
    ):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        """
        1. This approach simulates the recursive postorder traversal using a stack.
        2. We push nodes into the stack and process them iteratively.
           When we encounter a node, we push its children onto the stack
           in reverse order (so that the leftmost child is processed first).
        3. Once all the children of a node are processed, the node itself
           is added to the result list.

        # 先做 root → children 再 reverse → children → root

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
                stack.extend(node.children)

        # key point
        return result[::-1]
