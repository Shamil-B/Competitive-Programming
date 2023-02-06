# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # for n//k times we call reverseLinkedList giving it head and tail
        # then add it between start and end node for each k group
        
        dummy = ListNode(-1,head)
        cur = head
        count  = 0
        start = dummy
        end = dummy
        
        while cur:
            if count == k:
                new = self.reverseLinkedList(start.next,end)
                start.next = new
                curr = new
                while curr.next:
                    curr = curr.next

                curr.next = cur
                start = curr
                count = 0
                
            count += 1
            end = cur
            cur = cur.next

        if count == k:
                new = self.reverseLinkedList(start.next,end)
                start.next = new
                curr = new
                while curr.next:
                    curr = curr.next

                curr.next = cur
            
        

        return dummy.next
    
    def reverseLinkedList(self,head,tail):
        #reverse the linked list
        current = head
        cur = head 
        while cur:
            if cur==tail:
                cur.next = None
                break
                
            cur = cur.next
        
        if not head:
            return 
            
        elif head.next:
            current = head.next 

        else:
            return head        
        
        new = ListNode(head.val)
        current2 = head
        
        while current:

            current2 = ListNode(current.val)
            current2.next = new
            new = current2
            current = current.next
            
            
            
        newHead = current2
        return (newHead)
    