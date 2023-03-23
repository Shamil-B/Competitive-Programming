class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ind = 0
        
        n = len(nums)
        
        while ind<n:
            corPos = nums[ind]-1
            if corPos!=ind and nums[corPos]!=nums[ind]:
                nums[corPos],nums[ind] = nums[ind],nums[corPos]
                
            else:
                ind += 1
               
        res = []
        for i in range(n):
            if nums[i]-1 != i:
                res.append(nums[i])
                
        return res