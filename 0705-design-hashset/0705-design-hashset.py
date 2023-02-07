class MyHashSet:

    def __init__(self):
        self.arr = []

    def add(self, key: int) -> None:
        if key >= len(self.arr):
            self.arr += [-1]*(key+1)
            
        self.arr[key] = 0

    def remove(self, key: int) -> None:
        if key < len(self.arr):
            self.arr[key] = -1
        

    def contains(self, key: int) -> bool:
        if key<len(self.arr) and self.arr[key] != -1:
            return True
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)