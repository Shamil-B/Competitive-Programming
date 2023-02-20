# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        if not head.next:
            return None
        
        cur = head
        while cur:
            n += 1
            cur = cur.next
            
        prevInd = n//2-1
        
        ind = 0
        cur = head
        while cur:
            if ind==prevInd:
                cur.next = cur.next.next
                break
                
            ind += 1
            cur = cur.next
                
        return head
            