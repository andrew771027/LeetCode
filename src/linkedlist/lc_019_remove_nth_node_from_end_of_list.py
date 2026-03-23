from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        fast 先走 n 步
        然後 fast / slow 一起走
        """
        dummy = ListNode(0)
        dummy.next = head

        fast: ListNode = dummy
        slow: ListNode = dummy

        # 1️⃣ fast 先走 n+1 步（讓 slow 停在前一個）
        for _ in range(n + 1):
            fast = fast.next

        # 2️⃣ 同時移動
        while fast:
            fast = fast.next
            slow = slow.next

        # 3️⃣ 刪除節點
        slow.next = slow.next.next

        return dummy.next
