# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nums = []
        
        for ll in lists:
            head = ll
            while head:
                heapq.heappush(nums,head.val)
                head = head.next
           
        head = None
        if nums:
            head = ListNode(heapq.heappop(nums))
            cur = head
            while nums:
                cur.next = ListNode(heapq.heappop(nums))
                cur = cur.next

        return head