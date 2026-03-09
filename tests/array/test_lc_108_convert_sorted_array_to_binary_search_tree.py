from collections import deque
from typing import List

from src.array.lc_108_convert_sorted_array_to_binary_search_tree import Solution, TreeNode


def levelorder(root: TreeNode) -> List:
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    return result


def test_normal_case_1():
    result = Solution().sortedArrayToBST(nums=[-10, -3, 0, 5, 9])
    assert levelorder(result) == [0, -3, 9, -10, None, 5]


def test_normal_case_2():
    result = Solution().sortedArrayToBST(nums=[1, 3])
    assert levelorder(result) == [3, 1]
