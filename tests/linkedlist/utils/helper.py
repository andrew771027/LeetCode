from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def list_to_linkedlist(nums: list[int]) -> Optional[ListNode]:
    """Convert a list of integers to a linked list."""
    dummy = ListNode(0)
    current: ListNode = dummy
    for n in nums:
        current.next = ListNode(n)
        current = current.next
    return dummy.next


def linkedlist_to_list(node: Optional[ListNode]) -> list[int]:
    """Convert a linked list to a list of integers."""
    result: List = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def list_to_cycle_linkedlist(nums: list[int], pos: int) -> Optional[ListNode]:
    """
    Create a linked list from a list of integers with a cycle at position pos.
    If pos == -1, no cycle is created.
    """
    if not nums:
        return None

    dummy = ListNode(0)
    current: ListNode = dummy
    cycle_node = None

    for index, val in enumerate(nums):
        current.next = ListNode(val)
        current = current.next
        if index == pos:
            cycle_node = current

    if pos != -1 and cycle_node:
        current.next = cycle_node  # Create the cycle

    return dummy.next


def lists_to_interection_linkedlists(
    listA: list[int], listB: list[int], skipA: int, skipB: int
) -> tuple[ListNode, ListNode, Optional[ListNode]]:
    """
    Create two linked lists from lists with an intersection at specified positions.
    listA: [4,1,8,4,5]
    listB: [5,6,1,8,4,5]
    skipA: 2
    skipB: 3
    """

    # 建立A
    dummy_a = ListNode(0)
    current_a: ListNode = dummy_a
    nodes_a: list[ListNode] = []

    for val in listA:
        current_a.next = ListNode(val)
        current_a = current_a.next
        nodes_a.append(current_a)

    # 建立B
    dummy_b = ListNode(0)
    current_b: ListNode = dummy_b
    nodes_b: list[ListNode] = []

    for val in listB:
        current_b.next = ListNode(val)
        current_b = current_b.next
        nodes_b.append(current_b)

    # 建立 intersection（共享 node）
    intersection_node: ListNode = None
    if skipA < len(nodes_a) and skipB < len(nodes_b):
        nodes_b[skipB].next = nodes_a[skipA]
        intersection_node = nodes_a[skipA]

    return dummy_a.next, dummy_b.next, intersection_node
