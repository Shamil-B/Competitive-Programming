# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        if not head:
            return 
            
        elif head.next:
            current = head.next 

        else:
            return head        
        
        new = ListNode(head.val)
        
        while current:
            current2 = ListNode(current.val)
            current2.next = new
            new = current2
            current = current.next

        return current2