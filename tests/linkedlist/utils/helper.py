from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linkedlist(nums: List) -> ListNode:

    dummy = ListNode(0)
    current: ListNode = dummy

    for n in nums:
        current.next = ListNode(n)
        current = current.next

    return dummy.next


def linkedlist_to_list(node: ListNode) -> List:

    result: List = []

    while node:
        result.append(node.val)
        node = node.next

    return result
