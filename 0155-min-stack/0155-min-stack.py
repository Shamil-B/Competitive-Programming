class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MinStack:

    def __init__(self):
        self.head = None
        self.minStack = None

    def push(self, val: int) -> None:
        node1 = Node(val)
        node2 = Node(val)
        
        if not self.minStack or val <= self.minStack.val:
            node2.next = self.minStack
            self.minStack = node2
            
            
        node1.next = self.head
        self.head = node1

    def pop(self) -> None:
        
        if self.head.val == self.minStack.val:
            self.minStack = self.minStack.next

        
        self.head = self.head.next
        
    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.minStack.val
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()