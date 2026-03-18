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


def list_to_cycle_linkedlist(nums: list, pos: int) -> ListNode:
    """
    把 tail 指回某個節點
    """

    if not nums:
        return None

    dummy = ListNode(0)
    current: ListNode = dummy
    cycle_node: ListNode = None

    for index, val in enumerate(nums):
        if index != pos:
            current.next = ListNode(val)
            current = current.next
        else:
            cycle_node = current

    if pos != -1:
        current.next = cycle_node

    return dummy.next
