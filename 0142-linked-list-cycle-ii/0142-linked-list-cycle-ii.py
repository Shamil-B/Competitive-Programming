# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fast = slow = head
        ind = 0
        meet = False
        while fast and fast.next:
            if fast==slow and ind:
                meet = True
                break 
            
            slow = slow.next
            fast = fast.next.next
            ind += 1
            
        fast = head
        while slow and fast and fast!= slow:
            fast = fast.next
            slow = slow.next
        
        if meet:
            return fast
        
        return None
        
#         sett = set()
        
#         cur = head
#         while cur:
#             if cur in sett:
#                 return cur
#             sett.add(cur)
#             cur = cur.next
            
#         return None