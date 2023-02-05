# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n = 0
        intRes = 0
        
        cur = head
        while cur:
            n += 1
            cur = cur.next
            
        cur = head
        i = n-1
        while cur:
            intRes += (cur.val*(2**(i)))
            i -= 1
            cur = cur.next
            
        return intRes