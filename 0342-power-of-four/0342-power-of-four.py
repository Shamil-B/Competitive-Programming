class Solution:
    def isPowerOfFour(self, n: int,start=True) -> bool:
        if start and n==1:
            return True
        
        if n <= 4:
            if n == 4:
                return True
            
            return False
        
        
        return self.isPowerOfFour(n/4,False)