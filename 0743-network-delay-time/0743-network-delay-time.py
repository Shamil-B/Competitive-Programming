class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def dijkstraDistance(start,edges):
            graph = defaultdict(list)
            for node1, node2, weight in edges:
                graph[node1].append((node2,weight))

            distances = {}
            q = [(0, start)]
            heapq.heapify(q)
            visited = set()

            while q:
                costSoFar, node = heapq.heappop(q)
                if node in visited:
                    continue

                visited.add(node)
                distances[node] = costSoFar
                for neig, weight in graph[node]:
                    heapq.heappush(q,(costSoFar+weight, neig))

            if len(distances) < n:
                return -1
            return max(list(distances.values()))
        
        return dijkstraDistance(k,times)