class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        #construct the graph
        graph = {}
        n = len(edges)
        
        for pre,after in enumerate(edges):
            if pre not in graph:
                if after==-1:
                    graph[pre] = []
                else:
                    graph[pre] = [after]
                
                
            elif after!=-1:
                graph[pre].append(after)

        #do the khans bfs algorithm on it

        preq = {}
        nonStarters = set()
        for key in graph.keys():
            for item in graph[key]:
                nonStarters.add(item)
                if item in preq:
                    preq[item] += 1
                else:
                    preq[item] = 1
                    
        starters = []
        for i in range(n):
            if i not in nonStarters:
                starters.append(i)
                
        q = deque(starters)
        stack = set()
        while q:
            node = q.popleft()
            stack.add(node)
            if node in graph:
                for neig in graph[node]:
                    preq[neig] -= 1
                    if preq[neig]==0:
                        q.append(neig)
                    
        remaining = []
        for i in range(n):
            if i not in stack:
                remaining.append(i)
                
        #the remaining elements are cycles therefore do dfs to find the maximum depth meaning the longest cycle's length
        self.explored = set()
        maxDepth = -1
        for num in remaining:
            if num not in self.explored:
                maxDepth = max(maxDepth,self.maxDepthDfs(graph,num))
            
        return maxDepth
    
    
    def maxDepthDfs(self,graph,num):
        visited = set()
        stack = [(num,0)]
        maxDepth = 0
        
        while stack:
            node,depth = stack.pop()
            maxDepth = max(depth,maxDepth)

            if node in visited:
                continue
                
            visited.add(node)
            self.explored.add(node)
            for neig in graph[node]:
                stack.append((neig,depth+1))


        return maxDepth
                
                
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
