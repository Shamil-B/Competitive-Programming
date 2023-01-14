class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = []
        cols = []
        
        m = len(matrix)
        n = len(matrix[0])
        
        for row in range(m):
            for col in range(n):
                
                if matrix[row][col] == 0:
                    rows.append(row)
                    cols.append(col)
                    
        
        for row in rows:
            matrix[row] = [0]*n
            
        for col in cols:
            for row in range(m):
                matrix[row][col] = 0
        
           
        return matrix