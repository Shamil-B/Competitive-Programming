# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        
        cur = slow = fast = head
        size = 0
        
        while cur:
            size += 1
            cur = cur.next
            
        k = k%size
        n = k

        if n==0:
            return head
        
        while n>0:
            fast = fast.next
            n -= 1
            
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
            
        newHead = slow.next
        slow.next = None
        fast.next = head
        
        return newHead
        