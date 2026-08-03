import pytest

from src.tree.lc_501_find_mode_in_binary_search_tree import Solution
from tests.tree.utils.helper import TreeNode, list_to_tree


@pytest.mark.parametrize(
    "values, expected",
    [
        pytest.param(
            [1, None, 2, 2],
            [2],
            id="single-mode",
        ),
        pytest.param(
            [2, 1, 3],
            [1, 2, 3],
            id="all-values-are-modes",
        ),
        pytest.param(
            [2, 1, 2],
            [2],
            id="duplicate-root-value",
        ),
        pytest.param(
            [1],
            [1],
            id="single-node",
        ),
        pytest.param(
            [],
            [],
            id="empty-tree",
        ),
    ],
)
def test_find_mode(values: list[int], expected: int):
    root: TreeNode = list_to_tree(values)
    actual = Solution().findMode(root)
    assert sorted(actual) == sorted(expected)
