# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #The straightforward way
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
            
        cur = head

        for i in range(n):
            if i == n//2-1:
                break
            cur = cur.next
            
        cur.next = self.reverseList(cur.next)
        
        cur = cur.next
        cur2 = head
        maxx = 0
        while cur:
            maxx = max(maxx,cur.val+cur2.val)
            cur = cur.next
            cur2 = cur2.next
            
        return maxx
    
    def reverseList(self, head):
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
            
        