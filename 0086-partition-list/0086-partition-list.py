# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        
        current = head
        found = False
        
        while current:
            if current.val >= x:
                found = True
            current = current.next
            
        if not found:
            return head
        
        cur = dummy.next
        prev = dummy
        p1 = dummy
        
        while cur:
            nextNode = cur.next
            if cur.val < x and (cur == head or cur == p1.next):
                p1 = prev = cur
                
            elif cur.val < x:
                #first we remove it
                prev.next = cur.next
                
                #then add it after p1 
                
                
                temp = p1.next
                p1.next = cur
                cur.next = temp
                
                #update p1
                p1 = cur
                
            else:
                prev = cur
                
            cur = nextNode
            
        return dummy.next

            
        
        print(les,grt,res)
        return head