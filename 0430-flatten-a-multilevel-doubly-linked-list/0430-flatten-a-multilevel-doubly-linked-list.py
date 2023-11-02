class FlattenLinkedList:
    def __init__(self, head):
        self.head = head

    def solve(self, head):
        current =  head
        tail = current
        while current:
            tail = current
            if current.child:
                start = current
                end = current.next
                flattend_tail  = self.solve(current.child)

                # insert operation
                start.next = current.child
                flattend_tail.next = end
                if end:
                    end.prev = flattend_tail

                current.child.prev = start
                current.child = None

            current = current.next

        return tail

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]': 
        flatten = FlattenLinkedList(head)
        flatten.solve(flatten.head)
        return flatten.head