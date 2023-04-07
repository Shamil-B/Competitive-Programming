class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        newGrid = [[0 for i in range(len(grid[0]))] for i in range(n)]
        for row in range(n):
            for col in range(len(grid[0])):
                neighbours = 0
                if grid[row][col]:
                    neighbours = (grid[row-1][col] if row>0 else 0) + (grid[row][col-1] if col>0 else 0) + (grid[row+1][col] if row<n-1 else 0)+(grid[row][col+1] if col<len(grid[0])-1 else 0)
                    
                newGrid[row][col] = neighbours
        
        perimeter = 0
        print(newGrid)
        for row in range(n):
            for col in range(len(grid[0])):
                sides = newGrid[row][col]
                if grid[row][col]:
                    perimeter += (4-sides)

        return perimeter
                    