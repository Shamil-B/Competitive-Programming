class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = -1
        high = n
        
        while low<high-1:
            mid = low + (high-low)//2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                low = mid
                
            else:
                high = mid
        
        return high
        
        