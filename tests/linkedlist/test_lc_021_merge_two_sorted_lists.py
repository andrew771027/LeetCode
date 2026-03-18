from typing import List

import pytest

from src.linkedlist.lc_021_merge_two_sorted_lists import ListNode, Solution
from tests.linkedlist.utils.helper import linkedlist_to_list, list_to_linkedlist


@pytest.mark.parametrize(
    "list1, list2, expected_result",
    [([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]), ([], [], []), ([], [0], [0])],
)
def test_normal_case(list1, list2, expected_result):
    linkedlist1: ListNode = list_to_linkedlist(list1)
    linkedlist2: ListNode = list_to_linkedlist(list2)
    result: ListNode = Solution().mergeTwoLists(list1=linkedlist1, list2=linkedlist2)
    actual_result: List = linkedlist_to_list(result)
    assert actual_result == expected_result
