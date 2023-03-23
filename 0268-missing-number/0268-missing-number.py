class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums += [-1]
        
        ind = 0
        n = len(nums)
        while ind<n:
            corPos = nums[ind]
            
            if corPos != ind and nums[ind] !=-1:
                nums[corPos],nums[ind] = nums[ind],nums[corPos]
                
            else:
                ind += 1
                
        misInd = 0
        for index,num in enumerate(nums):
            if num == -1:
                misInd = index
                
        return misInd
                