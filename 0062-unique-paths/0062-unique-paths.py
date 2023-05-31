class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def solve(cord=(0,0),memo={}):
            
            row,col = cord
            if row==m-1 and col==n-1:
                return 1

            ways = 0
            if (row,col) in memo:
                return memo[(row,col)]
            if row+1<m:
                ways+=solve((row+1,col),memo)
                
            if col+1<n:
                ways += solve((row,col+1),memo)
                
            memo[(row,col)] = ways
            return memo[(row,col)]
        
        return solve()