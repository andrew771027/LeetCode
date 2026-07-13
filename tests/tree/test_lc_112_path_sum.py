from typing import Optional

import pytest

from src.tree.lc_112_path_sum import Solution
from tests.tree.utils.helper import list_to_tree


@pytest.mark.parametrize(
    "values, target_sum, expected",
    [
        pytest.param(
            [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1],
            22,
            True,
            id="path-exists",
        ),
        pytest.param(
            [1, 2, 3],
            5,
            False,
            id="path-does-not-exist",
        ),
        pytest.param(
            [],
            0,
            False,
            id="empty-tree",
        ),
        pytest.param(
            [1],
            1,
            True,
            id="single-node-matches",
        ),
        pytest.param(
            [1],
            2,
            False,
            id="single-node-does-not-match",
        ),
        pytest.param(
            [1, 2, None, 3],
            3,
            False,
            id="sum-matches-before-leaf",
        ),
        pytest.param(
            [-2, None, -3],
            -5,
            True,
            id="negative-values",
        ),
    ],
)
def test_has_path_sum(
    values: list[Optional[int]], target_sum: int, expected: bool
) -> None:
    root = list_to_tree(values)
    actual = Solution().hasPathSum(root, target_sum)
    assert actual is expected
