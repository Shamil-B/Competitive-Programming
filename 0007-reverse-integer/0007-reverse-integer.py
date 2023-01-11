class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
                return 0
            
        if x > 0:
            res = ''
            for num in str(x):
                res = num + res
                
            
                
            ans = int(res)
        
        else:
            res = ''
            for num in str(x):
                res = num + res
                
            
                
            ans = int('-'+res[:-1])
        
        
        if ans > 2**31 or ans < -2**31:
            return 0
        
        return ans