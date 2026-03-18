from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        1. Initialize variables
        2. Merge the lists
        3. Append remaining nodes
        4. Return the merged list
        """

        dummy = ListNode()
        current: ListNode = dummy

        while list1 and list2:
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next

            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next
