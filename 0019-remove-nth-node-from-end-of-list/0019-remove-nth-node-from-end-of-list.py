# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        
        cur = head
        
        while cur:
            size += 1
            cur = cur.next
            
        targetIndex = size - n
        
        cur = head
        dummy = ListNode(0,head)
        prev = dummy
        index = 0
        
        while cur:
            if index == targetIndex:
                prev.next = cur.next
                break
                
            index += 1
            prev = cur
            cur = cur.next
            
        return dummy.next