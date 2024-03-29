# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
#         sett = set()
        
#         cur = head
        
#         while cur:
#             if cur in sett:
#                 return True
#             sett.add(cur)
#             cur = cur.next
            
#         return False



          slow = fast = head
          index = 0
          while fast and fast.next:
            if fast==slow and index!=0:
                return True
            
            fast = fast.next.next
            slow = slow.next
            index+=1
            
          return False
            
            