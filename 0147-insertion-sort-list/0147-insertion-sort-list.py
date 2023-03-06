# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head):

        Head = ListNode(0)
        Head.next = nodeToInsert = head
        
        while head and head.next:
            if head.val > head.next.val:

                nodeToInsert = head.next

                nodeToInsertPre = Head
                while nodeToInsertPre.next.val < nodeToInsert.val:
                    nodeToInsertPre = nodeToInsertPre.next
                    
                head.next = nodeToInsert.next

                nodeToInsert.next = nodeToInsertPre.next
                nodeToInsertPre.next = nodeToInsert
            else:
                head = head.next
            
        return Head.next