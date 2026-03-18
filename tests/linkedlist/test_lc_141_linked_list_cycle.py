import pytest

from src.linkedlist.lc_141_linked_list_cycle import Solution
from tests.linkedlist.utils.helper import ListNode, list_to_cycle_linkedlist


@pytest.mark.parametrize(
    "head, pos, expected_result",
    [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([], -1, False),
    ],
)
def test_normal_case(head, pos, expected_result):
    head: ListNode = list_to_cycle_linkedlist(head, pos)
    actual_result: bool = Solution().hasCycle(head=head)
    assert actual_result is expected_result
