class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        # top down
        rows = len(matrix)
        cols = len(matrix[0])

        def topDown(i,j):
            
            if i >= rows or j >= cols or i < 0 or j < 0:
                return inf

            if i == rows-1:
                return matrix[i][j]
            
            state = (i,j)
            if state not in memo:
                res = min(topDown(i+1,j-1),topDown(i+1,j),topDown(i+1,j+1))
                memo[state] = matrix[i][j] + res

            return  memo[state]

        # bottom up
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

        min_ = inf
        memo = {}
        for col in range(cols):
            curRes = topDown(0,col)

            min_ = min(min_,curRes)
            
        return min_