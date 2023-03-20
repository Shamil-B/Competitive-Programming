class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        newGraph = {}
        dst = len(graph)-1
        paths = []
        for i in range(len(graph)):
            newGraph[i] = graph[i]

        def allPaths(path,node):
            if node == dst:
                paths.append(path+[node])
                return
            
            path.append(node)
            for neig in newGraph[node]:
                allPaths(path[:],neig)
                
        allPaths([],0)
        return paths