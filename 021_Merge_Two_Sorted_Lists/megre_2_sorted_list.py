class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():

    def method_iterative(self, l1: ListNode, l2: ListNode) -> ListNode:

        result = ListNode(None)    
        current = result
        
        while l1 and l2:
            if l1.val > l2.val:
                current.next = l2
                l2 = l2.next
            else:
                current.next = l1
                l1 = l1.next
            current = current.next
        
        if l1 != None:
            current.next = l1
        elif l2 != None:
            current.next = l2
        else:
            pass
        
        return result.next
    
    def method_recursive(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        if l1.val < l2.val:
            l1.next = self.method_recursive(l1.next, l2)
            return l1
        else:
            l2.next = self.method_recursive(l1, l2.next)
            return l2
