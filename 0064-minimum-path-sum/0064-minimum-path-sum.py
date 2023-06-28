class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        def getDown(cord):
            if cord[0]<len(grid)-1:
                return (grid[cord[0]+1][cord[1]])
            
            return -1
        
        def getRight(cord):
            if cord[1]<len(grid[0])-1:
                return (grid[cord[0]][cord[1]+1])
            
            return -1
        
        # bottom up
       
        for row in range(len(grid)-1,-1,-1):
            for col in range(len(grid[0])-1,-1,-1):

                down = getDown((row,col))
                right = getRight((row,col))

                if down != -1 and right != -1:
                    grid[row][col] += min(down,right)

                elif down != -1:
                    grid[row][col] += down

                elif right != -1:
                    grid[row][col] += right
             
        return grid[0][0]

            
            
            
            
        