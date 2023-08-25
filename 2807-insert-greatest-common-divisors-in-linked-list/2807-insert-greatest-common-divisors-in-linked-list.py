# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        cur = head
        
        while cur.next:
            gcd = self.gcd(cur.val,cur.next.val)
            nextNode = cur.next
            cur.next = ListNode(gcd)
            cur.next.next = nextNode
            cur = nextNode

        return head

    def gcd(self,a, b):
            while b:
                a, b = b, a % b
            return a
