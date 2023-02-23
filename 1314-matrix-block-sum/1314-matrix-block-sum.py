class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        pSum = [[0]*(len(mat[0])+1)]
        finalSum = []
        
        for r in range(len(mat)):
            pSum.append([0])
            for c in range(len(mat[0])):
                curVal = mat[r][c] 
                befCol = pSum[r+1][c]
                befRow = pSum[r][c+1]
                diag = pSum[r][c]
                
                curSum = curVal + befCol + befRow - diag
                pSum[-1].append(curSum)
                
        m,n = len(pSum),len(pSum[0])

        for r in range(1,len(pSum)):
            finalSum.append([])
            for c in range(1,len(pSum[0])):
                row1 = r-k 
                row2 = r+k 
                col1 = c-k 
                col2 = c+k 

                row2 = min(row2,m-1)
                col2 = min(col2,n-1)
                
                allSum = pSum[row2][col2]
                leftSum = pSum[row2][col1-1] if col1 > 0 and row2 < m else 0
                topSum = pSum[row1-1][col2]  if row1 > 0 and col2 < n else 0
                extraSum = pSum[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
                
                summ = allSum - leftSum - topSum + extraSum
                
                finalSum[-1].append(summ)
                
        return finalSum