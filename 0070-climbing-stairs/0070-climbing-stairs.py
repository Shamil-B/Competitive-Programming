class Solution:
    def climbStairs(self, n: int) -> int:
        self.n = n
        self.ways = 0
        def solve(s,memo={}):
            if s<2:
                self.ways+=1
                memo[s] = self.ways
                return
            
            if s in memo:
                self.ways += memo[s]
                return
            
            solve(s-1,memo)
            solve(s-2,memo)
            memo[s] = self.ways


        solve(n)
        return self.ways