class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        summ = 0
        
        
        for i in range(1,len(timeSeries)):
            diff = duration - (timeSeries[i] - timeSeries[i-1])
            
            if diff>0:
                summ += diff
                
        return len(timeSeries)*duration-summ