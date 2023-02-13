# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        count = 0
        newHead = dummy
        
        cur = head.next
        while cur:
            if cur.val == 0:
                newHead.next = ListNode(count)
                count = 0
                newHead = newHead.next
                
            else:
                count += cur.val
                
            cur = cur.next
            
        return dummy.next