# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n = 0
        intRes = 0
        sub = 0
        
        cur = head
        while cur:
            n += 1
            cur = cur.next
            
        cur = head
        i = 0
        while cur:
            if cur.val==0:
                sub += 2**(n-1-i)
            
            i += 1
            cur = cur.next
            
        return 2**n-1-sub