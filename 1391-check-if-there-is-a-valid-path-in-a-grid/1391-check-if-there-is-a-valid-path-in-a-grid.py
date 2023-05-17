class QuickUnion:
    def __init__(self,elements):
        self.reps = elements
        self.heights = {}

        for key in elements.keys():
            self.heights[key] = 1

    def findRep(self,x):
        rep = self.reps[x]
        
        while rep!=self.reps[rep]:
            rep = self.reps[rep]
            
        topParent = rep
        rep = self.reps[x]
        
        while rep!=self.reps[rep]:
            temp = rep
            rep = self.reps[rep]
            self.reps[temp] = topParent
            
        return topParent
    
    def union(self,x,y):
        oldRep = self.findRep(x)
        newRep = self.findRep(y)
        
        
        height1 = self.heights[oldRep]
        height2 = self.heights[newRep]

        newHeight = max(height1, height2)

        if height1>height2:
            newRep, oldRep = oldRep,newRep
            newHeight = max(height1, height2)
        
        if height1 == height2:
            newHeight = height1+1
            
        self.heights[newRep] = newHeight
        self.heights[oldRep] = -1
        
        self.reps[oldRep] = newRep
        
    def connected(self,x,y):
        return self.findRep(x) == self.findRep(y)

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # do bfs until
        
        q = deque([(0,0)])
        visited = set()
        n = len(grid)
        m = len(grid[0])
        
        elements = {}
        for i in range(n):
            for j in range(m):
                elements[(i,j)] = (i,j)
                
        uf = QuickUnion(elements)
                
        for i in range(n):
            for j in range(m):
                cur = (i,j)
                row,col = cur

                if grid[row][col]==2:
                    # up
                    if row>0:
                        neigStreet = grid[row-1][col]
                        if neigStreet == 2 or neigStreet == 3 or neigStreet == 4: 
                            uf.union(cur,(row-1,col))

                    # down
                    if row<n-1:
                        neigStreet = grid[row+1][col]
                        if neigStreet == 2 or neigStreet == 5 or neigStreet == 6: 
                            uf.union(cur,(row+1,col))

                if grid[row][col]==1:
                    # left
                    if col>0:
                        neigStreet = grid[row][col-1]
                        if neigStreet == 1 or neigStreet == 4 or neigStreet == 6: 
                            uf.union(cur,(row,col-1))

                    # right
                    if col<m-1:
                        neigStreet = grid[row][col+1]
                        if neigStreet == 1 or neigStreet == 3 or neigStreet == 5: 
                            uf.union(cur,(row,col+1))


                if grid[row][col]==3:
                    # down
                    if row<n-1:
                        neigStreet = grid[row+1][col]
                        if neigStreet == 2 or neigStreet == 5 or neigStreet == 6: 
                            uf.union(cur,(row+1,col))

                    # left
                    if col>0:
                        neigStreet = grid[row][col-1]
                        if neigStreet == 1 or neigStreet == 4 or neigStreet == 6: 
                            uf.union(cur,(row,col-1))


                if grid[row][col]==4:
                    # right
                    if col<m-1:
                        neigStreet = grid[row][col+1]
                        if neigStreet == 1 or neigStreet == 3 or neigStreet == 5: 
                            uf.union(cur,(row,col+1))

                    # down
                    if row<n-1:
                        neigStreet = grid[row+1][col]
                        if neigStreet == 2 or neigStreet == 5 or neigStreet == 6: 
                            uf.union(cur,(row+1,col))

                if grid[row][col]==5:
                    # left
                    if col>0:
                        neigStreet = grid[row][col-1]
                        if neigStreet == 1 or neigStreet == 4 or neigStreet == 6: 
                            uf.union(cur,(row,col-1))

                    # up
                    if row>0:
                        neigStreet = grid[row-1][col]
                        if neigStreet == 2 or neigStreet == 3 or neigStreet == 4: 
                            uf.union(cur,(row-1,col))


                if grid[row][col]==6:
                    # up
                    if row>0:
                        neigStreet = grid[row-1][col]
                        if neigStreet == 2 or neigStreet == 3 or neigStreet == 4: 
                            uf.union(cur,(row-1,col))

                    #right
                    if col<m-1:
                        neigStreet = grid[row][col+1]
                        if neigStreet == 1 or neigStreet == 3 or neigStreet == 5: 
                            uf.union(cur,(row,col+1))

        return uf.connected((0,0),(n-1,m-1))