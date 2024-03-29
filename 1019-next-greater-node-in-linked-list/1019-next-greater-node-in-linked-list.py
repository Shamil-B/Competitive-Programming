# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head):
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next

        arr = [0]*size

        cur = head.next
        ind = 1
        stack = []
        stack.append(head.val)
        while cur :
            if len(stack)>0 and cur.val<=stack[-1]:
                stack.append(cur.val)
                cur = cur.next
                ind += 1

            else:
                if len(stack)==0:
                    stack.append(cur.val)

                tmp = ind
                while len(stack)>0 and cur.val>stack[-1]:
                    if arr[ind-1]==0:
                        arr[ind-1] = cur.val
                        stack.pop()
                    ind-=1
                ind = tmp
                ind+=1
                    
                stack.append(cur.val)

                cur = cur.next

        return arr