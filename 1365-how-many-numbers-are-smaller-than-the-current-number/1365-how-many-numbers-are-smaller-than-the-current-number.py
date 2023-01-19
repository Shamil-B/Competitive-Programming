class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and nums[i]>nums[j]:
                    count += 1
                    
            res.append(count)
                
                
        return res
                    