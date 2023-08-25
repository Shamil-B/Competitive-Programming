class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
         
        @cache
        def solve(ind,steps):
            if steps == 0 and ind == endPos:
                return 1

            if steps == 0:
                return 0
            
            right = solve(ind+1,steps-1)
            left = solve(ind-1,steps-1)
            
            return right + left
        
        return solve(startPos,k)%(10**9+7)