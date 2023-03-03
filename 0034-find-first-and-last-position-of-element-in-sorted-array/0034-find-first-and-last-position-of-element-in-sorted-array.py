class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        low = -1
        high = n
        indices = []
        
        while low+1<high:
            mid = low + (high-low)//2
            
            if nums[mid] < target:
                low = mid
                
            else:
                high = mid
                
        if high == n:
            return [-1,-1]
        
        indices.append(high)
        
        low = -1
        high = n
        
        while low+1<high:
            mid = low + (high-low)//2
            
            if nums[mid] <= target:
                low = mid
                
            else:
                high = mid

        indices.append(high-1)
        
        if nums[indices[0]] != target or nums[indices[1]] != target:
            return [-1,-1]
        
        return indices