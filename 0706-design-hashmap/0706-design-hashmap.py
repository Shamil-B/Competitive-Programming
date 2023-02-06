class MyHashMap:

    def __init__(self):
        self.hMap = []

    def put(self, key: int, value: int) -> None:
        if key+1 > len(self.hMap):
            self.hMap += [-1]*((key+1)-len(self.hMap))
            self.hMap[key] = value
            
        else:
            self.hMap[key] = value

    def get(self, key: int) -> int:
        if key<len(self.hMap):
            return self.hMap[key]
        
        return -1

    def remove(self, key: int) -> None:
        if key<len(self.hMap):
            self.hMap[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)