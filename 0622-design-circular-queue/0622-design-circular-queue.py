class MyCircularQueue:

    def __init__(self, k: int):
        self.que = [-1]*k
        self.front = 0
        self.rear = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.que[self.rear%self.k] = value
            self.rear += 1
            return True

        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.que[self.front%self.k] = -1
            self.front += 1
            return True

    def Front(self) -> int:
        return self.que[self.front%self.k]

    def Rear(self) -> int:
        rear = self.rear-1 if self.rear >0 else 0
        if not self.isEmpty():
            return self.que[(rear)%self.k]
        
        return -1

    def isEmpty(self) -> bool:
        return (self.front == self.rear)

    def isFull(self) -> bool:
        return self.front+self.k == self.rear


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()