# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        parts = [[]]
        arr = []
        current = head
        origK = k
        while current:
            arr.append(current.val)
            current = current.next
       
        size = len(arr)
        cut = ceil(size/k)
        tmpSize = size
        for i in range(size):
            parts[-1].append(arr[i])
            if len(parts[-1]) == cut:
                tmpSize -= cut
                k -= 1
                cut = ceil(tmpSize/max(k,1))
                if len(parts) < origK:
                    parts.append([])
                
        while len(parts) < origK:
            parts.append([])

        ansParts = []
        for part in parts:
            ansParts.append(self.generateLL(part))
            
        return ansParts
    
    def generateLL(self,arr):
        if len(arr) == 0:
            return None
        
        head = ListNode(arr[0])
        current = head
        i = 1
        while i < len(arr):
            current.next = ListNode(arr[i])
            current = current.next
            i += 1
            
        return head