class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # (m-1 to 0) for row and (0,1) to (n-1) for col
        
        row = m-1
        
        while row >= 0:
            i = row
            j = 0
            if i<m and j<n:
                elem = matrix[i][j]
            
            while i < m and j < n:
                if elem != matrix[i][j]:
                    return False
                
                i += 1
                j += 1
                
        
            row -= 1
            
        col = 1
        
        while col < n:
            i = 0
            j = col
            if i<m and j<n:
                elem = matrix[i][j]
            
            while i < m and j < n:
                if elem != matrix[i][j]:
                    return False
                
                i += 1
                j += 1
                
        
            col += 1
            
        return True