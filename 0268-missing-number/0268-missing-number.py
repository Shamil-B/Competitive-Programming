class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums += [-1]
        
        ind = 0
        n = len(nums)
        misInd = 0
        while ind<n:
            corPos = nums[ind]
            
            if corPos != ind and nums[ind] !=-1:
                nums[corPos],nums[ind] = nums[ind],nums[corPos]
                
            elif nums[ind] == -1:
                misInd = ind
                ind += 1

            else:
                ind += 1

        return misInd
                