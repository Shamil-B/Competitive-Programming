class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            counter = 0
            num = i
            while num!=0:
                if num&1:
                    counter+=1
                num = num>>1
                
            res.append(counter)
            
        return res
    
#         res = []
#         for i in range(n+1):
#             res.append(Counter(bin(i)[2:])["1"])
            
#         return res
                