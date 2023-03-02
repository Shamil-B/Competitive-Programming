class Solution:
    def gridGame(self, grid) -> int:
        
        pfs1 = [grid[0][-1]]
        pfs2 = [grid[1][0]]
        n = len(grid[0])
        
        for i in range(1,n):
            pfs1.append(pfs1[i-1]+grid[0][n-1-i])
            
        for i in range(1,n):
            pfs2.append(pfs2[i-1]+grid[1][i])
            
        pfs1.reverse()
        result = []
        
        for i in range(n-1,-1,-1):
            if i<n-1:
                val1 = pfs1[i+1]
            else:
                val1 = 0
                
            if i>0:
                val2 = pfs2[i-1]
                
            else:
                val2 = 0
            result.append(max(val1,val2))
            
        return min(result)
            
            
#         cordinates1,res1 = self.gridGameCalculator(grid)
        
#         cordinates1.append((0,0))
#         cordinates1.append((-1,-1))

#         while cordinates1:
#             cor = cordinates1.pop()
#             grid[cor[0]][cor[1]] = 0
            
#         print(grid)
#         cordinates2,res2 = self.gridGameCalculator(grid)
#         return (res2)
    
#     def gridGameCalculator(self,grid,x=0,y=0,summ=0,changes=[],top=True):
#         if x==len(grid)-1 and y==len(grid[0])-1:
#             return (summ + grid[x][y])
        
#         if x == len(grid)-1:
#             summ += grid[x][y]
#             goRight = self.gridGameCalculator(grid,x,y+1,summ,changes,False)
#             return goRight
        
#         if y == len(grid[0])-1:
#             summ += grid[x][y]
#             goDown = self.gridGameCalculator(grid,x+1,y,summ,changes,False)
#             return goDown

#         summ += grid[x][y]
#         goRight = self.gridGameCalculator(grid,x,y+1,summ,changes,False)
#         goDown = self.gridGameCalculator(grid,x+1,y,summ,changes,False)

#         if goRight>goDown:
#             changes.append((x,y+1))
#         else:
#             changes.append((x+1,y))

#         if top:
            

#             tmp = changes.copy()
#             while changes:
#                 changes.pop()

#             return tmp,max(goRight,goDown)
#         print(goRight,goDown)
#         return max(goRight,goDown)