class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(list)
        for ind,route in enumerate(routes):
            for i in range(len(route)):
                graph[route[i]].append(ind)
                
        q = deque([(source,0)])
        visited = set()
        
        while q:
            cur, stops = q.popleft()
            
            if cur == target:
                return stops
 
            for i in graph[cur]:
                if i not in visited:
                    visited.add(i)
                    for neig in routes[i]:
                        if neig != cur:
                            q.append((neig,stops+1))

        return -1