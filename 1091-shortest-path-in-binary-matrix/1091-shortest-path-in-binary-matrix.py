class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        level = 0
        q = deque([((0,0),1)])
        visited = set()
        n = len(grid)
        
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        
        while q:
            node,level = q.popleft()
            
            if node == (n-1,n-1):
                return level
            
            if node in visited:
                continue
                
            visited.add(node)
            enum = [-1,0,1]
            
            for i in range(3):
                for j in range(3):
                    if enum[i]==0 and enum[j]==0:
                        continue
                        
                    row = node[0]+enum[i]
                    col = node[1]+enum[j]
                    
                    if row>=0 and row<n and col>=0 and col<n:
                        neighbour = grid[row][col]

                        if neighbour == 0 and (row,col) not in visited:
                            q.append(((node[0]+enum[i],node[1]+enum[j]),level+1))
                
        return -1
                    