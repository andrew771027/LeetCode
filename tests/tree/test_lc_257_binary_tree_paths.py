from typing import List, Optional

import pytest

from src.tree.lc_257_binary_tree_paths import Solution
from tests.tree.utils.helper import TreeNode, list_to_tree


@pytest.mark.parametrize(
    "values, expected",
    [
        pytest.param(
            [1, 2, 3, None, 5],
            ["1->2->5", "1->3"],
            id="two-root-to-leaf-paths",
        ),
        pytest.param(
            [1],
            ["1"],
            id="single-node",
        ),
        pytest.param(
            [],
            [],
            id="empty-tree",
        ),
        pytest.param(
            [1, 2, None, 3, None, 4],
            ["1->2->3->4"],
            id="left-skewed-tree",
        ),
        pytest.param(
            [1, None, 2, None, 3],
            ["1->2->3"],
            id="right-skewed-tree",
        ),
        pytest.param(
            [1, 2, 3, 4, 5, 6, 7],
            [
                "1->2->4",
                "1->2->5",
                "1->3->6",
                "1->3->7",
            ],
            id="complete-binary-tree",
        ),
        pytest.param(
            [-1, -2, 3],
            ["-1->-2", "-1->3"],
            id="negative-values",
        ),
    ],
)
def test_binary_tree_paths(values: List[Optional[int]], expected: List[str]) -> None:
    root: TreeNode = list_to_tree(values)
    actual = Solution().binaryTreePaths(root)
    assert sorted(actual) == sorted(expected)
