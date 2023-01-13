class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])
        newMat = [[0]*c for i in range(r)]
        
        if r*c != m*n:
            return mat
        
        uInd = 0
        
        for row in range(r):
            for col in range(c):
                r1 = uInd//n
                c1 = uInd%n
                
                newMat[row][col] = mat[r1][c1]
                
                uInd += 1
                
                
        return newMat