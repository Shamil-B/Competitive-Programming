class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        def bfs(starters):
            level = 0
            q = deque(starters)
            rows = len(grid)
            cols = len(grid[0])
            
            while q:
                node,level,anotherIsland = q.popleft()
                row,col = node

                if node in visited:
                    continue
                    
                if anotherIsland and grid[row][col]==1 and ((row,col) not in firstIsland):
                    return level
                    
                visited.add(node)

                #up
                if row>0:
                    if grid[row-1][col]==0:
                        q.append(((row-1,col),level+1,True))

                    else:
                        q.append(((row-1,col),level,anotherIsland))

                #down
                if row<rows-1:
                    if grid[row+1][col]==0:
                        q.append(((row+1,col),level+1,True))

                    else:
                        q.append(((row+1,col),level,anotherIsland))

                #left
                if col>0:
                    if grid[row][col-1]==0:
                        q.append(((row,col-1),level+1,True))

                    else:
                        q.append(((row,col-1),level,anotherIsland))

                #right
                if col<cols-1:
                    if grid[row][col+1]==0:
                        q.append(((row,col+1),level+1,True))

                    else:
                        q.append(((row,col+1),level,anotherIsland))
                        
            return inf
                        
        min_ = float("inf")

        # find the first group with dfs
        firstIsland = set()
        for i in range(len(grid)):
            found = False
            for j in range(len(grid[0])):
                if grid[i][j]:
                    start = (i,j)
                    found = True
                    break
   
            if found:
                break

        q = [start]
        visited2 = set()
        rows = len(grid)
        cols = len(grid[0])

        while q:
            node = q.pop()
            if node in visited2:
                continue
                
            visited2.add(node)
            row, col = node
            if grid[row][col]:
                firstIsland.add(node)

            #up
            if row>0:
                if grid[row-1][col]==1:
                    q.append(((row-1,col)))

            #down
            if row<rows-1:
                if grid[row+1][col]==1:
                    q.append(((row+1,col)))

            #left
            if col>0:
                if grid[row][col-1]==1:
                    q.append(((row,col-1)))

            #right
            if col<cols-1:
                if grid[row][col+1]==1:
                    q.append(((row,col+1)))
                    
            

        visited = set()
        firstIsland = list(firstIsland)
        for i in range(len(firstIsland)):
                firstIsland[i] = (firstIsland[i],0,False)
                

        return bfs(firstIsland)
