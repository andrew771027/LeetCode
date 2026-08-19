from collections import deque
from typing import List, Optional


class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node"]] = None
    ):
        self.val = val
        self.children = children if children is not None else []


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(values: list[int]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    index = 1

    while queue and index < len(values):
        current = queue.popleft()

        # 1. create left child
        if index < len(values) and values[index] is not None:
            current.left = TreeNode(values[index])
            queue.append(current.left)

        index += 1

        # 2. create right child
        if index < len(values) and values[index] is not None:
            current.right = TreeNode(values[index])
            queue.append(current.right)

        index += 1

    return root


def list_to_nary_tree(values: list[Optional[int]]) -> Optional[Node]:
    if not values:
        return None

    root = Node(values[0])
    queue = deque([root])

    # skip root and fist node
    index = 2

    while queue and index < len(values):
        parent: Node = queue.popleft()

        while index < len(values) and values[index] is not None:
            child = Node(values[index])
            parent.children.append(child)
            queue.append(child)

            index += 1

        # skip None separator
        index += 1

    return root
