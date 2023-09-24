class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        cols = len(grid[0])
        grid.append([0]*cols)
        rows = len(grid)
        ballPos = {(0,i):i for i in range(cols)}
        for row in range(rows):
            for col in range(cols):
                if (row, col) in ballPos:
                    ball = ballPos[(row, col)]
                    if col == 0:
                        if grid[row][col] == 1 and col<cols-1 and grid[row][col+1] == 1:
                            ballPos[(row+1, col+1)] = ball
                            
                    elif col == cols-1:
                        if grid[row][col] == -1 and col>0 and grid[row][col-1] == -1:
                            ballPos[(row+1,col-1)] = ball
                            
                    else:
                        if grid[row][col] == 1 and col<cols-1 and grid[row][col+1] == 1:
                            ballPos[(row+1,col+1)] = ball
                            
                        if grid[row][col] == -1 and col>0 and grid[row][col-1] == -1:
                            ballPos[(row+1,col-1)] = ball
                            
        ans = [-1]*cols
        for i in range(cols):
            if (rows-1,i) in ballPos:
                ans[ballPos[(rows-1,i)]] = i
                
        return ans