class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        limit = len(nums)
        for ind,num in enumerate(nums):
            
            if ind == limit:
                break
                
            tmp = str(num)
            revNum = ''
            
            for i in tmp:
                revNum = i + revNum

            nums.append(int(revNum))
            
            
        return len(set(nums))
    
   
        