class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)-1
        totalSum = sum(weights)
        high = totalSum+1
        
        while low+1 < high:
            
            capacity = low + (high-low)//2
            if self.amountOfDays(weights,capacity) > days:
                low = capacity
                
            else:
                high = capacity
             
        if high == totalSum+1:
            return low
        
        return high
    
    def amountOfDays(self,weights,capacity):
        days = 0
        curSum = 0
        for weight in weights:
            if curSum+weight>capacity:
                days += 1
                curSum = weight
                
            else:
                curSum += weight
                
        if curSum <= capacity:
            days+=1
        
        return days