# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = cur
        if not head:
            return head
        
        while cur:
            if cur.val!=prev.val:
                prev.next = cur
                prev = cur
                
            cur = cur.next
            
        prev.next = cur
            
        return head