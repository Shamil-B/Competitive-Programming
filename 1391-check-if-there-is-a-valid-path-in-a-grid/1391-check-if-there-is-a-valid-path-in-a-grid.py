class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # do bfs until
        
        q = deque([(0,0)])
        visited = set()
        n = len(grid)
        m = len(grid[0])
        
        while q:
            cur = q.popleft()
            
            if cur==(n-1,m-1):
                return True
            
            if cur in visited:
                continue

            row,col = cur
            visited.add(cur)
            if grid[row][col]==2:
                # up
                if row>0:
                    neigStreet = grid[row-1][col]
                    if neigStreet == 2 or neigStreet == 3 or neigStreet == 4: 
                        q.append((row-1,col))
                    
                # down
                if row<n-1:
                    neigStreet = grid[row+1][col]
                    if neigStreet == 2 or neigStreet == 5 or neigStreet == 6: 
                        q.append((row+1,col))
                    
            if grid[row][col]==1:
                # left
                if col>0:
                    neigStreet = grid[row][col-1]
                    if neigStreet == 1 or neigStreet == 4 or neigStreet == 6: 
                        q.append((row,col-1))
                    
                # right
                if col<m-1:
                    neigStreet = grid[row][col+1]
                    if neigStreet == 1 or neigStreet == 3 or neigStreet == 5: 
                        q.append((row,col+1))
                    
                    
            if grid[row][col]==3:
                # down
                if row<n-1:
                    neigStreet = grid[row+1][col]
                    if neigStreet == 2 or neigStreet == 5 or neigStreet == 6: 
                        q.append((row+1,col))
                    
                # left
                if col>0:
                    neigStreet = grid[row][col-1]
                    if neigStreet == 1 or neigStreet == 4 or neigStreet == 6: 
                        q.append((row,col-1))
                    
                    
            if grid[row][col]==4:
                # right
                if col<m-1:
                    neigStreet = grid[row][col+1]
                    if neigStreet == 1 or neigStreet == 3 or neigStreet == 5: 
                        q.append((row,col+1))
                    
                # down
                if row<n-1:
                    neigStreet = grid[row+1][col]
                    if neigStreet == 2 or neigStreet == 5 or neigStreet == 6: 
                        q.append((row+1,col))
                    
            if grid[row][col]==5:
                # left
                if col>0:
                    neigStreet = grid[row][col-1]
                    if neigStreet == 1 or neigStreet == 4 or neigStreet == 6: 
                        q.append((row,col-1))
                    
                # up
                if row>0:
                    neigStreet = grid[row-1][col]
                    if neigStreet == 2 or neigStreet == 3 or neigStreet == 4: 
                        q.append((row-1,col))
                    
                    
            if grid[row][col]==6:
                # up
                if row>0:
                    neigStreet = grid[row-1][col]
                    if neigStreet == 2 or neigStreet == 3 or neigStreet == 4: 
                        q.append((row-1,col))
                    
                #right
                if col<m-1:
                    neigStreet = grid[row][col+1]
                    if neigStreet == 1 or neigStreet == 3 or neigStreet == 5: 
                        q.append((row,col+1))
                    

        return False