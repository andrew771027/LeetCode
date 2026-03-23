from typing import List

import pytest

from src.linkedlist.lc_234_palindrome_linked_list import Solution
from tests.linkedlist.utils.helper import ListNode, list_to_linkedlist


@pytest.mark.parametrize(
    "head, expected_result",
    [([1, 2, 2, 1], True), ([1, 2], False), ([], True), ([1], True)],
)
def test_normal_case(head: List, expected_result: bool):
    head: ListNode = list_to_linkedlist(head)
    result: bool = Solution().isPalindrome(head)
    assert result is expected_result
