# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        newHead = head
        
        cur = head.next
        while cur:
            if cur.val == 0:
                cur.val = count
                newHead.next = cur
                count = 0
                newHead = cur
                
            else:
                count += cur.val
                
            cur = cur.next
            
        return head.next