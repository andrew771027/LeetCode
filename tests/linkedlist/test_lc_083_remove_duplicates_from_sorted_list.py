from typing import List

import pytest

from src.linkedlist.lc_083_remove_duplicates_from_sorted_list import Solution
from tests.linkedlist.utils.helper import ListNode, linkedlist_to_list, list_to_linkedlist


@pytest.mark.parametrize(
    "head, expected_result",
    [([1, 1, 2], [1, 2]), ([1, 1, 2, 3, 3], [1, 2, 3]), ([], []), ([1, 1, 1], [1])],
)
def test_normal_case(head, expected_result):
    head: ListNode = list_to_linkedlist(head)
    result = Solution().deleteDuplicates(head=head)
    actual_result: List = linkedlist_to_list(result)
    assert actual_result == expected_result
