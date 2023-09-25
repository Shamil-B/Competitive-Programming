class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        # build the graph 
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        contributions = defaultdict(int)

        for st, end in trips:
            q = [(st,[])]
            visited = set()
            bigPath = []
            while q:
                node, path = q.pop()

                if node in visited:
                    continue

                visited.add(node)
                path.append(node)
                if node == end:
                    bigPath = path[:]
                    break

                for neig in graph[node]:
                    q.append((neig,path[:]))

            for element in bigPath:
                contributions[element] += 1
                
        @cache          
        def solve(node, canHalve, parent):
            used = inf
            if canHalve:
                # used my half 
                used = (price[node]//2)*contributions[node]
                for neig in graph[node]:
                    if neig != parent:
                        used += solve(neig, False, node)

            # not used my half
            notUsed = (price[node])*contributions[node]
            for neig in graph[node]:
                if neig != parent:
                    notUsed += solve(neig, True, node)

            return min(used, notUsed)
            
        return solve(0,True,-1)