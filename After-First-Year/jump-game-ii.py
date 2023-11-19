class Solution:
    def jump(self, nums: List[int]) -> int:
        size = len(nums)

        @cache
        def solve(ind):
            if ind == size-1:
                return 0
            
            # now we iterate through our options
            min_ = size
            for i in range(ind+1,min(ind + nums[ind]+1,size)):
                min_ = min(min_,solve(i))
                
            return min_ + 1
        
        return solve(0)