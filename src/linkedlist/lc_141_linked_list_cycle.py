from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow: ListNode = head
        fast: ListNode = head

        while fast and fast.next:  # 如果fast為none, fast.next也是none
            slow = slow.next
            fast = fast.next.next

            if slow is fast:  # 不同 node 可能 值一樣。故要比較node本身
                # 判斷是否 同一個記憶體位置
                return True  # Cycle detected

        # No cycle
        return False
