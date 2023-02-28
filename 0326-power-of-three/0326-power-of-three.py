class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n<=3:
            if n==3 or n==1:
                return True 
            
            return False
        
        return self.isPowerOfThree(n/3)