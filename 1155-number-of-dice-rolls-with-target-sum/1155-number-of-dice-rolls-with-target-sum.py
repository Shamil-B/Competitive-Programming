class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        def dp(n,target):
            if target<=0:
                return 0

            if n == 1:
                if target <= k:
                    return 1

                else:
                    return 0   
                
            state = (n,target)
            
            if state not in memo:
                ways = 0
                for i in range(1,k+1):
                    ways += dp(n-1,target-i)
                    
                memo[state] = ways

            return memo[state]
        
        MOD = pow(10,9)+7
        memo = {}
        result = dp(n,target)

        return result%MOD