class MyQueue:

    def __init__(self):
        self.stack = []
        self.pos = 0

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        tmpInd = self.pos
        self.pos += 1 
        return self.stack[tmpInd]

    def peek(self) -> int:
        return self.stack[self.pos]

    def empty(self) -> bool:
        return not (len(self.stack)-self.pos)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()