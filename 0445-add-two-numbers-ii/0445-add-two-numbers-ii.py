# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

                # I had a solution for the Add Two Numbers 1 and I combined that with the reverse function to solve this one
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = self.reverseList(l1)
        head2 = self.reverseList(l2)
        summ = self.addTwoNumbersHelper(head1,head2)
        
        return self.reverseList(summ)    
    
    
    def addTwoNumbersHelper(self, l1, l2):
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