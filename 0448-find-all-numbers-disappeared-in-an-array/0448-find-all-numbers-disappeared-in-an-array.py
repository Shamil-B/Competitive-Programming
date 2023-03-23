class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        ind = 0
        n = len(nums)
        
        while ind<n:
            corPos = nums[ind]-1
            
            if corPos!=ind and nums[corPos] != nums[ind]:
                nums[corPos],nums[ind] = nums[ind],nums[corPos]

            else:
                ind += 1
                
        res = []
        for i in range(n):
            if i!=nums[i]-1:
                res.append(i+1)
                
        return res