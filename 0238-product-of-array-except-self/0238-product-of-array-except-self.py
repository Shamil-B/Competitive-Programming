class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = []
        res = []
        n = len(nums)
        total = 1
        
        for i in range(n):
            if nums[i] == 0:
                zeros.append(i)
            else:
                total *= nums[i]
                
                
        if len(zeros)>1:
            res = [0]*n
            
        elif len(zeros) == 1:
            for num in nums:
                if num == 0:
                    res.append(total)
                else:
                    res.append(0)
                
        else:
            for num in nums:
                res.append(total//num)
                
        return res