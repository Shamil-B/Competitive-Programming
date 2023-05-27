class Solution:
    def tribonacci(self, n: int) -> int:
        def solve(n,memo={}):
            if n==0:
                return 0
            if n<3:
                return 1
            
            if n in memo:
                return memo[n]
            
            
            memo[n] = solve(n-1,memo)+solve(n-2)+solve(n-3,memo)
            return memo[n]
        
        return solve(n)