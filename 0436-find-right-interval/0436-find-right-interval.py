class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        indices = {}
        
        for ind,inter in enumerate(intervals):
            indices[inter[0]] = ind
            
            
        intervals.sort()
        rIntervals = [-1]*n
        
        for ind,inter in enumerate(intervals):
            end = inter[1]
            #now we find bisect_left of end in the starts
            res = self.bisectLeft(intervals,end)

            if res!=-1:
                res = indices[intervals[res][0]]
            rIntervals[indices[inter[0]]] = res
            
        return rIntervals
    
    
    
    def bisectLeft(self,intervals,target):
        n = len(intervals)
        low = -1
        high = n
        
        while low+1 < high:
            mid = low + (high-low)//2
            
            if intervals[mid][0] < target:
                low = mid
                
            else:
                high = mid
                
                
        if high == n:
            return -1

        return high
        