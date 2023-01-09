class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.count = 0
        

    def consec(self, num: int) -> bool:
        count = self.count
        if num == self.value:
            count += 1
            
        else:
            count = 0
        
        if count >= self.k:
            self.count = count
            return True
        
        else:
            self.count = count
            return False
        

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)