class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        size = len(nums)

        def dp(n):
            if n == size-1:
                return nums[n]
            
            if n == size-2:
                return max(nums[-1],nums[-2])
            
            if n not in memo:
                memo[n] = max(nums[n] + dp(n+2),dp(n+1))
                
            return memo[n]
        
        return dp(0)