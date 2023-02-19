# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        
        cur1 = firstOdd = head
        cur2 = firstEven = head.next
        index = 2
        
        cur = head.next.next
        while cur:
            if index%2==0:
                cur1.next = cur
                cur1 = cur1.next
                
            else:
                cur2.next = cur
                cur2 = cur2.next
            
            index += 1
            cur = cur.next
            
            
        cur2.next = None
        cur1.next = firstEven
            
        return head