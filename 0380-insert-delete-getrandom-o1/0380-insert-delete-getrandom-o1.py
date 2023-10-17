class RandomizedSet:

    def __init__(self):
        self.list = [inf]
        self.indices = {}
        self.tail = 0
        

    def insert(self, val: int) -> bool:
        if val not in self.indices or self.indices[val] == inf:
            self.list.append(val)
            self.list[-1], self.list[self.tail] = self.list[self.tail], self.list[-1]
            self.tail += 1
            self.indices[val] = self.tail - 1
            return True
        
        return False

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False

        index = self.indices[val]
        self.list[index], self.list[self.tail-1] = self.list[self.tail-1], self.list[index]
        self.list[self.tail-1] = inf
        self.indices[self.list[index]] = index
        self.indices.pop(val)
        self.tail -= 1
        self.list.pop()
        return True

    def getRandom(self) -> int:
        rand_index = random.randint(0, self.tail-1)
        return self.list[rand_index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()