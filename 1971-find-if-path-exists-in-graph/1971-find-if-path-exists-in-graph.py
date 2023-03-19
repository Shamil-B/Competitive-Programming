class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        
        for node in edges:
            if node[0] not in graph:
                 graph[node[0]] = [node[1]]
                    
                    
            else:
                 graph[node[0]].append(node[1])
                    
            if node[1] not in graph:
                 graph[node[1]] = [node[0]]
                    
                    
            else:
                 graph[node[1]].append(node[0])

        used = set()
        def hasPath(src,dst):
            if src in used:
                return

            used.add(src)
            if src == dst:
                return True
            
            for neighbour in graph[src]:
                if hasPath(neighbour,dst):
                    return True
                
            return False

        return hasPath(source,destination)