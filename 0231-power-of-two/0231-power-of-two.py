class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==2 or n==1:
            return True
        
        if n<2 or n%2!=0:
            return False
        
        return self.isPowerOfTwo(n/2)