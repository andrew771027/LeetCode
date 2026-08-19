from typing import List, Optional

import pytest
from hypothesis import given
from hypothesis import strategies as st

from src.tree.lc_559_maximum_depth_of_n_ary_tree import Solution
from tests.tree.utils.helper import Node, list_to_nary_tree


@st.composite
def nary_tree(draw, max_nodes=20):
    size = draw(st.integers(min_value=0, max_value=max_nodes))

    if size == 0:
        return None

    values = draw(st.lists(st.integers(), min_size=size, max_size=size))

    nodes: List[Optional["Node"]] = [Node(value) for value in values]

    for index in range(1, size):
        parent_index = draw(st.integers(min_value=0, max_value=index - 1))

        nodes[parent_index].children.append(nodes[index])

    return nodes[0]


def max_depth_recursive(root: Optional[Node]) -> int:
    if root is None:
        return 0

    if not root.children:
        return 1

    return 1 + max(max_depth_recursive(child) for child in root.children)


@pytest.mark.parametrize(
    "values, expected",
    [
        pytest.param(
            [1, None, 3, 2, 4, None, 5, 6],
            3,
            id="leetcode-example",
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
            [1, None, 2, None, 3, None, 4],
            4,
            id="single-long-branch",
        ),
        pytest.param([1, None, 2, 3, 4], 2, id="wide-shallow-tree"),
    ],
)
def test_max_depth(values: List[Optional[int]], expected: int):
    root: Node = list_to_nary_tree(values)
    actual = Solution().maxDepth_method_1(root)
    assert actual == expected
    actual = Solution().maxDepth_method_2(root)
    assert actual == expected
    actual = Solution().maxDepth_method_3(root)
    assert actual == expected


@given(root=nary_tree())
def test_max_depth_property(root):
    actual = Solution().maxDepth_method_1(root)
    expected = max_depth_recursive(root)
    assert actual == expected

    actual = Solution().maxDepth_method_2(root)
    expected = max_depth_recursive(root)
    assert actual == expected

    actual = Solution().maxDepth_method_3(root)
    expected = max_depth_recursive(root)
    assert actual == expected
