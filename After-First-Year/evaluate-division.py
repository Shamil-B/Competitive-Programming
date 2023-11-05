class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        def dfs(start, end, val, visited = None):
            if not visited:
                visited = set()

            if start in visited:
                return 0

            visited.add(start)
            if start == end:
                return val

            if not graph[start]:
                return 0

            for neig, value in graph[start]:
                res = dfs(neig, end, value, visited)
                if res:
                    return val * res

            return 0

        graph = defaultdict(list)
        for index, equation in enumerate(equations):
            u, v = equation
            
            graph[u].append((v,values[index]))
            graph[v].append((u,1/values[index]))
            
            
        answer = [-1]*len(queries)
        for index, query in enumerate(queries):
            start, end = query 
            if start in graph and end in graph:
                if start == end:
                    answer[index] = 1
                else:
                    res = dfs(start, end, 1)
                    if res:
                        answer[index] = res

        return answer
            