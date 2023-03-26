class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num))==1:
            return int(num)
        
        ls = list(map(int,list(str(num))))
        return self.addDigits(sum(ls))