class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        graph = {}
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    graph[(i,j)] = []
                    if i>0 and grid[i-1][j]:
                        graph[(i,j)].append((i-1,j))
                    if j>0 and grid[i][j-1]:
                        graph[(i,j)].append((i,j-1))
                        
                    if i<n-1 and grid[i+1][j]:
                        graph[(i,j)].append((i+1,j))
                        
                    if j<m-1 and grid[i][j+1]:
                        graph[(i,j)].append((i,j+1))
                    
        def dfs(node,graph,visited=None):
            if not visited:
                visited = set()
            
            self.explored.add(node)
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    dfs(neigh,graph,visited)

            return len(visited)

        max_ = 0  
        self.explored = set()
        for key in graph.keys():
            if key not in self.explored:
                res = dfs(key,graph)
                max_ = max(max_,res)
            
            
        return max_
            
        