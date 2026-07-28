from typing import List, Optional
from tests.tree.utils.helper import list_to_tree
from src.tree.lc_222_count_complete_tree_nodes import Solution


@pytest.mark.parametrize(
    "values, expected",
    [
        pytest.param(
            [1, 2, 3, 4, 5, 6],
            6,
            id="complete-tree",
        ),
        pytest.param(
            [1, 2, 3, 4, 5, 6, 7],
            7,
            id="perfect-tree",
        ),
        pytest.param(
            [1],
            1,
            id="single-node",
        ),
        pytest.param(
            [],
            0,
            id="empty-tree",
        ),
        pytest.param(
            [1, 2],
            2,
            id="two-nodes",
        ),
    ],
)
def test_count_nodes(values: List[Optional[int]], expected:int):
    root = list_to_tree(values)
    actual = Solution(root)
    assert actual == expected
