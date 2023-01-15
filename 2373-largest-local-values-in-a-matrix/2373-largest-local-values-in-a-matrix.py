class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = []
        
        for row in range(n-2):
            temp = []
            for col in range(n-2):
                maxx = 0
                for i in range(row,row+3):
                    for j in range(col,col+3):
                        maxx = max(maxx,grid[i][j])
                        
                temp.append(maxx)
            res.append(temp)
                
        return res
                        