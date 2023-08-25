class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        @cache
        def solve(ind,steps):
            if steps == 0 and ind == 0:
                return 1
            if steps == 0 or ind < 0 or ind >= arrLen:
                return 0
            
            right = solve(ind+1,steps-1)
            stay = solve(ind,steps-1)
            left = solve(ind-1,steps-1)
            
            return right + left + stay
        
        return solve(0,steps)%(10**9+7)