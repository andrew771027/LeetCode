from typing import Optional

import pytest

from src.tree.lc_783_minimum_distance_between_bst_nodes import Solution
from tests.tree.utils.helper import list_to_binary_tree


@pytest.mark.parametrize(
    "values, expected",
    [
        pytest.param([4, 2, 6, 1, 3], 1, id="leetcode-example"),
        pytest.param([1, 0, 48, None, None, 12, 49], 1, id="minimum-on-right"),
        pytest.param([2, 1], 1, id="two-nodes"),
        pytest.param([10, 5, 20, 2, 8, 15, 30], 2, id="multiple-levels"),
        pytest.param(
            [10, 5, None, None, 9],
            1,
            id="minimum-not-parent-child",
        ),
    ],
)
def test_normal_case(values: list[Optional[int]], expected: int):
    root = list_to_binary_tree(values)
    actual = Solution().minDiffInBST(root)
    assert actual == expected
