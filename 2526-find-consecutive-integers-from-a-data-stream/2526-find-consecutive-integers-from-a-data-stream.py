class DataStream:

    def __init__(self, value: int, k: int):
        self.value = [value,k,0]
       
        

    def consec(self, num: int) -> bool:
        value = self.value
        if num == value[0]:
            value[2] += 1
            
        else:
            value[2] = 0
        
        if value[2] >= value[1]:
            self.value = value
            return True
        
        else:
            self.value = value
            return False
        

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)