from typing import List

import pytest

from src.linkedlist.lc_019_remove_nth_node_from_end_of_list import Solution
from tests.linkedlist.utils.helper import ListNode, linkedlist_to_list, list_to_linkedlist


@pytest.mark.parametrize(
    "head, n , expected_result",
    [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2, 3], 1, [1, 2]),
        ([1, 2], 2, [2]),
    ],
)
def test_normal_case(head: List, n: int, expected_result: List):
    head: ListNode = list_to_linkedlist(head)
    result = Solution().removeNthFromEnd(head, n)
    actual_result = linkedlist_to_list(result)
    assert actual_result == expected_result
