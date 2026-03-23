from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Method 1: Using List
        """
        list_val: List = []
        while head:
            list_val.append(head.val)
            head = head.next

        left, right = 0, len(list_val) - 1

        while left < right and list_val[left] == list_val[right]:
            left += 1
            right -= 1

        return left >= right

    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #     """
    #     Method 2: Using Stack
    #     """
    #     stack: List = []
    #     current: ListNode = head

    #     while current:
    #         stack.append(current.val)
    #         current = current.next

    #     current = head
    #     while current and current.val == stack.pop():
    #         current = current.next

    #     return current is None

    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #     """
    #     Method 3: Using Recursion
    #     As you know, if any problem you can do using stack only then you can use
    #     recursion as well ( mostly ).
    #     So we will have one global pointer as curr we will move this pointer once
    #     we reach the end and recursion will start from end of the list.
    #     """
    #     self.current: ListNode = head

    #     return self.solved(self.current)

    # def solved(self, head: Optional[ListNode]) -> bool:
    #     if head is None:
    #         return True
    #     ans: bool = self.solved(head.next) and head.val == self.current.val
    #     self.current = self.current.next
    #     return ans

    # def gen_reverse_linked_list(self, head: Optional[ListNode]) -> ListNode:
    #     previous: ListNode = None
    #     current: ListNode = head
    #     while current:
    #         next_temp: ListNode = current.next
    #         current.next = previous
    #         previous = current
    #         current = next_temp
    #     return previous

    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #     """
    #     Method 4: Using Reverse Linked List
    #     """
    #     slow: ListNode = head
    #     fast: ListNode = head

    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next

    #     reversed: ListNode = self.gen_reverse_linked_list(slow)

    #     while reversed:
    #         if head.val != reversed.val:
    #             return False
    #         head = head.next
    #         reversed = reversed.next
    #     return True
