# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:        
        cur = headA
        size1 = 0
        size2 = 0
        
        while cur:
            size1 += 1
            cur = cur.next
            
        cur = headB
        while cur:
            size2 += 1
            cur = cur.next
            
        if size1>size2:
            diff = size1-size2
            
            while diff>0:
                headA = headA.next
                diff -= 1
                
        else:
            diff = size2-size1
            
            while diff>0:
                headB = headB.next
                diff -= 1
                
        while headA != headB:
            
            if not headA or not headB:
                return None
            
            headA = headA.next
            headB = headB.next
            
        return headA
            
        return None