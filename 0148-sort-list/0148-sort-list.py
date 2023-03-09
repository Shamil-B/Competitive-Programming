# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        def mergeSort(head):
            if not head:
                return
            
            if head and not head.next:
                return head
            
            #we find mid
            left = head
            
            slow = head
            fast = head
            prev = None
            while fast and fast.next:
                fast = fast.next.next
                prev = slow
                slow = slow.next

            right = slow
            prev.next = None
            
            return self.mergeTwoLists(mergeSort(left),mergeSort(right))
        
        
        return mergeSort(head)
        
        
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        merged = dummy
        ptr1 = ptr = 0
        cur1 = list1
        cur2 = list2
        
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                merged.next = cur1
                cur1 = cur1.next
                
            else:
                merged.next = cur2
                cur2 = cur2.next
                
            merged = merged.next
            
        while cur1:
            merged.next = cur1
            cur1 = cur1.next
            merged =merged.next
            
        while cur2:
            merged.next = cur2
            cur2 = cur2.next
            merged = merged.next
            
        return dummy.next

