# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #The straightforward way
        res = []
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
            
        cur = head

        for i in range(n):
            if i < n//2:
                res.append(cur.val)
                
            else:
                res[n-i-1] += cur.val
                
            cur = cur.next
                
        return max(res)
            
        