import pytest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if not head :
            return head

        previous = head
        current = head.next

        while current:

            if previous.val == current.val:
            
                current = current.next
                previous.next = current

            else:
                previous = current
                current = current.next

        return head
        
def test_1st_testcase():

    c = ListNode(2 , None)
    b = ListNode(1, c)
    a = ListNode(1, b)

    test = Solution()
    test.deleteDuplicates(head=a)