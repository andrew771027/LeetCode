from typing import List

import pytest

from src.linkedlist.lc_206_reverse_linked_list import Solution
from tests.linkedlist.utils.helper import ListNode, linkedlist_to_list, list_to_linkedlist


@pytest.mark.parametrize(
    "head, expected_result",
    [([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]), ([1, 2], [2, 1]), ([], [])],
)
def test_normal_case(head: List, expected_result: List):
    head: ListNode = list_to_linkedlist(head)
    result: ListNode = Solution().reverseList(head)
    actual_result: List = linkedlist_to_list(result)
    assert actual_result == expected_result
