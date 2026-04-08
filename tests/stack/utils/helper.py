from collections import deque
from typing import List, Optional


class Node:
    """
    General Tree
    """
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children or []


class TreeNode:
    """
    Binary Tree
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # left
        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)

            i += 1

        # right
        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)

            i += 1

    return root


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # 去掉尾巴多餘的 None（LeetCode 會省略）
    while result and result[-1] is None:
        result.pop()

    return result


def build_nary_tree(values: List[Optional[int]]) -> Optional[Node]:
    if not values:
        return None

    root = Node(values[0])
    queue = deque([root])

    i = 2

    while queue and i < len(values):
        parent: Node = queue.popleft()
        children = []

        while i < len(values) and values[i] is not None:
            child = Node(values[i])
            children.append(child)
            queue.append(child)

            i += 1

        parent.children = children
        i += 1  # skip null

    return root
