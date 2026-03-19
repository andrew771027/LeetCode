from typing import List

import pytest

from src.linkedlist.lc_203_remove_linked_list_elements import Solution
from tests.linkedlist.utils.helper import ListNode, linkedlist_to_list, list_to_linkedlist


@pytest.mark.parametrize(
    "head, val, expected_result",
    [([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]), ([], 1, []), ([7, 7, 7, 7], 7, [])],
)
def test_normal_case(head: List, val: int, expected_result: List):
    head: ListNode = list_to_linkedlist(head)
    result: ListNode = Solution().removeElements(head=head, val=val)
    actual_result: List = linkedlist_to_list(result)
    assert actual_result == expected_result
