from typing import Optional

import pytest

from src.tree.lc_530_minimum_absolute_difference_in_bst import Solution
from tests.tree.utils.helper import list_to_binary_tree


@pytest.mark.parametrize(
    "values, expected",
    [
        pytest.param([4, 2, 6, 1, 3], 1, id="leetcode-example"),
        pytest.param([1, 0, 48, None, None, 12, 49], 1, id="minimum-on-right"),
        pytest.param([2, 1], 1, id="two-nodes"),
        pytest.param([10, 5, 20, 2, 8, 15, 30], 2, id="multiple-levels"),
    ],
)
def test_get_minimum_difference(values: list[Optional[int]], expected: int):
    root = list_to_binary_tree(values)
    actual = Solution().getMinimumDifference(root)
    assert actual == expected
