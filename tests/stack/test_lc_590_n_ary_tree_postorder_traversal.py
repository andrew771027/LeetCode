from typing import List, Optional

import pytest
from hypothesis import given
from hypothesis import strategies as st

from src.stack.lc_590_n_ary_tree_postorder_traversal import Solution
from tests.stack.utils.helper import Node, build_nary_tree


@pytest.mark.parametrize(
    "root, expected_result",
    [
        ([1, None, 3, 2, 4, None, 5, 6], [5, 6, 3, 2, 4, 1]),
        (
            [
                1,
                None,
                2,
                3,
                4,
                5,
                None,
                None,
                6,
                7,
                None,
                8,
                None,
                9,
                10,
                None,
                None,
                11,
                None,
                12,
                None,
                13,
                None,
                None,
                14,
            ],
            [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1],
        ),
        ([1], [1]),
        ([], []),
    ],
)
def test_normal_case_1(root, expected_result):
    root: Node = build_nary_tree(root)
    assert Solution().postorder(root) == expected_result


@pytest.mark.parametrize(
    "root, expected_result",
    [
        pytest.param(
            [1, None, 3, 2, 4, None, 5, 6], [5, 6, 3, 2, 4, 1], id="Normal Case"
        ),
        pytest.param(
            [
                1,
                None,
                2,
                3,
                4,
                5,
                None,
                None,
                6,
                7,
                None,
                8,
                None,
                9,
                10,
                None,
                None,
                11,
                None,
                12,
                None,
                13,
                None,
                None,
                14,
            ],
            [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1],
            id="Normal Case Group",
        ),
        pytest.param([1], [1], id="Single Node Case"),
        pytest.param([], [], id="Empty Case"),
    ],
)
def test_normal_case_2(root, expected_result):
    root: Node = build_nary_tree(root)
    assert Solution().postorder(root) == expected_result


def postorder_recursive(root: Optional[Node]):
    if not root:
        return []

    result = []
    for child in root.children:
        result.extend(postorder_recursive(child))

    result.append(root.val)
    return result


@st.composite
def nary_tree(draw, max_nodes=10):
    size = draw(st.integers(min_value=0, max_value=max_nodes))

    if size == 0:
        return None

    nodes: List[Node] = [Node(i) for i in range(size)]

    for i in range(1, size):
        parent = draw(st.integers(min_value=0, max_value=i - 1))
        nodes[parent].children.append(nodes[i])

    return nodes[0]


@given(nary_tree())
def test_noraml_case_3(root):
    sol = Solution()

    assert sol.postorder(root) == postorder_recursive(root)
