class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 0
        high = max(nums)+1
        
        while low < high-1:
            mid = low + (high-low)//2
            
            if self.divideAndSum(mid,nums) > threshold:
                low = mid
                
            else:
                high = mid
                
        if high == max(nums)+1:
            return high-1

        return high
        
    def divideAndSum(self,mid,nums):
        summ = 0

        for num in nums:
            summ = (summ+num//mid) if num//mid==num/mid else (summ+num//mid+1)

        return summ