class Solution:
    def findFarmland(self, grid):
        self.res=[]
        
        n=len(grid)
        
        m=len(grid[0])
        
        def helper(i,j,grid):
            if  i<0 or j<0 or j>=len(grid[0]) or i>=len(grid) or grid[i][j]==0:
                return (0,0)

            (num1,num2)=(i,j)
            grid[i][j]=0

            for x,y in [(1,0),(0,1)]:
                (num1,num2)=max((num1,num2),helper(i+x,j+y,grid))

            return (num1,num2)
                  
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    (x,y)=helper(i,j,grid)
                    self.res.append([i,j,x,y])

        return self.res