class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        return (high-low+1)//2 + min(high%2,low%2)