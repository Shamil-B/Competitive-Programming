class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesRow = []
        onesCol = []
        
        zerosRow = []
        zerosCol = []
        
        
        m = len(grid)
        n = len(grid[0])
        
        diff = [[0 for i in range(n)] for i in range(m)]

        for row in range(m):
            ones = 0
            for col in range(n):
                if grid[row][col] == 1:
                    ones+=1
                    
            onesRow.append(ones)
            zerosRow.append(n-ones)
            
        for col in range(n):
            ones = 0
            
            for row in range(m):
                if grid[row][col] == 1:
                    ones+=1
                    
            onesCol.append(ones)
            zerosCol.append(m-ones)
            
        for row in range(m):
            for col in range(n):
                diff[row][col] = onesRow[row] + onesCol[col] - zerosRow[row] - zerosCol[col]
                
                
        return diff
            
        
                