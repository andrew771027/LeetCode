import pytest

from src.stack.lc_094_binary_tree_inorder_traversal import Solution
from tests.stack.utils.helper import TreeNode, list_to_tree


@pytest.mark.parametrize(
    "root, expected_result",
    [
        ([1, None, 2, 3], [1, 3, 2]),
        ([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], [4, 2, 6, 5, 7, 1, 3, 9, 8]),
        ([], []),
        ([1], [1]),
    ],
)
def test_normal_case(root, expected_result):
    root: TreeNode = list_to_tree(root)
    assert Solution().inorderTraversal(root) == expected_result
