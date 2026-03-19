from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy: ListNode = ListNode(0)
        dummy.next = head

        previous: ListNode = dummy
        current: ListNode = head

        while current:
            if current.val == val:
                previous.next = current.next  # 刪掉 current
            else:
                previous = current  # 只在沒刪時移動 prev
            current = current.next

        return dummy.next
