class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        
        if n < 2*k+1:
            return [-1]*n

        avgs = [-1]*k
        sum_ = 0
        i = 0

        while i < n:
            if i < 2*k+1:
                sum_ += nums[i]
                
            else:
                avgs.append(sum_//(2*k+1))
                sum_ += nums[i]
                sum_ -= nums[i-(2*k+1)]
                
            i += 1
    
        avgs.append(sum_//(2*k+1))
        return avgs + [-1]*k