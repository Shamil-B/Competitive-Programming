class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seeker = nums[0]
        holder = 1
        
        for i in range (1,len(nums)):
            if nums[i]>seeker :
                seeker = nums[i]
                nums[holder] = seeker
                holder+=1
                
        return holder