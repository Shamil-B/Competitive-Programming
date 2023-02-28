class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        suffix = [nums[-1]]
        n = len(nums)
        total = 1
        res = []
        
        for i in range(1,n):
            prefix.append(nums[i]*prefix[i-1])
            
        for i in range(n-2,-1,-1):
            suffix.append(nums[i]*suffix[(n-2)-i])
        
        suffix.reverse()
        
        for i in range(n):
            val1 = prefix[i-1] if i > 0 else 1
            if i<n-1:
                val2 = suffix[i+1]
            else:
                val2 = 1
                
            res.append(val1*val2)
            
        return res