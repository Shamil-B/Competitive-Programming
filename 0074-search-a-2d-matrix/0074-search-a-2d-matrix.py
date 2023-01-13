class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        left = 0
        right = m*n
        
        #first we assume that we have changed the matrix to a one dimensional array
        #and we will be doing binary search on this array but the elements will be
        #from the matrix 
        
        
        while True:
            mid = (right+left)//2
            
            row = mid//n
            col = mid%n
            
            currNum = matrix[row][col]
            
            if currNum == target:
                return True
            
            elif currNum < target:
                left = mid+1
                
            else:
                right = mid
                
            if right <= left:
                return False
        