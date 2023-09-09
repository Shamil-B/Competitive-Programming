class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def solve(ind,sum_):
            if ind >= len(nums) and sum_ == target:
                return 1
            
            if ind >= len(nums):
                return 0
            
            return solve(ind+1,sum_+nums[ind]) + solve(ind+1,sum_-nums[ind])
        
        return solve(0,0)