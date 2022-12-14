class Solution:
    def findDiagonalOrder(self, mat):
        
        result = [mat[0][0]]
        m = len(mat)
        n = len(mat[0])
        upward = True
        row,col = 0,0
        
        for i in range(m*n-1):
            
            if upward:
                
                if col==n-1:
                    upward = False
                    row+=1

                elif row==0:
                    upward = False
                    col+=1
                    
                else:
                    col+=1
                    row-=1
            else:
                
                if row==m-1:
                    upward = True
                    col+=1

                elif col==0:
                    upward = True
                    row+=1
                    
                else:
                    col-=1
                    row+=1

            result.append(mat[row][col])
            
        return result
    
    