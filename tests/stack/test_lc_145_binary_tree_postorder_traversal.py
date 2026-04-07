import pytest

from src.stack.lc_145_binary_tree_postorder_traversal import Solution
from tests.stack.utils.helper import TreeNode, list_to_tree


@pytest.mark.parametrize(
    "root, expected_result",
    [
        ([1, None, 2, 3], [3, 2, 1]),
        ([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], [4, 6, 7, 5, 2, 9, 8, 3, 1]),
        ([], []),
        ([1], [1]),
    ],
)
def test_normal_case(root, expected_result):
    root: TreeNode = list_to_tree(root)
    assert Solution().postorderTraversal(root) == expected_result
