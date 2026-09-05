from typing import Optional

import pytest

from src.tree.lc_404_sum_of_left_leaves import Solution
from tests.tree.utils.helper import list_to_binary_tree


@pytest.mark.parametrize(
    "values, expected",
    [
        pytest.param([3, 9, 20, None, None, 15, 7], 24, id="leetcode-example"),
        pytest.param([1], 0, id="single-root-is-not-left-leaf"),
        pytest.param([], 0, id="empty-tree"),
        pytest.param([1, 2], 2, id="single-left-leaf"),
        pytest.param([1, None, 2], 0, id="single-right-leaf"),
        pytest.param(
            [1, 2, 3, 4, 5, 6, 7],
            10,
            id="multiple-left-leaves",
        ),
        pytest.param([1, 2, None, 3], 3, id="deep-left-leaf"),
    ],
)
def test_sum_of_leaves(values: list[Optional[int]], expected: int) -> None:
    root = list_to_binary_tree(values)

    actual = Solution().sumOfLeftLeaves(root)

    assert actual == expected
