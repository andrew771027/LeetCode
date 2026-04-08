import pytest
from hypothesis import given
from hypothesis import strategies as st

from src.stack.lc_589_n_ary_tree_preorder_traversal import Solution
from tests.stack.utils.helper import Node, build_nary_tree


@pytest.mark.parametrize(
    "root, expected_result",
    [
        ([1, None, 3, 2, 4, None, 5, 6], [1, 3, 5, 6, 2, 4]),
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
            [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10],
        ),
        ([1, None, 2, 3, 4], [1, 2, 3, 4]),
        ([1], [1]),
        ([], []),
    ],
)
def test_normal_case_1(root, expected_result):
    root: Node = build_nary_tree(root)
    assert Solution().preorder(root) == expected_result


@pytest.mark.parametrize(
    "root, expected_result",
    [
        pytest.param(
            [1, None, 3, 2, 4, None, 5, 6], [1, 3, 5, 6, 2, 4], id="Normal Case"
        ),
        pytest.param([1], [1], id="Single Node Case"),
        pytest.param([], [], id="Empty Case"),
    ],
)
def test_normal_case_2(root, expected_result):
    root: Node = build_nary_tree(root)
    assert Solution().preorder(root) == expected_result


def preorder_recursive(root):
    if not root:
        return []
    return [root.val] + [
        v for child in root.children for v in preorder_recursive(child)
    ]


@st.composite
def nary_tree(draw, max_nodes=10):
    size = draw(st.integers(min_value=0, max_value=max_nodes))

    if size == 0:
        return None

    nodes = [Node(i) for i in range(size)]

    for i in range(1, size):
        parent = draw(st.integers(min_value=0, max_value=i - 1))
        nodes[parent].children.append(nodes[i])

    return nodes[0]


@given(nary_tree())
def test_normal_case_3(root):
    sol = Solution()

    assert sol.preorder(root) == preorder_recursive(root)
