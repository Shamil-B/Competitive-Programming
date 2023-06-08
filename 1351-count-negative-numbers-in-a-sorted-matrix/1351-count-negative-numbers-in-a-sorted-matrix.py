class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        negs = 0
        for row in range(rows-1,-1,-1):
            for col in range(cols-1,-1,-1):
                if grid[row][col]<0:
                    negs += 1
                    
                else:
                    break
                    
        return negs