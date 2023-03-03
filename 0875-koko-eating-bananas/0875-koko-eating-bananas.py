class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        maxB = max(piles)
        low = 0
        high = maxB+1
        self.piles = piles
        
        while low+1<high:
            mid = low + (high-low)//2
            
            if self.isSafe(mid,h):
                high = mid
                
            else:
                low = mid

        print(low,high)
        if low == -1:
            return (piles[0]//h)+min(1,piles[0]%h)
        
        return high
        
        
        
    def isSafe(self,num,hours):
        count = 0
        
        for pile in self.piles:
            if num!=0:
                count += (pile//num+min(pile%num,1))
            
        return count <= hours