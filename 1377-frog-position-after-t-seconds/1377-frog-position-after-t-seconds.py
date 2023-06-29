class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = [[] for i in range(n+1)]
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        level = 0
        q = deque([(1,1,level)])
        visited = set([1])
        probs = [0 for i in range(n+1)]
        once = 1
        while q:
            
            node, prob, level = q.popleft()
            size = 0
            
            for neig in graph[node]:
                if neig not in visited:
                    size += 1

            if node == target:
                once -= 1
                if level == t or (size == 0 and level<t):
                    return prob
            
            if node == target and once < 0:
                continue

            for neig in graph[node]:
                if (neig not in visited) and size>0:
                    visited.add(neig)
                    q.append((neig,prob*(1/size),level+1))
                    
                    
        return 0