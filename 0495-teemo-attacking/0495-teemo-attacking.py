class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        summ = 0
        
        
        for i in range(1,len(timeSeries)):
            diff = timeSeries[i]-timeSeries[i-1]
            diff = duration-diff
            if diff>0:
                summ += diff
                
        print(len(timeSeries),duration,summ)
        return len(timeSeries)*duration-summ