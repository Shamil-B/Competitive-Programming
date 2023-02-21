# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        before = prev = dummy = ListNode(-1,head)
        cur = head
        
        while cur:
            if (cur.val != prev.val or prev==dummy) and (not cur.next or cur.val != cur.next.val):
                before.next = cur
                before = cur
                
            prev = cur
            cur = cur.next
            
        before.next = None
            
        return dummy.next
                
            