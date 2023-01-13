class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        size = len(nums)
        temp = []
        
        for i in range(size-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
                
                
        for num in nums:
            if num != 0:
                temp.append(num)
                
                
        return temp + [0]*(size-len(temp))