class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        
        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1],succProb[i]))
            graph[edges[i][1]].append((edges[i][0],succProb[i]))
        
        # UCS
        fringe = [(-1,start)]
        heapq.heapify(fringe)
        visited = set()
        max_ = -inf
        
        while fringe:
            probSofar, node = heapq.heappop(fringe)

            if node == end:
                return probSofar*(-1)
            
            if node in visited:
                continue
                
            visited.add(node)
            for neig,neigProb in graph[node]:
                    heapq.heappush(fringe,(probSofar*neigProb,neig))
                  
        return 0
            