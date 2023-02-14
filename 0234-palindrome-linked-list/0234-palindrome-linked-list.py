# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        arr = []
        
        while current:
            arr.append(current.val)
            current = current.next
            
        arr = reversed(arr)
        current = head
        
        for val in arr:
            if current.val != val:
                return False
            current = current.next
            
            
        return True
            
        