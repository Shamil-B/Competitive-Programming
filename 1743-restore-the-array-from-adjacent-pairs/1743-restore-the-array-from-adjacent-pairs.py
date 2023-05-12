class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        #construct the graph
        n = len(adjacentPairs)+1
        graph = {}
        
        for pre,after in adjacentPairs:
            if pre in graph:
                graph[pre].append(after)
            else:
                graph[pre] = [after]
                
            if after in graph:
                graph[after].append(pre)
            else:
                graph[after] = [pre]
                
            
        for key in graph.keys():
            if len(graph[key])==1:
                start = key
                break
                
        #dfs on the graph to construct the array
        resArr = []
        
        stack = [start]
        visited = set([start])
        
        while stack:
            curNum = stack.pop()
            resArr.append(curNum)
            for adjNum in graph[curNum]:
                if adjNum not in visited:
                    visited.add(adjNum)
                    stack.append(adjNum)
                    
        return resArr
