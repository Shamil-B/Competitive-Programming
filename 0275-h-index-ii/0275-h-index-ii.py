class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        low = -1
        high = n
        
        while low+1<high:
            mid = low + (high-low)//2
            
            if citations[mid] >= n-mid:
                high = mid
                
            else:
                low = mid
                
        return n-high