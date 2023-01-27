class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        
    def get(self, index: int) -> int:
        current = self.head
        count = 0
        while current:
            if count==index:
                return current.value
            current = current.next
            count += 1
            
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = self.tail = node
        
        else:
            node.next = self.head
            self.head = node
    
    
        
    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if not self.tail:
            self.head = self.tail = node
            
        else:
            tmp = self.tail
            self.tail = node
            tmp.next = self.tail

        
    def addAtIndex(self, index: int, val: int) -> None:
        current = self.head
        count = 0
        node = Node(val)
        
        if index==0:
            node.next = self.head
            self.head = node
            return
            
        
        while current and current.next:
            if count == index-1:
                cur = current.next
                current.next = node
                node.next = cur
                return None
                
            current = current.next
            count += 1
            
        if count == index-1:
            if self.tail:
                self.tail.next = node
                self.tail = node        
            
        

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return None
        
        current = self.head
        count = 0
        
        if index==0 and self.head:
            self.head = self.head.next
            return None
        
        while current and current.next:
            if count == index-1:
                if current.next.next:
                    current.next = current.next.next
                    return None
                
                self.tail = current
                current.next = None
                
            current = current.next
            count += 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)