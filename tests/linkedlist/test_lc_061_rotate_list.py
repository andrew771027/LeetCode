from typing import List

import pytest

from src.linkedlist.lc_061_rotate_list import Solution
from tests.linkedlist.utils.helper import ListNode, linkedlist_to_list, list_to_linkedlist


@pytest.mark.parametrize(
    "head, k, expected_result",
    [
        ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 1, [5, 1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([1, 2, 3, 4, 5], 3, [3, 4, 5, 1, 2]),
        ([1, 2, 3, 4, 5], 4, [2, 3, 4, 5, 1]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 6, [5, 1, 2, 3, 4]),
        ([0, 1, 2], 0, [0, 1, 2]),
        ([0, 1, 2], 1, [2, 0, 1]),
        ([0, 1, 2], 2, [1, 2, 0]),
        ([0, 1, 2], 3, [0, 1, 2]),
        ([0, 1, 2], 4, [2, 0, 1]),
    ],
)
def test_normal_case(head, k, expected_result):
    head: ListNode = list_to_linkedlist(head)
    result: ListNode = Solution().rotateRight(head=head, k=k)
    actual_result: List = linkedlist_to_list(result)
    assert actual_result == expected_result
