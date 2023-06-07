class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        dic = {"000":0,"001":1,"010":1,"011":0,"100":1,"101":0,"110":2,"111":0}
        
        num = max(a,b,c)
        i = 0
        flips = 0
        while num:
            val = str(1&(a>>i))+str(1&(b>>i))+str(1&(c>>i))
            flips += dic[val]
            num >>= 1
            i+=1
            
        return flips