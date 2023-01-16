class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        mat = matrix.copy()
            
        res = []
        
        for col in range(n):
            newRow = []
            for row in range(n-1,-1,-1):
                newRow.append(mat[row][col])
                
            res.append(newRow)
            
            
        for row in range(n):
            for col in range(n):
                matrix[row][col] = res[row][col]
                
                
                
                
                
            