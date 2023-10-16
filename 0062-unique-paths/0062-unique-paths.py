class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def numericsSolution():
            ans = ((factorial((n+m-2)))//(factorial((n-1))*factorial((m-1))))
            return ans

        def topDownDP(cord=(0,0),memo={}):
            
            row,col = cord
            if row==m-1 and col==n-1:
                return 1

            ways = 0
            if (row,col) in memo:
                return memo[(row,col)]
            if row+1<m:
                ways+=topDownDP((row+1,col),memo)
                
            if col+1<n:
                ways += topDownDP((row,col+1),memo)
                
            memo[(row,col)] = ways
            return memo[(row,col)]
        
        # return topDownDP()

        #row wise
        def bottomUpDP():
            start = (m-1,n-1)
            dp = [[0 for i in range(n)] for i in range(m)]
            dp[-1][-1] = 1 
            
            
            for col in range(n-1,-1,-1):
                for row in range(m-1,-1,-1):
                    dp[row][col] += (self.calculate(row+1,col,m,n,dp)+self.calculate(row,col+1,m,n,dp))
                
            return dp[0][0]

        return numericsSolution()
    
    def calculate(self,x,y,m,n,dp):
        if 0<=x<m and 0<=y<n:
            return dp[x][y]
        return 0
