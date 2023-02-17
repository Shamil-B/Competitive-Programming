# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        start = left-2
        end = right
        dummy = ListNode(0,head)
        startNode = endNode = None
        
        cur = head
        index = 0
        if start == -1:
            startNode = dummy
            
        
        while cur:
            if index == start and startNode == None:
                startNode = cur

            if index == end:
                endNode = cur

            index += 1
            cur = cur.next
            
        newHead = startNode.next
        cur = newHead
        
        while cur.next:
            if cur.next == endNode:
                cur.next = None
                break
                
            cur = cur.next
                
        reversedPartsHead, tail = self.reverseLinkedList(newHead)
        
        startNode.next = reversedPartsHead
        tail.next = endNode
        
        return dummy.next
                
            
            
    def reverseLinkedList(self,head):
        dummy = ListNode(0,head)
        cur = head
        prev = dummy
        
        while cur:
            print(cur.val)
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
            
        newHead = prev
        cur = newHead
        dic = {}
        while cur.next:

            if cur.next == dummy:
                cur.next = None
                break
                
            cur = cur.next

        return newHead,head     
        