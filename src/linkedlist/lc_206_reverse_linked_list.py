from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous: ListNode = None
        current: ListNode = head

        while current:
            temp: ListNode = current.next   # 1️⃣ 暫存 next
            current.next = previous         # 2️⃣ 反轉指標
            previous = current              # 3️⃣ previous 前進
            current = temp                  # 4️⃣ current 前進

        return previous
