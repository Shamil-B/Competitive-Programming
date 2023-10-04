class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v,w))
            
        q = [(0,src,k+2)]
        visited = set()

        while q:
            costSofar, node, steps = heapq.heappop(q)
            
            if steps == 1 and node != dst:
                continue
                
            if node == dst:
                return costSofar
            
            state = (node,costSofar)
            if state in visited:
                continue
      
            visited.add(state)
            for neig, cost in graph[node]:
                heapq.heappush(q,(costSofar+cost,neig,steps-1))
                
        return -1