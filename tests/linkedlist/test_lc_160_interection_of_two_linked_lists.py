from typing import List

import pytest

from src.linkedlist.lc_160_interection_of_two_linked_lists import Solution
from tests.linkedlist.utils.helper import lists_to_interection_linkedlists


@pytest.mark.parametrize(
    "listA, listB, skipA, skipB, expected_result",
    [
        ([4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3, 8),
        ([1, 9, 1, 2, 4], [3, 2, 4], 3, 1, 2),
        ([2, 6, 4], [1, 5], 3, 2, None),
    ],
)
def test_normal_case(
    listA: List, listB: List, skipA: int, skipB: int, expected_result: int
):
    head_a, head_b, intersect_node = lists_to_interection_linkedlists(
        listA=listA, listB=listB, skipA=skipA, skipB=skipB
    )

    actual_result = Solution().getIntersectionNode(headA=head_a, headB=head_b)

    if expected_result is None:
        assert actual_result is None
    else:
        assert actual_result is intersect_node
        assert actual_result.val == expected_result
