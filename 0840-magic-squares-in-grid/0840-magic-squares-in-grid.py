class Solution:
    def numMagicSquaresInside(self, grid):
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        
        for row in range(m-2):
            for col in range(n-2):
                mainSum = -1
                miniGrid = set()
                complete = True
                
                #first traverse through the rows while checking
        
                for i in range(row,row+3):
                    summ = 0
                    for j in range(col,col+3):
                        ele = grid[i][j]
                        summ += ele
                        if ele > 0 and ele < 10:
                            miniGrid.add(ele)
                        
                    if mainSum == -1:
                        mainSum = summ

                    else:
                        if mainSum != summ:
                            complete = False
                            break
                            
                            
                
                
                #then traverse through the columns while checking
                
                for j in range(col,col+3):
                    summ = 0
                    for i in range(row,row+3):
                        summ += grid[i][j]
                        
                    if mainSum == -1:
                        mainSum = summ

                    else:
                        if mainSum != summ:
                            complete = False
                            break
                            
                            
                
                    
                #then traverse through the forward diagonal while checking
                summ = 0
                j = col
                for i in range(row,row+3):
                    
                    summ += grid[i][j]
                    
                    j += 1
                        
                if mainSum == -1:
                    mainSum = summ

                else:
                    if mainSum != summ:
                        complete = False                            
                            
                
                    
                #then traverse through the backward diagonal while checking
                
                summ = 0
                j = col + 2
                for i in range(row,row+3):
                    
                    summ += grid[i][j]
                    
                    j -= 1
                        
                if mainSum == -1:
                    mainSum = summ

                else:
                    if mainSum != summ:
                        complete = False                            
                    
                    
                if len(miniGrid)==9 and complete:
                    count += 1
                                
        return count