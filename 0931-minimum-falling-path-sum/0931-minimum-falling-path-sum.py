class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        def getDown(cord):
            if cord[0]<len(matrix)-1:
                return (matrix[cord[0]+1][cord[1]])
            
            return inf
        
        def getRightDown(cord):
            if cord[0]<len(matrix)-1 and cord[1]<len(matrix[0])-1:
                return (matrix[cord[0]+1][cord[1]+1])
            
            return inf
        
        def getLeftDown(cord):
            if cord[0]<len(matrix)-1 and cord[1]>0:
                return (matrix[cord[0]+1][cord[1]-1])

            return inf
        
        def bottomUp():
            for row in range(len(matrix)-1,-1,-1):
                for col in range(len(matrix[0])-1,-1,-1):

                    down = getDown((row,col))
                    rightDown = getRightDown((row,col))
                    leftDown = getLeftDown((row,col))
                    
                    
                    min_ = min(down,rightDown,leftDown)

                    if min_ != inf:
                        matrix[row][col] += min_

            return min(matrix[0])

        return bottomUp()