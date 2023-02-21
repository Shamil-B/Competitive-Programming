# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        newCur = newDummy = ListNode(-1)
        rem = 0
        
        while cur1 and cur2:
            
            q = ((cur1.val+cur2.val+rem)%10)
            rem = (cur1.val+cur2.val+rem)//10
            node = ListNode(q)
            newCur.next = node
            newCur = newCur.next
            cur1 = cur1.next
            cur2 = cur2.next
            
        while cur1:
            q = ((cur1.val+rem)%10)
            rem = (cur1.val+rem)//10
            node = ListNode(q)
            newCur.next = node
            newCur = newCur.next
            cur1 = cur1.next
            
        while cur2:
            q = ((cur2.val+rem)%10)
            rem = (cur2.val+rem)//10
            node = ListNode(q)
            newCur.next = node
            newCur = newCur.next
            cur2 = cur2.next
            
        if rem:
            newCur.next = ListNode(rem)
        
        return newDummy.next
        
#         num1 = num2 = ""
        
#         cur1 = l1
#         cur2 = l2
        
#         while cur1:
#             num1 = str(cur1.val) + num1
#             cur1 = cur1.next
            
#         while cur2:
#             num2 = str(cur2.val) + num2
#             cur2 = cur2.next
        
#         summ = str(int(num1) + int(num2))
        
#         newHead = ListNode(int(summ[-1]))
#         cur = newHead
        
#         for i in range(len(summ)-2,-1,-1):
#             node = ListNode(summ[i])
#             cur.next = node
#             cur = cur.next
            
#         return newHead