class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #construct adjecency list
        
        newGraph = {}
        group = {}
        for index,neig in enumerate(graph):
            newGraph[index] = neig
            
        def dfs(node,visited=None):
            if not visited:
                visited = set()
                
            if node in visited:
                return True
            
            visited.add(node)
            self.explored.add(node)
            if node not in group:
                group[node] = True

            for neig in newGraph[node]:
                if neig not in group:
                    group[neig] = not group[node]
                    if not dfs(neig,visited):
                        return False
                    else:
                        continue
                    
                elif group[neig] == group[node]:
                    return False
                
                if not dfs(neig,visited):
                    return False
                    
            return True
        
        self.explored = set()
        for index in newGraph.keys():
            if index not in self.explored:
                if not dfs(index):
                    return False

        return True
            
            
            