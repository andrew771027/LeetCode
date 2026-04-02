from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        1. Count the length of the list.
        2. Connect the tail to the head to form a cycle.
        3. Find the new tail: (length - k % length) steps from head.
        4. Break the cycle and return the new head.
        """

        if not head or k == 0:
            return head

        length: int = 1
        tail: ListNode = head

        while tail.next:
            tail = tail.next
            length += 1

        k = k % length

        if k == 0:
            return head

        # Make it circular
        tail.next = head

        steps_to_new_head: int = length - k
        new_tail: ListNode = tail

        while steps_to_new_head:
            new_tail = new_tail.next
            steps_to_new_head -= 1

        new_head: ListNode = new_tail.next
        new_tail.next = None

        return new_head
