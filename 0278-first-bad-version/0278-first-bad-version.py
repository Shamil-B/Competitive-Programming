# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n
        
        while low < high-1:
            mid = low + (high-low)//2
            
            if isBadVersion(mid):
                high = mid
                
            else:
                low = mid
                
        return high