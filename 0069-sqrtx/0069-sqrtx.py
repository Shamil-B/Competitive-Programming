class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        
        if x == 1:
            return 1
        
        while low < high-1:
            mid = (low + (high-low)//2)
            
            if mid**2 > x:
                high = mid
                
            elif mid**2 < x:
                low = mid
                
            else:
                return mid
            
            
        return low